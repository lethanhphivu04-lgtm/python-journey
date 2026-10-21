/**
 * Vua Cóc Battle Arena - Game Engine (2D Pond & 1D Classic)
 * Tích hợp Web Audio API, Local 2-Player, A* AI, và Replay Timeline.
 */

// ==============================================================================
// 1. SYNTHESIZED SOUND EFFECTS ENGINE (WEB AUDIO API - ZERO EXTERNAL ASSETS)
// ==============================================================================
let audioCtx = null;
let soundEnabled = true;

function initAudio() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    audioCtx = new AudioContext();
  }
  if (audioCtx.state === "suspended") {
    audioCtx.resume();
  }
}

function playSound(type) {
  if (!soundEnabled) return;
  try {
    initAudio();
    const now = audioCtx.currentTime;

    if (type === "hop") {
      // Am thanh coc nhay boing
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(180, now);
      osc.frequency.exponentialRampToValueAtTime(360, now + 0.1);
      osc.frequency.exponentialRampToValueAtTime(240, now + 0.18);
      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.18);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.18);
    } else if (type === "eat") {
      // Am thanh an ruoi vang ting ting
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = "triangle";
      osc.frequency.setValueAtTime(587.33, now); // D5
      osc.frequency.setValueAtTime(880, now + 0.08); // A5
      gain.gain.setValueAtTime(0.25, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.25);
    } else if (type === "rock") {
      // Am thanh cham da
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = "square";
      osc.frequency.setValueAtTime(120, now);
      osc.frequency.exponentialRampToValueAtTime(40, now + 0.12);
      gain.gain.setValueAtTime(0.2, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.12);
    } else if (type === "win") {
      // Khuc nhac chien thang
      const notes = [523.25, 659.25, 783.99, 1046.5]; // C E G C
      notes.forEach((freq, idx) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = "triangle";
        osc.frequency.setValueAtTime(freq, now + idx * 0.12);
        gain.gain.setValueAtTime(0.3, now + idx * 0.12);
        gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.12 + 0.2);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + idx * 0.12);
        osc.stop(now + idx * 0.12 + 0.2);
      });
    }
  } catch (e) {
    // Audio context fallback
  }
}

document.getElementById("btnSoundToggle").addEventListener("click", () => {
  soundEnabled = !soundEnabled;
  document.getElementById("soundIcon").textContent = soundEnabled ? "🔊" : "🔇";
  if (soundEnabled) playSound("hop");
});

// ==============================================================================
// 2. STATE TOAN CUC VA CAU HINH
// ==============================================================================
const state = {
  arenaMode: "2D", // "2D" hoac "1D"
  activeTab: "singleplayer",
  // 2D Game State
  game2D: null,
  pvpQueuedActionA: null, // Dung de dong bo luot trong PvP
  // 1D Game State
  game1D: {
    turn: 1,
    maxTurns: 6,
    state: { bot_a_position: 0, bot_b_position: 4 },
    history: [],
    isFinished: false,
  },
  // Replay
  replay: {
    mode: "2D",
    turns: [],
    initialState: null,
    currentIndex: 0,
    isPlaying: false,
    timer: null,
  },
};

// DOM Elements
const grid2D = document.getElementById("grid2D");
const view2D = document.getElementById("view2D");
const view1D = document.getElementById("view1D");
const boardTrack1D = document.getElementById("boardTrack1D");
const boardTitle = document.getElementById("boardTitle");
const turnBadge = document.getElementById("turnBadge");
const scoreA = document.getElementById("scoreA");
const scoreB = document.getElementById("scoreB");
const statusBanner = document.getElementById("statusBanner");
const aiThoughtDisplay = document.getElementById("aiThoughtDisplay");
const turnLogBody = document.getElementById("turnLogBody");
const replayScrubber = document.getElementById("replayScrubber");
const timelineSlider = document.getElementById("timelineSlider");

// ==============================================================================
// 3. ENGINE BAN CO 2D (5X5 LOTUS POND)
// ==============================================================================
async function initNewGame2D() {
  try {
    const res = await fetch("/api/2d/new");
    const data = await res.json();
    if (data.success) {
      state.game2D = data.game;
      state.replay.mode = "2D";
      state.replay.turns = [];
      state.replay.initialState = JSON.parse(JSON.stringify(data.game));
      state.replay.currentIndex = 0;
      replayScrubber.style.display = "none";
      render2DBoard();
      updateHUD();
      clearTurnLog();
      updateStatusBanner("in_progress", "Trận đấu 2D bắt đầu! Dùng phím WASD hoặc Mũi Tên để di chuyển.");
    }
  } catch (err) {
    console.error("Loi khoi tao 2D:", err);
  }
}

function render2DBoard() {
  if (!state.game2D) return;
  const g = state.game2D;
  grid2D.innerHTML = "";

  const rocksMap = new Set(g.rocks.map((r) => `${r.x},${r.y}`));
  const fliesMap = new Set(g.flies.map((f) => `${f.x},${f.y}`));
  const posA = `${g.frog_a.x},${g.frog_a.y}`;
  const posB = `${g.frog_b.x},${g.frog_b.y}`;
  const goalA = `${g.frog_a.goal.x},${g.frog_a.goal.y}`;
  const goalB = `${g.frog_b.goal.x},${g.frog_b.goal.y}`;

  for (let y = 0; y < g.grid_size; y++) {
    for (let x = 0; x < g.grid_size; x++) {
      const coord = `${x},${y}`;
      const cell = document.createElement("div");
      cell.className = "cell-2d pad";
      cell.id = `cell_${x}_${y}`;

      // Goal markings
      if (coord === goalA) {
        cell.classList.add("goal-a");
        cell.innerHTML += `<div class="goal-label-2d">ĐÍCH A</div>`;
      }
      if (coord === goalB) {
        cell.classList.add("goal-b");
        cell.innerHTML += `<div class="goal-label-2d">ĐÍCH B</div>`;
      }

      // Obstacles
      if (rocksMap.has(coord)) {
        cell.className = "cell-2d rock";
        cell.innerHTML = `<span class="rock-token">🪨</span>`;
      }

      // Bonus flies
      if (fliesMap.has(coord)) {
        cell.innerHTML += `<span class="fly-token">🪰</span>`;
      }

      // Frogs
      if (coord === posA && coord === posB) {
        cell.innerHTML += `<div style="display:flex;gap:2px;"><span class="frog-avatar hop">🐸</span><span class="frog-avatar hop">🐸</span></div>`;
      } else if (coord === posA) {
        cell.innerHTML += `<span class="frog-avatar hop" title="Ếch A (Bạn)">🐸</span>`;
      } else if (coord === posB) {
        cell.innerHTML += `<span class="frog-avatar hop" title="Ếch B">🐸</span>`;
      }

      grid2D.appendChild(cell);
    }
  }
}

function updateHUD() {
  if (state.arenaMode === "2D" && state.game2D) {
    const g = state.game2D;
    scoreA.textContent = `${g.frog_a.score} Điểm`;
    scoreB.textContent = `${g.frog_b.score} Điểm`;
    turnBadge.textContent = `Lượt: ${g.current_turn} / ${g.max_turns}`;
  } else {
    scoreA.textContent = `Vị trí: ${state.game1D.state.bot_a_position}`;
    scoreB.textContent = `Vị trí: ${state.game1D.state.bot_b_position}`;
    turnBadge.textContent = `Lượt: ${state.game1D.turn} / ${state.game1D.maxTurns}`;
  }
}

async function play2DStep(actionA, actionB = "wait", mode = "pve") {
  if (!state.game2D || state.game2D.is_finished) return;

  playSound("hop");

  try {
    const res = await fetch("/api/2d/step", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        game: state.game2D,
        action_a: actionA,
        action_b: actionB,
        mode: mode,
      }),
    });
    const data = await res.json();
    if (!data.success) {
      alert("Lỗi: " + data.error);
      return;
    }

    const prevFliesCount = state.game2D.flies.length;
    state.game2D = data.game;
    const log = data.turn_log;

    // Kiem tra am thanh an ruoi
    if (data.game.flies.length < prevFliesCount) {
      playSound("eat");
    }

    // Luu replay
    state.replay.turns.push(log);

    // Render va cap nhat
    render2DBoard();
    updateHUD();
    append2DTurnLog(log);

    if (log.thought_b) {
      aiThoughtDisplay.textContent = `AI: "${log.thought_b}"`;
    }

    if (data.game.is_finished) {
      playSound("win");
      show2DEndGame(data.game);
      setupReplay(state.replay.turns, state.replay.initialState);
      replayScrubber.style.display = "flex";
    }
  } catch (e) {
    console.error("Loi step 2D:", e);
  }
}

function show2DEndGame(game) {
  if (game.winner === "A") {
    updateStatusBanner("completed-win-a", `🏆 ẾCH A CHIẾN THẮNG! Điểm: ${game.frog_a.score}đ vs ${game.frog_b.score}đ. (${game.reason})`);
  } else if (game.winner === "B") {
    updateStatusBanner("completed-win-b", `🏆 ẾCH B CHIẾN THẮNG! Điểm: ${game.frog_b.score}đ vs ${game.frog_a.score}đ. (${game.reason})`);
  } else {
    updateStatusBanner("completed-draw", `🤝 TRẬN ĐẤU HÒA NHAU! (${game.reason})`);
  }
}

// D-Pad and Button Listeners
document.getElementById("btnUp").addEventListener("click", () => handlePlayerAction("up"));
document.getElementById("btnDown").addEventListener("click", () => handlePlayerAction("down"));
document.getElementById("btnLeft").addEventListener("click", () => handlePlayerAction("left"));
document.getElementById("btnRight").addEventListener("click", () => handlePlayerAction("right"));
document.getElementById("btnWait").addEventListener("click", () => handlePlayerAction("wait"));
document.getElementById("btnNewGame").addEventListener("click", initNewGame2D);
document.getElementById("btnResetPvP").addEventListener("click", initNewGame2D);

function handlePlayerAction(action) {
  if (state.arenaMode === "2D") {
    if (state.activeTab === "pvp") {
      // Che do PvP: Luu action cua nguoi 1, cho nguoi 2
      state.pvpQueuedActionA = action;
      updateStatusBanner("in_progress", `🟢 Người 1 đã chọn '${action}'. 🟠 Đến lượt Người 2 bấm phím mũi tên!`);
    } else {
      play2DStep(action, "wait", "pve");
    }
  } else {
    // 1D Mode
    if (["left", "right", "wait"].includes(action)) {
      play1DStep(action);
    }
  }
}

// Keyboard controls
window.addEventListener("keydown", (e) => {
  // Neu dang go trong code editor thi khong bat phim game
  if (document.activeElement && document.activeElement.tagName === "TEXTAREA") return;

  const k = e.key.toLowerCase();

  if (state.arenaMode === "2D") {
    if (state.activeTab === "pvp") {
      // Nguoi 1: W A S D
      if (k === "w") { e.preventDefault(); state.pvpQueuedActionA = "up"; updateStatusBanner("in_progress", "🟢 P1: Lên. 🟠 Mời P2 bấm mũi tên!"); }
      else if (k === "s") { e.preventDefault(); state.pvpQueuedActionA = "down"; updateStatusBanner("in_progress", "🟢 P1: Xuống. 🟠 Mời P2 bấm mũi tên!"); }
      else if (k === "a") { e.preventDefault(); state.pvpQueuedActionA = "left"; updateStatusBanner("in_progress", "🟢 P1: Trái. 🟠 Mời P2 bấm mũi tên!"); }
      else if (k === "d") { e.preventDefault(); state.pvpQueuedActionA = "right"; updateStatusBanner("in_progress", "🟢 P1: Phải. 🟠 Mời P2 bấm mũi tên!"); }
      else if (k === " ") { e.preventDefault(); state.pvpQueuedActionA = "wait"; updateStatusBanner("in_progress", "🟢 P1: Chờ. 🟠 Mời P2 bấm mũi tên!"); }

      // Nguoi 2: Phim mui ten
      let actB = null;
      if (e.key === "ArrowUp") actB = "up";
      else if (e.key === "ArrowDown") actB = "down";
      else if (e.key === "ArrowLeft") actB = "left";
      else if (e.key === "ArrowRight") actB = "right";
      else if (e.key === "Enter" || e.key === "0") actB = "wait";

      if (actB) {
        e.preventDefault();
        const actA = state.pvpQueuedActionA || "wait";
        state.pvpQueuedActionA = null;
        play2DStep(actA, actB, "pvp");
      }
    } else if (state.activeTab === "singleplayer") {
      // Single player: chap nhan ca WASD va Arrow Keys
      if (k === "w" || e.key === "ArrowUp") { e.preventDefault(); play2DStep("up", "wait", "pve"); }
      else if (k === "s" || e.key === "ArrowDown") { e.preventDefault(); play2DStep("down", "wait", "pve"); }
      else if (k === "a" || e.key === "ArrowLeft") { e.preventDefault(); play2DStep("left", "wait", "pve"); }
      else if (k === "d" || e.key === "ArrowRight") { e.preventDefault(); play2DStep("right", "wait", "pve"); }
      else if (k === " " || k === "x") { e.preventDefault(); play2DStep("wait", "wait", "pve"); }
    }
  } else {
    // 1D Mode
    if (k === "a" || e.key === "ArrowLeft") { e.preventDefault(); play1DStep("left"); }
    else if (k === "d" || e.key === "ArrowRight") { e.preventDefault(); play1DStep("right"); }
    else if (k === " " || k === "s" || e.key === "ArrowDown") { e.preventDefault(); play1DStep("wait"); }
  }
});

// ==============================================================================
// 4. CHUYEN DOI CHE DO 2D POND VA 1D CLASSIC
// ==============================================================================
const btnMode2D = document.getElementById("btnMode2D");
const btnMode1D = document.getElementById("btnMode1D");

btnMode2D.addEventListener("click", () => {
  btnMode2D.classList.add("active");
  btnMode1D.classList.remove("active");
  state.arenaMode = "2D";
  view2D.style.display = "block";
  view1D.style.display = "none";
  document.getElementById("dpad2D").style.display = "grid";
  document.getElementById("controls1D").style.display = "none";
  boardTitle.textContent = "🪷 Đầm Sen Đại Chiến 5x5";
  if (!state.game2D) initNewGame2D();
  else { render2DBoard(); updateHUD(); }
});

btnMode1D.addEventListener("click", () => {
  btnMode1D.classList.add("active");
  btnMode2D.classList.remove("active");
  state.arenaMode = "1D";
  view2D.style.display = "none";
  view1D.style.display = "block";
  document.getElementById("dpad2D").style.display = "none";
  document.getElementById("controls1D").style.display = "flex";
  boardTitle.textContent = "📏 Bàn Đua Lá Sen Cổ Điển (0 ➔ 4)";
  render1DBoard(state.game1D.state.bot_a_position, state.game1D.state.bot_b_position);
  updateHUD();
});

// 1D Board initialization
function init1DBoard() {
  boardTrack1D.innerHTML = "";
  for (let i = 0; i <= 4; i++) {
    const pad = document.createElement("div");
    pad.className = "pad-cell";
    pad.id = `pad1D_${i}`;
    let badge = i === 0 ? `<span class="pad-target target-b">ĐÍCH B</span>` : i === 4 ? `<span class="pad-target target-a">ĐÍCH A</span>` : "";
    pad.innerHTML = `
      <div class="pad-header"><span class="pad-label">Ô ${i}</span>${badge}</div>
      <div class="pad-frogs" id="frogs1D_${i}"></div>
      <div style="font-size:10px;color:var(--text-light);">${i === 0 ? "Xuất phát A" : i === 4 ? "Xuất phát B" : ""}</div>
    `;
    boardTrack1D.appendChild(pad);
  }
}

function render1DBoard(posA, posB) {
  for (let i = 0; i <= 4; i++) {
    const pad = document.getElementById(`pad1D_${i}`);
    const frogContainer = document.getElementById(`frogs1D_${i}`);
    if (!pad || !frogContainer) continue;
    frogContainer.innerHTML = "";
    pad.className = "pad-cell";

    if (posA === i && posB === i) pad.classList.add("active-both");
    else if (posA === i) pad.classList.add("active-a");
    else if (posB === i) pad.classList.add("active-b");

    if (posA === i) frogContainer.innerHTML += `<div class="frog-token frog-a">🐸 Ếch A</div>`;
    if (posB === i) frogContainer.innerHTML += `<div class="frog-token frog-b">🐸 Ếch B</div>`;
  }
}

async function play1DStep(action) {
  if (state.game1D.isFinished) return;
  playSound("hop");
  try {
    const res = await fetch("/api/step", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        state: state.game1D.state,
        turn: state.game1D.turn,
        max_turns: state.game1D.maxTurns,
        action: action,
        opponent: "cautious",
      }),
    });
    const data = await res.json();
    if (!data.success) return;

    state.game1D.history.push(data.turn_record);
    state.game1D.state = data.new_state;
    state.game1D.turn = data.next_turn;

    render1DBoard(data.new_state.bot_a_position, data.new_state.bot_b_position);
    updateHUD();
    append1DTurnLog(data.turn_record);

    if (data.status === "completed") {
      state.game1D.isFinished = true;
      playSound("win");
      updateStatusBanner(data.winner === "A" ? "completed-win-a" : data.winner === "B" ? "completed-win-b" : "completed-draw",
        `Trận đấu 1D kết thúc! Người thắng: ${data.winner || "Hòa"}. (${data.reason})`
      );
    }
  } catch (e) {
    console.error("Loi 1D step:", e);
  }
}

document.getElementById("btn1DLeft").addEventListener("click", () => play1DStep("left"));
document.getElementById("btn1DWait").addEventListener("click", () => play1DStep("wait"));
document.getElementById("btn1DRight").addEventListener("click", () => play1DStep("right"));

// ==============================================================================
// 5. CHUYEN DOI TAB CHUC NANG
// ==============================================================================
document.querySelectorAll(".tab-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab-btn").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    const t = btn.getAttribute("data-tab");
    state.activeTab = t;

    document.querySelectorAll(".mode-panel").forEach((p) => (p.style.display = "none"));
    if (t === "singleplayer") document.getElementById("panelSingle").style.display = "block";
    else if (t === "pvp") document.getElementById("panelPvP").style.display = "block";
    else if (t === "duel") document.getElementById("panelDuel").style.display = "block";
    else if (t === "tournament") document.getElementById("panelTournament").style.display = "block";
    else if (t === "editor") document.getElementById("panelEditor").style.display = "block";
  });
});

// ==============================================================================
// 6. TOURNAMENT VA CODE TESTING
// ==============================================================================
document.getElementById("btnRunTournament").addEventListener("click", async () => {
  const btn = document.getElementById("btnRunTournament");
  btn.disabled = true;
  btn.textContent = "⏳ Đang thi đấu giải...";

  const customCode = document.getElementById("customBotCode").value;
  try {
    const res = await fetch("/api/tournament", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ custom_code: customCode }),
    });
    const data = await res.json();
    btn.disabled = false;
    btn.textContent = "▶ Chạy Lại Giải Đấu";
    if (data.success) {
      playSound("win");
      renderTournamentTable(data);
    }
  } catch (e) {
    btn.disabled = false;
    btn.textContent = "▶ Chạy Toàn Bộ Giải Đấu";
  }
});

function renderTournamentTable(data) {
  const summaryBox = document.getElementById("tournamentSummary");
  const s = data.summary;
  summaryBox.style.display = "grid";
  summaryBox.style.gridTemplateColumns = "repeat(4, 1fr)";
  summaryBox.style.gap = "8px";
  summaryBox.innerHTML = `
    <div style="background:#eaf3ec;padding:10px;border-radius:6px;text-align:center;">
      <div style="font-size:18px;font-weight:700;color:var(--primary);">${s.matches}</div>
      <div style="font-size:11px;">Tổng trận</div>
    </div>
    <div style="background:#d3f9d8;padding:10px;border-radius:6px;text-align:center;">
      <div style="font-size:18px;font-weight:700;color:#2b8a3e;">${s.wins}</div>
      <div style="font-size:11px;">Thắng</div>
    </div>
    <div style="background:#fff3bf;padding:10px;border-radius:6px;text-align:center;">
      <div style="font-size:18px;font-weight:700;color:#d97706;">${s.draws}</div>
      <div style="font-size:11px;">Hòa</div>
    </div>
    <div style="background:#ffe3e3;padding:10px;border-radius:6px;text-align:center;">
      <div style="font-size:18px;font-weight:700;color:#c92a2a;">${s.losses}</div>
      <div style="font-size:11px;">Thua</div>
    </div>
  `;

  const tbody = document.getElementById("tournamentTableBody");
  tbody.innerHTML = "";
  data.standings.forEach((r) => {
    const tr = document.createElement("tr");
    const badge = r.outcome === "win" ? "badge-win" : r.outcome === "loss" ? "badge-loss" : "badge-draw";
    tr.innerHTML = `
      <td><strong>${r.opponent}</strong></td>
      <td>Ghế ${r.student_seat}</td>
      <td><span class="standings-badge ${badge}">${r.outcome.toUpperCase()}</span></td>
      <td>${r.turns}</td>
      <td>${r.student_legal_actions}/${r.student_action_attempts}</td>
      <td style="font-size:12px;color:var(--text-muted);">${r.reason}</td>
    `;
    tbody.appendChild(tr);
  });
}

document.getElementById("btnTestCode").addEventListener("click", async () => {
  const code = document.getElementById("customBotCode").value;
  const feedback = document.getElementById("codeFeedback");
  feedback.style.display = "block";
  feedback.innerHTML = "⏳ Đang kiểm tra...";

  try {
    const res = await fetch("/api/test-bot", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: code }),
    });
    const data = await res.json();
    if (data.success) {
      playSound("eat");
      feedback.style.color = "var(--primary)";
      feedback.style.background = "var(--primary-light)";
      feedback.style.padding = "8px";
      feedback.style.borderRadius = "6px";
      feedback.innerHTML = `✅ ${data.message}`;
    } else {
      playSound("rock");
      feedback.style.color = "#c92a2a";
      feedback.style.background = "#ffe3e3";
      feedback.style.padding = "8px";
      feedback.style.borderRadius = "6px";
      feedback.innerHTML = `❌ ${data.error}`;
    }
  } catch (e) {
    feedback.innerHTML = "❌ Lỗi: " + e;
  }
});

// ==============================================================================
// 7. REPLAY SCRUBBER VA NHAT KY
// ==============================================================================
function setupReplay(turns, initialState) {
  state.replay.turns = turns;
  state.replay.initialState = initialState;
  state.replay.currentIndex = 0;
  timelineSlider.min = 0;
  timelineSlider.max = turns.length;
  timelineSlider.value = 0;
}

function clearTurnLog() {
  turnLogBody.innerHTML = "";
}

function append2DTurnLog(log) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td><strong>#${log.turn}</strong></td>
    <td><span style="color:var(--primary);font-weight:600;">${log.action_a}</span> (${log.pos_a[0]},${log.pos_a[1]})</td>
    <td><span style="color:var(--accent);font-weight:600;">${log.action_b}</span> (${log.pos_b[0]},${log.pos_b[1]})</td>
    <td>A: ${log.score_a}đ | B: ${log.score_b}đ</td>
  `;
  turnLogBody.appendChild(tr);
}

function append1DTurnLog(t) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td><strong>#${t.turn_number}</strong></td>
    <td><span style="color:var(--primary);font-weight:600;">${t.bot_a_action}</span></td>
    <td><span style="color:var(--accent);font-weight:600;">${t.bot_b_action}</span></td>
    <td>A: ${t.state_after.bot_a_position} | B: ${t.state_after.bot_b_position}</td>
  `;
  turnLogBody.appendChild(tr);
}

function updateStatusBanner(type, msg) {
  statusBanner.className = `status-banner status-${type}`;
  statusBanner.innerHTML = msg;
}

// Download replay JSON
document.getElementById("btnDownloadReplay").addEventListener("click", () => {
  const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `vuacoc_replay_${Date.now()}.json`;
  a.click();
  URL.revokeObjectURL(url);
});

// Khoi chay ban dau
init1DBoard();
initNewGame2D();

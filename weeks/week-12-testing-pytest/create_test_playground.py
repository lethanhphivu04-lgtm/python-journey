"""Script to generate a multi-folder test playground with a configurable failure rate."""

from pathlib import Path
import random

PLAYGROUND_DIR = Path(__file__).resolve().parent / "playground"

# Seed for reproducible yet interesting results
random.seed(42)

MODULES = {
    "math_core": [
        ("test_basic_math.py", [
            ("test_addition", "assert 10 + 20 == 30", "assert 10 + 20 == 35"),
            ("test_subtraction", "assert 50 - 15 == 35", "assert 50 - 15 == 40"),
            ("test_multiplication", "assert 6 * 7 == 42", "assert 6 * 7 == 40"),
            ("test_integer_division", "assert 10 // 3 == 3", "assert 10 // 3 == 4"),
        ]),
        ("test_statistics.py", [
            ("test_mean_value", "assert sum([2, 4, 6]) / 3 == 4.0", "assert sum([2, 4, 6]) / 3 == 5.0"),
            ("test_median_odd", "assert sorted([1, 9, 5])[1] == 5", "assert sorted([1, 9, 5])[1] == 9"),
            ("test_min_max_spread", "assert max([3, 10, 7]) - min([3, 10, 7]) == 7", "assert max([3, 10, 7]) - min([3, 10, 7]) == 6"),
        ]),
        ("test_geometry.py", [
            ("test_rectangle_area", "assert 5 * 8 == 40", "assert 5 * 8 == 45"),
            ("test_perimeter", "assert 2 * (4 + 6) == 20", "assert 2 * (4 + 6) == 22"),
            ("test_square_diagonal_squared", "assert 3**2 + 4**2 == 25", "assert 3**2 + 4**2 == 20"),
        ]),
        ("test_algebra.py", [
            ("test_linear_equation", "x = 5; assert 2 * x + 3 == 13", "x = 5; assert 2 * x + 3 == 15"),
            ("test_power_of_two", "assert 2**8 == 256", "assert 2**8 == 512"),
            ("test_absolute_difference", "assert abs(-15) == 15", "assert abs(-15) == -15"),
        ]),
    ],
    "bot_ai": [
        ("test_navigation.py", [
            ("test_move_forward", "pos = 0; pos += 1; assert pos == 1", "pos = 0; pos += 1; assert pos == 2"),
            ("test_boundary_limit", "pos = 100; assert min(pos + 10, 100) == 100", "pos = 100; assert pos + 10 == 100"),
            ("test_turn_around", "direction = 'N'; assert {'N': 'S'}[direction] == 'S'", "direction = 'N'; assert {'N': 'S'}[direction] == 'W'"),
        ]),
        ("test_combat.py", [
            ("test_damage_calculation", "hp = 100; hp -= 25; assert hp == 75", "hp = 100; hp -= 25; assert hp == 80"),
            ("test_shield_block", "shield = 50; dmg = 30; assert shield - dmg == 20", "shield = 50; dmg = 30; assert shield - dmg == 15"),
            ("test_is_alive", "hp = 10; assert (hp > 0) is True", "hp = 0; assert (hp > 0) is True"),
        ]),
        ("test_inventory.py", [
            ("test_bag_capacity", "bag = ['potion', 'sword']; assert len(bag) == 2", "bag = ['potion', 'sword']; assert len(bag) == 3"),
            ("test_has_key", "items = {'bronze_key', 'shield'}; assert 'bronze_key' in items", "items = {'shield'}; assert 'bronze_key' in items"),
            ("test_gold_coins", "gold = 150; gold += 50; assert gold == 200", "gold = 150; gold += 50; assert gold == 250"),
        ]),
        ("test_dialogue.py", [
            ("test_npc_greeting", "msg = 'Hello Traveler'; assert 'Hello' in msg", "msg = 'Go away'; assert 'Hello' in msg"),
            ("test_quest_trigger", "quest_accepted = True; assert quest_accepted is True", "quest_accepted = False; assert quest_accepted is True"),
        ]),
    ],
    "user_auth": [
        ("test_login.py", [
            ("test_valid_credentials", "status = 200; assert status == 200", "status = 401; assert status == 200"),
            ("test_locked_after_5_tries", "tries = 5; assert tries >= 5", "tries = 3; assert tries >= 5"),
            ("test_remember_me_cookie", "cookie = {'token': 'xyz'}; assert 'token' in cookie", "cookie = {}; assert 'token' in cookie"),
        ]),
        ("test_password_hash.py", [
            ("test_hash_length", "h = 'a' * 64; assert len(h) == 64", "h = 'a' * 32; assert len(h) == 64"),
            ("test_salt_differs", "s1, s2 = 'salt1', 'salt2'; assert s1 != s2", "s1, s2 = 'salt1', 'salt1'; assert s1 != s2"),
        ]),
        ("test_roles.py", [
            ("test_admin_privilege", "roles = ['admin', 'editor']; assert 'admin' in roles", "roles = ['viewer']; assert 'admin' in roles"),
            ("test_guest_restriction", "can_delete = False; assert can_delete is False", "can_delete = True; assert can_delete is False"),
        ]),
        ("test_session.py", [
            ("test_session_active", "ttl = 300; assert ttl > 0", "ttl = -1; assert ttl > 0"),
            ("test_token_not_empty", "token = 'jwt.payload.sig'; assert bool(token) is True", "token = ''; assert bool(token) is True"),
        ]),
    ],
    "e_commerce": [
        ("test_cart.py", [
            ("test_add_to_cart", "cart = [19.99, 5.00]; assert sum(cart) == 24.99", "cart = [19.99, 5.00]; assert sum(cart) == 30.00"),
            ("test_item_count", "items = ['book', 'pen']; assert len(items) == 2", "items = ['book', 'pen']; assert len(items) == 3"),
            ("test_empty_cart", "cart = []; assert len(cart) == 0", "cart = [1]; assert len(cart) == 0"),
        ]),
        ("test_discounts.py", [
            ("test_coupon_10_percent", "price = 100 * 0.9; assert price == 90.0", "price = 100 * 0.8; assert price == 90.0"),
            ("test_vip_free_shipping", "shipping = 0.0; assert shipping == 0.0", "shipping = 5.0; assert shipping == 0.0"),
        ]),
        ("test_checkout.py", [
            ("test_vat_tax", "tax = 100 * 0.10; assert tax == 10.0", "tax = 100 * 0.15; assert tax == 10.0"),
            ("test_payment_success", "res = 'SUCCESS'; assert res == 'SUCCESS'", "res = 'FAILED'; assert res == 'SUCCESS'"),
        ]),
        ("test_inventory_stock.py", [
            ("test_stock_decreased", "stock = 10; stock -= 1; assert stock == 9", "stock = 10; stock -= 1; assert stock == 10"),
            ("test_out_of_stock_flag", "stock = 0; assert stock <= 0", "stock = 5; assert stock <= 0"),
        ]),
    ],
    "network_api": [
        ("test_http_status.py", [
            ("test_get_ok", "status = 200; assert status == 200", "status = 404; assert status == 200"),
            ("test_created", "status = 201; assert status == 201", "status = 500; assert status == 201"),
            ("test_not_found", "status = 404; assert status == 404", "status = 200; assert status == 404"),
        ]),
        ("test_payload_parser.py", [
            ("test_json_mime_type", "mime = 'application/json'; assert 'json' in mime", "mime = 'text/plain'; assert 'json' in mime"),
            ("test_content_length", "body = 'hello'; assert len(body) == 5", "body = 'hello'; assert len(body) == 10"),
        ]),
        ("test_rate_limiter.py", [
            ("test_under_limit", "req_count = 8; assert req_count <= 10", "req_count = 15; assert req_count <= 10"),
            ("test_cool_down", "cooldown = 0; assert cooldown == 0", "cooldown = 3; assert cooldown == 0"),
        ]),
        ("test_retry_mechanism.py", [
            ("test_max_retries", "retries = 3; assert retries <= 3", "retries = 5; assert retries <= 3"),
            ("test_exponential_backoff", "delay = 2**2; assert delay == 4", "delay = 2**2; assert delay == 6"),
        ]),
    ],
}


def generate_playground(fail_probability: float = 0.25) -> None:
    """Generate 20 test files in 5 modules with a specified failure probability."""
    total_tests = 0
    failing_tests = 0

    for module_name, test_files in MODULES.items():
        module_dir = PLAYGROUND_DIR / module_name
        module_dir.mkdir(parents=True, exist_ok=True)

        for filename, test_cases in test_files:
            file_path = module_dir / filename
            lines = [f'"""Auto-generated tests for {module_name} -> {filename}."""\n']

            for test_name, pass_code, fail_code in test_cases:
                total_tests += 1
                should_fail = random.random() < fail_probability
                if should_fail:
                    failing_tests += 1
                    code = fail_code
                    doc = "Deliberate failing test for demonstration."
                else:
                    code = pass_code
                    doc = "Passing test."

                lines.append(f"\ndef {test_name}() -> None:\n    \"\"\"{doc}\"\"\"\n    {code}\n")

            file_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated {len(MODULES)} modules, 20 files, {total_tests} test cases.")
    print(f"Deliberate failures: {failing_tests} (~{fail_probability*100:.0f}% chance).")
    print(f"Playground location: {PLAYGROUND_DIR}")


if __name__ == "__main__":
    generate_playground(fail_probability=0.25)

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_profiles import validate


VALID = {
    "name": "Ada <script>alert(1)</script>",
    "github": "ada-lovelace",
    "favorite_language": "Python",
    "fun_fact": "Writes symbols, not raw HTML",
}


class ValidatorTests(unittest.TestCase):
    def run_case(self, files):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return validate(root)

    def profile(self, **changes):
        value = VALID | changes
        return json.dumps(value)

    def test_empty_directory(self):
        self.assertEqual(self.run_case({}), [])

    def test_valid_and_html_like_text(self):
        self.assertEqual(self.run_case({"ada-lovelace.json": self.profile()}), [])

    def test_malformed_json(self):
        self.assertTrue(self.run_case({"ada-lovelace.json": '{"name":"Ada" "github":"ada-lovelace"}'}))

    def test_missing_and_extra_keys(self):
        data = VALID.copy(); del data["fun_fact"]; data["extra"] = "no"
        self.assertTrue(self.run_case({"ada-lovelace.json": json.dumps(data)}))

    def test_wrong_type_empty_and_too_long(self):
        self.assertTrue(self.run_case({"ada-lovelace.json": self.profile(name=3)}))
        self.assertTrue(self.run_case({"ada-lovelace.json": self.profile(name=" ")}))
        self.assertTrue(self.run_case({"ada-lovelace.json": self.profile(fun_fact="x" * 181)}))

    def test_bad_handle_and_filename_mismatch(self):
        self.assertTrue(self.run_case({"other.json": self.profile(github="-bad-")}))
        self.assertTrue(self.run_case({"other.json": self.profile()}))

    def test_duplicate_case_insensitive(self):
        files = {"ada-lovelace.json": self.profile(), "duplicate.json": self.profile(github="ADA-LOVELACE")}
        self.assertTrue(self.run_case(files))

    def test_wrong_extension_and_subdirectory(self):
        self.assertTrue(self.run_case({"notes.txt": "no", "nested/profile.json": self.profile()}))


if __name__ == "__main__":
    unittest.main()

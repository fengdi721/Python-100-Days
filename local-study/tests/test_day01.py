"""Day 01 的验收测试；初始占位实现应产生10项报错。"""

import unittest

from exercises.day01 import normalize_tags


class NormalizeTagsTests(unittest.TestCase):
    def test_typical_tags(self):
        self.assertEqual(normalize_tags([" Python ", "python", "", "PHP", "php", "Node.js"]),
                         ["python", "php", "node.js"])

    def test_empty_list(self):
        self.assertEqual(normalize_tags([]), [])

    def test_blank_tags(self):
        self.assertEqual(normalize_tags(["", " ", "\n\t"]), [])

    def test_order_is_preserved(self):
        self.assertEqual(normalize_tags(["Z", "a", "B", "A", "z"]), ["z", "a", "b"])

    def test_unicode_casefold(self):
        self.assertEqual(normalize_tags(["Straße", "STRASSE", " 你好 ", "你好"]),
                         ["strasse", "你好"])

    def test_input_unchanged(self):
        original = [" Python ", "PYTHON", ""]
        before = original.copy()
        normalize_tags(original)
        self.assertEqual(original, before)

    def test_results_are_independent(self):
        source = ["python"]
        first = normalize_tags(source)
        first.append("new")
        self.assertEqual(normalize_tags(source), ["python"])
        self.assertEqual(source, ["python"])

    def test_rejects_non_list(self):
        with self.assertRaises(TypeError):
            normalize_tags("python")

    def test_rejects_tuple(self):
        with self.assertRaises(TypeError):
            normalize_tags(("python",))

    def test_rejects_non_string(self):
        with self.assertRaises(TypeError):
            normalize_tags(["python", 1])


if __name__ == "__main__":
    unittest.main()

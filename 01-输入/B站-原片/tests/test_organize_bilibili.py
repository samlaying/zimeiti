import tempfile
import unittest
from pathlib import Path

from organize_bilibili import classify_title, parse_srt, safe_filename


class OrganizeBilibiliTests(unittest.TestCase):
    def test_classification_rules(self):
        self.assertEqual(classify_title("Claude Code 实战：自动化写作"), "A")
        self.assertEqual(classify_title("产品经理需求分析与面试"), "B")
        self.assertEqual(classify_title("国产大模型横评与行业趋势"), "C")
        self.assertEqual(classify_title("阿里人才离职内幕"), "C")

    def test_parse_srt_removes_cues_and_tags(self):
        text = "1\n00:00:00,000 --> 00:00:01,000\n你好 <i>世界</i>\n\n2\n00:00:01,000 --> 00:00:02,000\n你好\n"
        self.assertEqual(parse_srt(text), "你好 世界")

    def test_safe_filename_is_bounded(self):
        name = safe_filename("标题 / 含有:非法*字符?" * 20)
        self.assertNotIn("/", name)
        self.assertLessEqual(len(name), 120)


if __name__ == "__main__":
    unittest.main()

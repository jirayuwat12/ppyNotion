import unittest
from ppyNotion.annotation import Annotation
from ppyNotion.type import ColorType


class TestAnnotation(unittest.TestCase):
    OBJ = {
            "bold": False,
            "italic": False,
            "strikethrough": True,
            "underline": False,
            "code": True,
            "color": "blue"
    }
    def test_empty_init(self):
        a = Annotation()
        self.assertFalse(a.bold)
        self.assertFalse(a.italic)
        self.assertFalse(a.code)
        self.assertFalse(a.strikethrough)
        self.assertFalse(a.underline)
        self.assertEqual(a.color, ColorType.default)

    def test_obj_init(self):
        a = Annotation(self.OBJ)
        self.assertFalse(a.bold)
        self.assertFalse(a.italic)
        self.assertTrue(a.strikethrough)
        self.assertFalse(a.underline)
        self.assertTrue(a.code)
        self.assertEqual(a.color, ColorType.blue)

    def test_change_field(self):
        a = Annotation(self.OBJ)
        # valid change
        a.bold = True
        self.assertTrue(a.bold)
        # invalid change
        with self.assertRaises(TypeError):
            a.bold = "True"
        # change by str
        with self.assertRaises(TypeError):
            a.color = "blue"
        a.set_color("pink")
        self.assertEqual(a.color, ColorType.pink)
if __name__ == "__main__":
    unittest.main()
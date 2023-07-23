'''
test `Annotation class
'''
import unittest
from ppyNotion.annotation import Annotation
from ppyNotion.type import ColorType


class TestAnnotation(unittest.TestCase):
    ''' test `Annotation class '''
    OBJ = {
        "bold": False,
        "italic": False,
        "strikethrough": True,
        "underline": False,
        "code": True,
        "color": "blue"
    }

    def test_empty_init(self):
        ''' test for empty obj initiation '''
        annotation_class = Annotation()
        self.assertFalse(annotation_class.bold)
        self.assertFalse(annotation_class.italic)
        self.assertFalse(annotation_class.code)
        self.assertFalse(annotation_class.strikethrough)
        self.assertFalse(annotation_class.underline)
        self.assertEqual(annotation_class.color, ColorType.default)

    def test_obj_init(self):
        ''' test with object from Notion API '''
        annotation_class = Annotation(self.OBJ)
        self.assertFalse(annotation_class.bold)
        self.assertFalse(annotation_class.italic)
        self.assertTrue(annotation_class.strikethrough)
        self.assertFalse(annotation_class.underline)
        self.assertTrue(annotation_class.code)
        self.assertEqual(annotation_class.color, ColorType.blue)

    def test_change_field(self):
        ''' test for change field both valid and invalid '''
        annotation_class = Annotation(self.OBJ)
        # valid change
        annotation_class.bold = True
        self.assertTrue(annotation_class.bold)
        # invalid change
        with self.assertRaises(TypeError):
            annotation_class.bold = "True"
        # change by str
        with self.assertRaises(TypeError):
            annotation_class.color = "blue"
        annotation_class.set_color("pink")
        self.assertEqual(annotation_class.color, ColorType.pink)

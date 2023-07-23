'''
test base text class
'''
import unittest
from ppyNotion.base_text import BaseText
from ppyNotion.type import BaseTextType
from ppyNotion.annotation import Annotation

class TestBaseText(unittest.TestCase):
    '''
    test base text class
    '''
    OBJ = {
      "type": "text",
      "text": {
        "content": "MTL Intern work timestamp",
        "link": None
      },
      "annotations": {
        "bold": False,
        "italic": True,
        "strikethrough": False,
        "underline": True,
        "code": False,
        "color": "default"
      },
      "plain_text": "MTL Intern work timestamp",
      "href": None
    }

    def test_empty_obj_init(self):
        ''' test with empty obj initiation '''
        base_text_var = BaseText()
        self.assertIsNone(base_text_var.type)
        self.assertIsInstance(base_text_var.annotations, Annotation)
        self.assertEqual(base_text_var.plain_text, str())
        self.assertEqual(base_text_var.href, str())

    def test_obj_init(self):
        ''' test with obj init '''
        base_text_var = BaseText(obj=self.OBJ)
        self.assertEqual(base_text_var.type, BaseTextType.text)
        self.assertEqual(base_text_var.annotations.bold, False)
        self.assertEqual(base_text_var.annotations.italic, True)
        self.assertEqual(base_text_var.annotations.strikethrough, False)
        self.assertEqual(base_text_var.annotations.underline, True)
        self.assertEqual(base_text_var.annotations.code, False)
        self.assertEqual(base_text_var.plain_text, "MTL Intern work timestamp")
        self.assertIsNone(base_text_var.href)
  
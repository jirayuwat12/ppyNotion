'''
    test `RichText` class
'''

import unittest
from ppyNotion.richtext import RichText
from ppyNotion.type import BaseTextType

class TestRichText(unittest.TestCase):
    ''' test `RichText` class '''
    OBJ = [
        {
            "type": "text",
            "text": {
                "content": "Hello world",
                "link": None
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default"
            },
            "plain_text": "Hello world",
            "href": None
        }
    ]
    def test_empty_init(self):
        ''' test initiation with empty object'''

    def test_obj_init(self):
        ''' test initiation with non-empty object'''
        rich_text_var = RichText(texts= self.OBJ)
        self.assertEqual(rich_text_var.rich_text[0].type,
                         BaseTextType.text)

    def test_edit_field(self):
        ''' test edit all field in class '''

    def test_to_object(self):
        ''' test `to_object` function '''

import unittest
from ppyNotion.text import Text
from ppyNotion.type import BaseTextType
from ppyNotion.annotation import Annotation
from ppyNotion.link import Link


class TestText(unittest.TestCase):
    ''' test `text` class '''
    TEXT = {
        "type": "text",
        "text": {
            "content": "inline link",
            "link": {
                "url": "https://developers.notion.com/"
            }
        },
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default"
        },
        "plain_text": "inline link",
        "href": "https://developers.notion.com/"
    }

    def test_empty_init(self):
        ''' test with empty object initiation '''
        text_var = Text()
        self.assertEqual(text_var.content, str())
        self.assertIsInstance(text_var.link, Link)

    def test_object_init(self):
        ''' test with object initiation '''
        text_var = Text(obj=self.TEXT)
        self.assertEqual(text_var.type,
                         BaseTextType.text)
        self.assertEqual(text_var.content,
                         self.TEXT['text']['content'])
        self.assertEqual(text_var.link.url,
                         self.TEXT['text']['link']['url'])
        self.assertIsInstance(text_var.annotations,
                              Annotation)
        self.assertEqual(text_var.plain_text,
                         self.TEXT['plain_text'])
        self.assertEqual(text_var.href,
                         self.TEXT['href'])

    def test_edit_field(self):
        ''' test edit all field in class '''
        text_var = Text()
        # edit content
        text_var.content = 'hello'
        self.assertEqual(text_var.content, 'hello')

        text_var.content = None
        self.assertIsNone(text_var.content)

        # edit link
        text_var.link = None
        self.assertIsNone(text_var.link)

        with self.assertRaises(TypeError):
            text_var.link = 'hello.com'

        url = r'https://google.com'
        text_var.set_link(link_value=url)
        self.assertIsInstance(text_var.link, Link)

    def test_to_object(self):
        ''' test `to_object` function '''
        text_var = Text(obj=self.TEXT)
        self.assertDictEqual(text_var.to_object(), self.TEXT)

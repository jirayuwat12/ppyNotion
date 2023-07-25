''' 
test `Emoji` class 
'''
import unittest
from ppyNotion.emoji import Emoji


class TestEmoji(unittest.TestCase):
    ''' test `Emoji` class '''
    OBJ = {
        "type": "emoji",
        "emoji": "😻"
    }

    def test_empty_init(self):
        ''' test with empty initiation '''
        emoji_var = Emoji()
        self.assertIsNone(emoji_var.emoji)

    def test_object_init(self):
        ''' test with object initiation '''
        emoji_var = Emoji(obj = self.OBJ)
        self.assertEqual(emoji_var.emoji, self.OBJ['emoji'])

        emoji_var = Emoji(obj = "🥨")
        self.assertEqual(emoji_var.emoji, "🥨")

    def test_edit_field(self):
        ''' test edit all field in class'''
        emoji_var = Emoji()
        emoji_var.emoji = "🥨"
        self.assertEqual(emoji_var.emoji, "🥨")

    def test_to_object(self):
        ''' test `to_object` function '''
        emoji_var = Emoji(obj = self.OBJ)
        self.assertDictEqual(emoji_var.to_object(), self.OBJ)

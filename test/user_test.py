'''
 test user class
'''
from ppyNotion.utils.user import user_id_2_object

import unittest
from ppyNotion.user import User
from ppyNotion.type import UserType

class TestUser(unittest.TestCase):
    ''' test user class '''
    PERSON = {
      "object": "user",
      "id": "d40e767c-d7af-4b18-a86d-55c61f1e39a4",
      "type": "person",
      "person": {
        "email": "avo@example.org",
      },
      "name": "Avocado Lovelace",
      "avatar_url": "https://secure.notion-static.com/e6a352a8-8381-44d0-a1dc-9ed80e62b53d.jpg",
    }
    BOT = {
      "object": "user",
      "id": "9a3b5ae0-c6e6-482d-b0e1-ed315ee6dc57",
      "type": "bot",
      "bot": {},
      "name": "Doug Engelbot",
      "avatar_url": "https://secure.notion-static.com/6720d746-3402-4171-8ebb-28d15144923c.jpg",
    }

    def test_empty_init(self):
        ''' test with empty initiation '''
        user_var = User()
        self.assertEqual(user_var.user_id, None)
        self.assertIsNone(user_var.type)
        self.assertEqual(user_var.name, None)
        self.assertEqual(user_var.avatar_url, None)
        self.assertEqual(user_var.bot, None)

    def test_obj_init(self):
        ''' test with object init '''
        # person user
        person_var = User(obj = self.PERSON)
        self.assertEqual(person_var.user_id,
                         self.PERSON['id'])
        self.assertEqual(person_var.type,
                         UserType.person)
        self.assertEqual(person_var.person_email,
                         self.PERSON['person']['email'])
        self.assertEqual(person_var.avatar_url,
                         self.PERSON['avatar_url'])
        # bot user
        bot_var = User(obj= self.BOT)
        self.assertEqual(bot_var.user_id,
                         self.BOT['id'])
        self.assertEqual(bot_var.type,
                         UserType.bot)
        self.assertEqual(bot_var.avatar_url,
                         self.BOT['avatar_url'])
        self.assertEqual(bot_var.bot,
                         dict())

    def test_to_object(self):
        ''' test to object function '''
        bot_var = User(obj = self.BOT)
        self.assertDictEqual(bot_var.to_object(),
                             self.BOT)

        person_var = User(obj = self.PERSON)
        self.assertDictEqual(person_var.to_object(),
                             self.PERSON)

        user_var = User(user_id= self.BOT['id'])
        self.assertDictEqual(user_var.to_object(),
                             user_id_2_object(self.BOT['id']))
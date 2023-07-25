''' test `Choice` class '''
import unittest
from ppyNotion.choice import Choice
from ppyNotion.type import ColorType

class TestChoice(unittest.TestCase):
    ''' test `Choice` class '''
    OBJ1 = {
        "id": "e28f74fc-83a7-4469-8435-27eb18f9f9de",
        "name": "🥦Vegetable",
        "color": "purple"
    }
    OBJ2 = {
        "id": "6132d771-b283-4cd9-ba44-b1ed30477c7f",
        "name": "🍎Fruit",
        "color": "red"
    }

    def test_empty_init(self):
        ''' test empty initiation '''
        choice_var = Choice()
        self.assertEqual(choice_var.color,
                         ColorType.default)
        self.assertEqual(choice_var.id,
                         str())
        self.assertEqual(choice_var.name,
                         str())

    def test_object_init(self):
        ''' test init with object '''
        choice_var = Choice(obj = self.OBJ1)
        self.assertEqual(choice_var.id,
                         self.OBJ1['id'])
        self.assertEqual(choice_var.name,
                         self.OBJ1['name'])
        self.assertEqual(choice_var.color,
                         ColorType.purple)

    def test_edit_field(self):
        ''' test edit all field in class '''
        choice_var = Choice()

        choice_var.id = self.OBJ1['id']
        self.assertEqual(choice_var.id, self.OBJ1['id'])

        choice_var.name = self.OBJ1['name']
        self.assertEqual(choice_var.name, self.OBJ1['name'])

        choice_var.color = ColorType.brown
        self.assertEqual(choice_var.color, ColorType.brown)

    def test_to_object_function(self):
        ''' test `to_object` function '''
        choice_var = Choice(obj = self.OBJ1)
        self.assertDictEqual(choice_var.to_object(), self.OBJ1)

        choice_var = Choice(obj = self.OBJ2)
        self.assertDictEqual(choice_var.to_object(), self.OBJ2)

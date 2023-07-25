'''
    test `Checkbox` class
'''
import unittest
from ppyNotion.checkbox import Checkbox
from ppyNotion.type import PropertyType

class TestCheckbox(unittest.TestCase):
    '''
        test `Checkbox` class
    '''
    OBJ1 = {
        "id": "ZI%40W",
        "type": "checkbox",
        "checkbox": True
    }
    OBJ2 = {
        "checkbox": True
    }

    def test_empty_init(self):
        ''' init with empty object '''
        checkbox_var = Checkbox()
        self.assertIsNone(checkbox_var.checkbox)
        self.assertEqual(checkbox_var.id,
                         str())
        self.assertIsNone(checkbox_var.type)

    def test_object_init(self):
        ''' init with non-empty object '''
        checkbox_var = Checkbox(obj = self.OBJ1)
        self.assertEqual(checkbox_var.id,
                         self.OBJ1['id'])
        self.assertEqual(checkbox_var.type,
                         PropertyType[self.OBJ1['type']])
        self.assertTrue(checkbox_var.checkbox)

        checkbox_var = Checkbox(obj = self.OBJ2)
        self.assertIsNone(checkbox_var.id)
        self.assertIsNone(checkbox_var.type)
        self.assertTrue(checkbox_var.checkbox)

    def test_edit_field(self):
        ''' edit all field in class '''
        checkbox_var = Checkbox()

        checkbox_var.id = '1234'
        self.assertEqual(checkbox_var.id,
                         '1234')

        checkbox_var.type = PropertyType.created_by
        self.assertEqual(checkbox_var.type,
                         PropertyType.created_by)

        checkbox_var.checkbox = False
        self.assertFalse(checkbox_var.checkbox)

    def test_to_object(self):
        ''' test `to_object` function '''
        checkbox_var = Checkbox()
        self.assertDictEqual(checkbox_var.to_object(),
                             dict())

        checkbox_var = Checkbox(obj = self.OBJ1)
        self.assertDictEqual(checkbox_var.to_object(),
                             self.OBJ1)

        checkbox_var = Checkbox(obj = self.OBJ2)
        self.assertDictEqual(checkbox_var.to_object(),
                             self.OBJ2)

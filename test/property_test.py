''' 
    test `Property` class 
'''
import unittest
from ppyNotion.property import Property
from ppyNotion.type import PropertyType

class TestProperty(unittest.TestCase):
    '''
        test `Property` class
    '''
    OBJ1 = {
        "id": "eB_%7D",
        "type": "created_time",
        "created_time": "2022-10-24T22:54:00.000Z"
    }
    OBJ2 = {
        "date": {
                "start": "2023-02-23"
            }
    }
    def test_empty_init(self):
        ''' test initiation with empty object '''
        property_var = Property()
        self.assertEqual(property_var.id,
                         str())
        self.assertIsNone(property_var.type)

    def test_object_init(self):
        ''' test initiation with non-empty object '''
        property_var = Property(obj = self.OBJ1)
        self.assertEqual(property_var.id,
                         self.OBJ1['id'])
        self.assertEqual(property_var.type,
                         PropertyType.created_time)

        property_var = Property(obj = self.OBJ2)
        self.assertIsNone(property_var.id)
        self.assertIsNone(property_var.type)

    def test_edit_field(self):
        ''' test edit all field in class '''
        property_var = Property()

        property_var.id = '1234'
        self.assertEqual(property_var.id,
                         '1234')

        property_var.type = PropertyType.email
        self.assertEqual(property_var.type,
                         PropertyType.email)

    def test_to_object(self):
        ''' test `to_object` function '''
        property_var = Property(obj = self.OBJ1)
        self.assertDictContainsSubset(property_var.to_object(),
                                      self.OBJ1)

        property_var = Property(obj = self.OBJ2)
        self.assertDictEqual(property_var.to_object(),
                             dict())

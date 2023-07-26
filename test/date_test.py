'''
    test `Date` class
'''
import unittest
from ppyNotion.date import Date
from ppyNotion.type import PropertyType

class TestDate(unittest.TestCase):
    '''
        test `Date` class
    '''
    OBJ1 = {
        "id": "M%3BBw",
        "type": "date",
        "date": {
            "start": "2023-02-07",
            "end": None,
            "time_zone": None
        }
    }
    OBJ2 = {
        "date": {
            "start": "2023-02-23"
        }
    }

    def test_empty_init(self):
        ''' test init with empty object '''
        date_var = Date()
        self.assertEqual(date_var.id,
                         None)
        self.assertEqual(date_var.type,
                         PropertyType.date)
        self.assertIsNone(date_var.start)
        self.assertIsNone(date_var.end)

    def test_object_init(self):
        ''' test init with non-empty object '''

    def test_edit_field(self):
        ''' test edit all field in class '''

    def test_to_object(self):
        ''' test `to_object` function '''

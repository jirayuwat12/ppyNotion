'''
test `Parent` class
'''
import unittest
from ppyNotion.parent import Parent


class TestParent(unittest.TestCase):
    ''' test `Parent` class '''
    OBJ1 = {
        "type": "workspace",
        "workspace": True
    }
    OBJ2 = {
        "type": "block_id",
        "block_id": "7d50a184-5bbe-4d90-8f29-6bec57ed817b"
    }

    def test_empty_init(self):
        ''' test empty initiation '''
        parent_var = Parent()
        self.assertEqual(parent_var.type,
                         str())
        self.assertIsNone(parent_var.data)

    def test_object_init(self):
        ''' test non-empty object initiation '''
        parent_var = Parent(obj=self.OBJ1)
        self.assertEqual(parent_var.type,
                         self.OBJ1['type'])
        self.assertEqual(parent_var.data,
                         True)

        parent_var = Parent(obj=self.OBJ2)
        self.assertEqual(parent_var.type,
                         self.OBJ2['type'])
        self.assertEqual(parent_var.data,
                         self.OBJ2[self.OBJ2['type']])

    def test_edit_field(self):
        ''' test edit all field in class '''
        parent_var = Parent()
        parent_var.data = 'test'
        self.assertEqual(parent_var.data, 'test')
        parent_var.type = 'workspace'
        self.assertEqual(parent_var.type, 'workspace')

    def test_to_object(self):
        ''' test `to_object` function '''
        parent_var = Parent(obj=self.OBJ1)
        self.assertDictEqual(parent_var.to_object(),
                             self.OBJ1)

        parent_var = Parent(obj=self.OBJ2)
        self.assertDictEqual(parent_var.to_object(),
                             self.OBJ2)

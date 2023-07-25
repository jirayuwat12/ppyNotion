'''
    test `Link` class
'''
import unittest
from ppyNotion.link import Link

class TestLink(unittest.TestCase):
    ''' test link class '''

    def test_empty_init(self):
        ''' test empty object initiation '''
        link_var = Link()
        self.assertEqual(link_var.url, str())


    def test_object_init(self):
        ''' test non-empty object initiation '''
        url = r'https://google.com'
        link_var = Link({
            'url' : url
        })
        self.assertEqual(link_var.url, url)

    def test_edit_field(self):
        ''' test edit all field in class '''
        url = r'https://github.com'
        link_var = Link()
        link_var.url = url
        self.assertEqual(link_var.url, url)

    def test_to_object(self):
        ''' test `to_object` function '''
        obj = {
            'url' : 'https://guthib.com'
        }

        link_var = Link(obj=obj)
        self.assertDictEqual(link_var.to_object(), obj)

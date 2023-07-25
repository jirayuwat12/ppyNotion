'''
    test `Equation` class
'''
import unittest
from ppyNotion.equation import Equation
from ppyNotion.type import BaseTextType

class TestEquation(unittest.TestCase):
    '''
        test `Equation` class
    '''
    OBJ = {
        "type": "equation",
        "equation": {
            "expression": "E = mc^2"
        },
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default"
        },
        "plain_text": "E = mc^2",
        "href": ''
    }

    def test_empty_init(self):
        ''' test with empty initiation '''
        equation_var = Equation()
        self.assertEqual(equation_var.expression,
                         str())

    def test_object_init(self):
        ''' test with object initiation '''
        equation_var = Equation(obj = self.OBJ)
        self.assertEqual(equation_var.type,
                         BaseTextType.equation)
        self.assertEqual(equation_var.expression,
                         self.OBJ['equation']['expression'])

    def test_edit_field(self):
        ''' test edit all field in class'''
        equation_var = Equation(obj = self.OBJ)
        equation_var.expression = 'F = ma'
        self.assertEqual(equation_var.expression,
                         'F = ma')

    def test_to_object(self):
        ''' test `to_object` function '''
        equation_var = Equation(obj = self.OBJ)
        self.assertDictEqual(equation_var.to_object(),self.OBJ)

'''
    test `Equation` class
'''
import unittest
from ppyNotion.equation import Equation
from ppyNotion.annotation import Annotation
from ppyNotion.type import BaseTextType, ColorType

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
        self.assertIsNone(equation_var.type)
        self.assertEqual(equation_var.expression,
                         str())
        self.assertIsInstance(equation_var.annotations,
                              Annotation)
        self.assertEqual(equation_var.plain_text,
                         str())
        self.assertEqual(equation_var.href,
                         str())

    def test_object_init(self):
        ''' test with object initiation '''
        equation_var = Equation(obj = self.OBJ)
        self.assertEqual(equation_var.type,
                         BaseTextType.equation)
        self.assertEqual(equation_var.expression,
                         self.OBJ['equation']['expression'])
        self.assertFalse(equation_var.annotations.bold)
        self.assertFalse(equation_var.annotations.italic)
        self.assertEqual(equation_var.annotations.color,
                         ColorType.default)
        self.assertEqual(equation_var.plain_text,
                         'E = mc^2')
        self.assertEqual(equation_var.href,
                         str())

    def test_edit_field(self):
        ''' test edit all field in class'''
        equation_var = Equation()

        equation_var.expression = 'v = u + at'
        self.assertEqual(equation_var.expression,
                         'v = u + at')

        equation_var.annotations.bold = True
        self.assertTrue(equation_var.annotations.bold)

        equation_var.annotations.color = ColorType.gray
        self.assertEqual(equation_var.annotations.color,
                         ColorType.gray)

        equation_var.expression = 'F = ma'
        self.assertEqual(equation_var.expression,
                         'F = ma')
        self.assertEqual(equation_var.plain_text,
                         'F = ma')

    def test_to_object(self):
        ''' test `to_object` function '''
        equation_var = Equation(obj = self.OBJ)
        self.assertDictEqual(equation_var.to_object(),self.OBJ)

from .annotation import Annotation
from .type import ColorType


if __name__ == "__main__":
    import unittest

    class TestAnnotation(unittest.TestCase):

        def test_empty_obj_init(self):
            ''' test empty obj init '''
            a = Annotation()
            self.assertFalse(a.bold)
            self.assertFalse(a.italic)
            self.assertFalse(a.code)
            self.assertFalse(a.strikethrough)
            self.assertEqual(a.color, ColorType.default)
        
    unittest.main()
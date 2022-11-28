import unittest
import atbash

class TestAtbash(unittest.TestCase):
    
    def test_atbash1(self):
        self.assertEqual(atbash.atbash1('a'), 'z')
        self.assertEqual(atbash.atbash1('b'), 'y')
        self.assertEqual(atbash.atbash1('c'), 'x')
        self.assertEqual(atbash.atbash1('X'), 'C')
        self.assertEqual(atbash.atbash1('!'), '!')

    def test_atbash(self):
        self.assertEqual(atbash.atbash('apple'), 'zkkov')
        self.assertEqual(atbash.atbash('Hello world!'), 'Svool dliow!')
        self.assertEqual(atbash.atbash('Christmas is the 25th of December'),
                         'Xsirhgnzh rh gsv 25gs lu Wvxvnyvi')

if __name__ == '__main__':
    unittest.main()
    
    

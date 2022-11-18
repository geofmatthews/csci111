import unittest, quadratic

class Test_Quadratic(unittest.TestCase):
    def test_quadratic(self):
        roots = quadratic.quadratic(1,0,-1)
        self.assertEqual( roots, (-1, 1))
        roots = quadratic.quadratic(1, 0, -4)
        self.assertEqual(  roots, (-2, 2))
        roots = quadratic.quadratic(1, -7, 12)
        self.assertEqual(  roots, (3,4))
        roots = quadratic.quadratic(2, 2, -12)
        self.assertEqual(  roots,(-3,2))

    def test_quadratic_exception(self):
        self.assertRaises(RuntimeError, quadratic.quadratic, 1, 1, 1)

if __name__ == '__main__':
    unittest.main()

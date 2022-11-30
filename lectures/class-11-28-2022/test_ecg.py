import unittest
import ecg

class TestECG(unittest.TestCase):
    
    def test_common_factor(self):
        self.assertTrue(ecg.common_factor(2*5*7, 5*11))
        self.assertFalse(ecg.common_factor(3*11*13, 5*7*23))

    def test_extend_sequence(self):
        ls = [1,2]
        ecg.extend_sequence(ls)
        self.assertEqual(ls, [1,2,4])
        ecg.extend_sequence(ls)
        self.assertEqual(ls, [1,2,4,6])
        ecg.extend_sequence(ls)
        self.assertEqual(ls, [1,2,4,6,3])
        ecg.extend_sequence(ls)
        self.assertEqual(ls, [1,2,4,6,3,9])

    def test_ecg_seq_index(self):
        self.assertEqual(ecg.ecg_seq_index(3), 4)
        self.assertEqual(ecg.ecg_seq_index(5), 9)
        self.assertEqual(ecg.ecg_seq_index(7), 13)

    def test_ecg_seq_element(self):
        self.assertEqual(ecg.ecg_seq_element(4), 3)
        self.assertEqual(ecg.ecg_seq_element(9), 5)
        self.assertEqual(ecg.ecg_seq_element(13), 7)
        

if __name__ == '__main__':
    unittest.main()
    
    

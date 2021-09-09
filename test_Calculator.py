import unittest    #include test library 
import Calculator  #include Calculator file which contain functions that need to be tested

class TestCalc(unittest.TestCase):

  #test Cases for addation operations 
    def test_add(self):
        self.assertEqual(Calculator.add(10, 5), 15)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)

   #test Cases for subtraction operations 
    def test_sub(self):
        self.assertEqual(Calculator.sub(10, 5), 5)
        self.assertEqual(Calculator.sub(-1, 1), -2)
        self.assertEqual(Calculator.sub(-1, -1), 0)

    #test Cases for multiplaction operations 
    def test_multi(self):
        self.assertEqual(Calculator.multi(10, 5), 50)
        self.assertEqual(Calculator.multi(-1, 1), -1)
        self.assertEqual(Calculator.multi(-1, -1), 1)

    #test Cases for division operations 
    def test_div(self):
        self.assertEqual(Calculator.div(10, 5), 2)
        self.assertEqual(Calculator.div(-1, 1), -1)
        self.assertEqual(Calculator.div(-1, -1), 1)
        self.assertEqual(Calculator.div(5, 2), 2.5)

        with self.assertRaises(ValueError):
            Calculator.div(10, 0)
       
    #test Cases for modulus operations 
    def test_modulas(self):
        self.assertEqual(Calculator.modulas(10, 5), 0)
        self.assertEqual(Calculator.modulas(-5, 3), 1)
        self.assertEqual(Calculator.modulas(17, 3), 2)


if __name__ == '__main__':     #Test runner
    unittest.main() 

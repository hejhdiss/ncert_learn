import unittest
import ncert_learn

class TestIntFunctions(unittest.TestCase):
    
    def test_checkprime(self):
        self.assertTrue(ncert_learn.checkprime(7))
        self.assertFalse(ncert_learn.checkprime(4))

    def test_factors(self):
        self.assertEqual(ncert_learn.factors(10), [1, 2, 5, 10])

    def test_checkarmstrong(self):
        self.assertTrue(ncert_learn.checkarmstrong(153))
        self.assertFalse(ncert_learn.checkarmstrong(10))

    def test_checkpalindrome(self):
        self.assertTrue(ncert_learn.checkpalindrome(121))
        self.assertFalse(ncert_learn.checkpalindrome(123))

    def test_checkstrong(self):
        self.assertTrue(ncert_learn.checkstrong(145))
        self.assertFalse(ncert_learn.checkstrong(123))

    def test_checkniven(self):
        self.assertTrue(ncert_learn.checkniven(18))
        self.assertFalse(ncert_learn.checkniven(19))


class TestAreaFunctions(unittest.TestCase):
    
    def test_areaofcircle(self):
        self.assertAlmostEqual(ncert_learn.areaofcircle(3), 28.27, places=2)

    def test_areaofpolygon(self):
        self.assertEqual(ncert_learn.areaofpolygon(5, 6, 7), 105)  # Example values

    def test_areaofrectangle(self):
        self.assertEqual(ncert_learn.areaofrectangle(5, 10), 50)

    def test_areaofsquare(self):
        self.assertEqual(ncert_learn.areaofsquare(4), 16)

    def test_areaoftriangle(self):
        self.assertEqual(ncert_learn.areaoftriangle(5, 10), 25)


class TestConversionFunctions(unittest.TestCase):
    
    def test_integertobinary(self):
        self.assertEqual(ncert_learn.integertobinary(10), '1010')

    def test_integertooctal(self):
        self.assertEqual(ncert_learn.integertooctal(10), '12')

    def test_integertohexadecimal(self):
        self.assertEqual(ncert_learn.integertohexadecimal(10), 'a')

    def test_binarytointeger(self):
        self.assertEqual(ncert_learn.binarytointeger('1010'), 10)


class TestSortingFunctions(unittest.TestCase):

    def test_bubblesort(self):
        self.assertEqual(ncert_learn.bubblesort([4, 2, 7, 1]), [1, 2, 4, 7])

    def test_insertionsort(self):
        self.assertEqual(ncert_learn.insertionsort([4, 2, 7, 1]), [1, 2, 4, 7])


class TestStackDictionaryFunctions(unittest.TestCase):

    def setUp(self):
        self.stack = ncert_learn.createstackdict()

    def test_pushstackdict(self):
        ncert_learn.pushstackdict(self.stack, 5)
        self.assertEqual(self.stack, [5])

    def test_popstackdict(self):
        ncert_learn.pushstackdict(self.stack, 5)
        self.assertEqual(ncert_learn.popstackdict(self.stack), 5)

    def test_peekstackdict(self):
        ncert_learn.pushstackdict(self.stack, 5)
        self.assertEqual(ncert_learn.peekstackdict(self.stack), 5)


class TestStackListFunctions(unittest.TestCase):

    def setUp(self):
        self.stack = ncert_learn.createstacklst()

    def test_pushstacklst(self):
        ncert_learn.pushstacklst(self.stack, 5)
        self.assertEqual(self.stack, [5])

    def test_popstacklst(self):
        ncert_learn.pushstacklst(self.stack, 5)
        self.assertEqual(ncert_learn.popstacklst(self.stack), 5)

    def test_peekstacklst(self):
        ncert_learn.pushstacklst(self.stack, 5)
        self.assertEqual(ncert_learn.peekstacklst(self.stack), 5)


class TestMysqlFunctions(unittest.TestCase):

    def test_mysqlconnect(self):
        # Test mysqlconnect to ensure it returns a successful connection object
        # Here, you should mock this function as actual database connection isn't tested
        conn = ncert_learn.mysqlconnect(host="localhost", user="user", password="password")
        self.assertIsNotNone(conn)  # Check if connection is not None



if __name__ == '__main__':
    unittest.main()

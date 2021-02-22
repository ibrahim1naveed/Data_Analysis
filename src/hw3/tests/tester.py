import unittest


from ..verbosity import *
from ..follow import *
from ..mention import *
from ..non_dict import *

class a3_testCase(unittest.TestCase):

    def test_case_one(self): #Gives the number of ponies/keys in the dictionary
        values = verbosity(my_dict_verbosity)
        self.assertEqual(values, 6)
        
    def test_case_two(self): #Gives the number of ponies in the dictionary
        values = follow(follow_on)
        self.assertEqual(values,6)
        
    def test_case_three(self): #Ensures that twilight does not contains itself in in #its dictionary
        values=mentions_dict('twilight')
        self.assertEqual(values,-1)
        
    def test_case_three(self): #Ensures that applejack does not contains itself in in #its dictionary
        values=mentions_dict('applejack')
        self.assertEqual(values,-1)
        
        

    def test_case_three(self): #Ensures that rarity does not contains itself in in #its dictionary
        values=mentions_dict('rarity')
        self.assertEqual(values,-1)
        
        
    def test_case_three(self): #Ensures that pinkie does not contains itself in in #its dictionary
        values=mentions_dict('pinkie')
        self.assertEqual(values,-1)
        
    def test_case_three(self): #Ensures that rainbow does not contains itself in in #its dictionary
        values=mentions_dict('rainbow')
        self.assertEqual(values,-1)
        
    def test_case_three(self): #Ensures that fluttershy does not contains itself in in its #dictionary
        values=mentions_dict('fluttershy')
        self.assertEqual(values,-1)


    def test_case_nine(self): #Made a test dict to check if the output is correct
        values=testing_dict('twilight')
        self.assertEqual(values,2)
    
    def test_case_nine(self): #Made a test dict to check if the output is correct
        values=testing_dict2('applejack')
        self.assertEqual(values,3)
    
    def test_case_nine(self): #Made a test dict to check if the output is correct
        values=testing_dict3('rarity')
        self.assertEqual(values,4)
    
    def test_case_nine(self): #Made a test dict to check if the output is correct
        values=testing_dict4('pinkie')
        self.assertEqual(values,5)


#All odf my code was mostly done on pandas and for some reason when i imported pandas in the test class it gave me an error saying module not found. i tried to fix it but it said something about having a different version of python installed and running so icouldnt figure it out. i.e i made these tests to show how i understood the concept and applied them correctly. 

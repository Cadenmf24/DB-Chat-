from datetime import date
from doctest import FAIL_FAST
from pickle import FALSE, TRUE
import unittest
from src.chat import *
from src.swen344_db_utils import *
from src.chat1 import *


class TestChat(unittest.TestCase):
    
    # def setUp(self):
    #     run_dataseed
    
    def test_0run_file(self):
        """ **Running exec_sql_file test...** """
        
        exec_sql_file('db-cmf5531/src/chat.sql')
        
    def test_dataseed(self):
        """ **Running dataseed test** """
        # result = exec_get_all(f'SELECT COUNT(*) FROM %s', [database])
        self.assertEqual(len(exec_get_all('SELECT COUNT(*) FROM user_info')), 1)
        self.assertEqual(len(exec_get_all('SELECT COUNT(*) FROM ban_logs')), 1)
        self.assertEqual(len(exec_get_all('SELECT COUNT(*) FROM chat_logs')), 1)
        
        
    def test_Abbott_Costello_convo(self):
        """ **Running Abbott Costello convo** """
        x = run_chat_conversation('Abbott', 'Costello')
        self.assertEqual(len(run_chat_conversation('Abbott', 'Costello')), 2)
        
        """ ** Checking if sender and receiver are both Costello or Abbott ** """
        self.assertEqual(x[0][0], 1) # Abbott's Id
        self.assertEqual(x[0][1], 2) # Costello's ID
        self.assertEqual(x[1][0], 2) 
        self.assertEqual(x[1][1], 1) 
        
        
    def test_Abbott_unread_messages(self):
        """ ** Running ABBOTT UNREAD MESSAGES ** """
        x = run_unread_conversation('Abbott')
        self.assertEqual(len(run_unread_conversation('Abbott')), 1)
        
        """ ** Abbott receives a message and doesn't read it """
        self.assertEqual(x[0][1], 1) # Abbott's ID
        self.assertEqual(x[0][2], False) # Abbott is a bad friend for not reading messages
        
        """ ** Abbott has one unread messages from Costello ** """
        self.assertEqual(x[0][0] , 2) # Costello's ID
        self.assertEqual(x[0][1], 1) # Abbott's Id
        self.assertEqual(x[0][2], False)
        
    def test_Larry_Moe_timed_convo(self):
        """ ** Running Larry Moe timed messages ** """
        x = run_chat_conversation('Larry', 'Moe', 1995)
        self.assertEqual(len(run_chat_conversation('Larry', 'Moe', 1995)), 2)
        
        """ ** Checking to see if Larry and Moe are the only ones talking and the times are right ** """
        self.assertEqual(x[0][0], 3) # Moe's ID
        self.assertEqual(x[0][1], 4) # Larry's ID
        self.assertEqual(x[0][2].year, 1995) # Year is 1995
        self.assertEqual(x[1][0], 4)
        self.assertEqual(x[1][1], 3)
        self.assertEqual(x[1][2].year, 1995) 
        
        
        
    def test_larry_ban(self):
        """ ** Running Larry banned? ** """
        x = run_banned_time('Larry', 2012)
        self.assertEqual(len(run_banned_time('Larry', 2012)), 1)
        
        """ ** Banned Time should return Larry's Id since he is banned until 2060 ** """  
        self.assertEqual(x[0][0], 4) # Larry's ID
        
        
    def test_Curly_ban(self):
        """ ** Running Curly Banned? ** """
        """ ** Banned Time should return Nothing since Curly is not banned in 2000 ** """
        self.assertEqual(len(run_banned_time('Curly',2000)), 0)
        
        
        
    # THREE UNIQUE ONES 
    
    def test_Costello_read_convo(self): #How many convos he has read
        """ ** Running Costello_Read_convo ** """
        x = run_read_conversation('Costello')
        self.assertEqual(len(run_read_conversation('Costello')), 1)
        
        self.assertEqual(x[0][1], 2) # Costello received a message
        self.assertEqual(x[0][2], True) # Message is read
        
        
    def test_abbott_run_single_chat(self):
        """ ** Running Abbott Run Single Chat """
        """ ** Should return 'Ayo' since that is the only message Abbott sent"""
        x = run_single_chat('Abbott')
        self.assertEqual(len(run_single_chat('Abbott')), 1) 
        self.assertEqual(x[0][0], 'Ayo') # Message Context 
        
        
    def test_user_exists(self):
        """ ** Running User Existence ** """
        """ ** Returns nothing since George does not exist ** """
        self.assertEqual(len(run_user_exists('George')), 0) # No one is named George in the system
        
        
        
        
    #More Tests kek
    
    # create_new_user('Bob', '1991-05-17')
    
    
    def test_user_exists(self):
        create_new_user('Bob', '1991-05-17')
        
        self.assertEqual(len(run_user_exists('Bob')), 1)
        
    
if __name__ == '__main__':
    
    unittest.main()
        
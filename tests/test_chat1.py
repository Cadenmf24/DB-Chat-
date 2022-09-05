from doctest import FAIL_FAST
from pickle import FALSE
import unittest
from src.chat import *
from src.swen344_db_utils import *
from src.chat1 import *


class TestChat(unittest.TestCase):
    
    def test_run_file(self):
        """ **Running exec_sql_file test...** """
        
        exec_sql_file('db-cmf5531\\src\\chat.sql')
        
    def test_dataseed(self):
        """ **Running dataseed test** """
        
        self.assertEqual(len(run_dataseed('user_info')), 5)
        self.assertEqual(len(run_dataseed('ban_logs')), 2)
        self.assertEqual(len(run_dataseed('chat_logs')), 7)
        
        
    def test_Abbott_Costello_convo(self):
        """ **Running Abbott Costello convo** """
        self.assertEqual(len(run_chat_conversation('Abbott', 'Costello')),2)
                    
    def test_Abbott_unread_messages(self):
        """ ** Running ABBOTT UNREAD MESSAGES ** """
        self.assertEqual(len(run_unread_conversation('Abbott')), 1)
        
    def test_Larry_Moe_timed_convo(self):
        """ ** Running Larry Moe timed messages ** """
        self.assertEqual(len(run_chat_conversation('Larry', 'Moe', 1995)),3)        
        
    def test_larry_ban(self):
        """ ** Running Larry banned? ** """
        self.assertEqual(len(run_banned_time('Larry', 2012)), 1)
        
    def test_Curly_ban(self):
        """ ** Running Curly Banned? ** """
        self.assertEqual(len(run_banned_time('Curly',2000)), 0)
        
        
    # THREE UNIQUE ONES 
    
    def test_Costello_read_convo(self): #How many convos he has read
        self.assertEqual(len(run_read_conversation('Costello')), 1)
        
    def test_run_single_chat(self):
        self.assertEqual(len(run_single_chat('Abbott')), 1)
        
    def test_user_exists(self):
        self.assertEqual(len(run_user_exists('George')), 0)
        
        
        
        
    
        
        
        
if __name__ == '__main__':
    unittest.main()
        
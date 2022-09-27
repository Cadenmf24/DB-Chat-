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
    
    def test_user_exists(self):
        create_new_user('Bob', '1991-05-17', '1865')
        
        self.assertEqual(len(run_user_exists('Bob')), 1)
        
    def test_change_username(self):
        create_new_user('Bob', '1991-05-17', '1856')
        
        change_username('Bob', 'BabySteps2Door', '1991-05-19')

        self.assertEqual(len(run_user_exists('Bob')), 0) # Bob no longer exists
        
        self.assertEqual(len(run_user_exists('BabySteps2Door')), 1) # Replaced by the superior BabySteps2Door
        
    # def test_csv_file(self):
        
    #     read_csv('whos_on_first.csv')
        
    #     # print(exec_get_all('SELECT * FROM chat_logs'))
        
    def test_new_server_message(self):
        
        self.assertEqual(len(read_server_messages('General')), 7) 
        self.assertEqual(len(read_server_messages('Gamer_mail')), 0 ) #Social Constructs do not exists
        
        
    def test_new_message_in_different_server(self):
        
        create_message(1, 2, 'Chicken Nuggets', '1991-05-18', 'Social_Constructs')
        self.assertEqual(len(read_server_messages('Social_Constructs')), 1)
        
    
    def test_server_message_count(self):
        self.assertEqual((get_server_message_count('General')[0]), 7)
        
        
    def test_final_test1(self):
        
        '''Creating Names'''
        create_new_user('Paul', '2022-09-27', 1234)
        create_new_user('John', '2022-09-27', 5679)
        create_new_user('George', '2022-09-27', 5555)
        create_new_user('Cherry', '2022-09-27', 9999)
        
        '''Creating Server'''
        add_server('Arrakis')
        add_server('Comedy')
        
        '''Creating Messages'''
        Paul = get_name_id('Paul')[0]
        John = get_name_id('John')[0]
        George = get_name_id('George')[0]
        Cherry = get_name_id('Cherry')[0]
        
        create_message(Paul, John, 'Please reply', server_name='Comedy' )
        
        create_message(John, Paul, 'I replied already!', server_name='Comedy')  
        
        """Full Text Search Query"""
        print('\n', word_count('reply')[0])
        print('\n', word_count('reply')[1])   
        print('\n', word_count('reply please')[1])  
       
        
        """Activity Summary"""
        create_message(George, Cherry, 'Can you believe we are only used for a test?', server_name = 'Arrakis' )
        create_message(Cherry, Cherry, 'Nope, I seriously cannot!', server_name = 'Arrakis')  
        create_message(Cherry, John, 'We arent real man!', server_name = 'Arrakis')
        create_message(Paul, John, 'gonna get banned', server_name = 'Arrakis')
        
        create_message(George, Cherry, 'Oh, wow. We seriously arent real', server_name = 'Comedy' )
        create_message(Cherry, Cherry, 'Dude, I cant feel my hands!', server_name = 'Comedy')  
        create_message(Cherry, John, 'We are in a simulation!', server_name = 'Comedy')
        create_message(Paul, John, 'Brb gonna get banned', '1990-9-27', 'Comedy')
        
        # print(get_active_members('Arrakis', '2022-09-27'))
        print(get_active_members('Comedy', '2022-09-27'))
        
        
        """Ban Summary"""
        add_ban(Paul, '2022-09-1', '2023-09-1', 'Arrakis')
        print(read_server_messages('Arrakis'))
        
        
        '''Beautify'''
        beautify('Comedy')
        beautify('Arrakis')
        
        
        
        
        
         
        
        
        
        
        
        
        
        
    
if __name__ == '__main__':
    
    unittest.main()
        
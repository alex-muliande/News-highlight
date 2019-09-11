import unittest
from app.models import News, Articles
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(id,"Gizmodo.com","Jennings Brown","Man Claims He Invented Bitcoin, Is Ordered to Pay Billions in Bitcoin", "A man who has insisted he is the man behind the pseudonymous identity of Satoshi Nakamoto, inventor of bitcoin, has been ordered to pay half of his cryptocurrency bounty to a man believed to be his former colleague. Read more...","https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816","https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png,"2019-08-28T16:50:00Z","A man who has insisted he is the man behind the pseudonymous identity of Satoshi Nakamoto, inventor of bitcoin, has been ordered to pay half of his cryptocurrency bounty to a man believed to be his former colleague.\r\nA U.S. district court ruled on Tuesday tha… [+2903 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


# if __name__ == '__main__':
#     unittest.main()

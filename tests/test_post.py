import unittest
from app.models import Post, User

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.user_iano=User(username='ivan', password_hash='220000', email='ivan@gmail.com')
        self.new_post=Post(title='iano', content='The golden times',  user=self.user_iano)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEqual(self.new_post.title, 'iano')
        self.assertEqual(self.new_post.content, 'The golden times')
        self.assertEqual(self.new_post.user, self.user_iano)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())==1)

    def test_get_posts(self):
        self.new_post.save_post()
        got_posts=Post.get_all_posts()
        self.assertTrue(len(got_posts)>0)


    def test_delete_post(self):
        self.new_post.delete_post()
        self.assertTrue(len(Post.query.all()==0))
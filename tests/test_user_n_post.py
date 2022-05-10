import unittest
from app.models import User, Post


class TestUser(unittest.TestCase):
  '''
  Test behaviour of the user model
  '''
  def setUp(self) -> None:
      self.new_user = User(password = 'baby')

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_pass is not None)
  
  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password


  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('baby'))




class TestPost(unittest.TestCase):
  '''
  Test behaviour of the user model
  '''
  def setUp(self) -> None:
      self.new_pitch = Post(1,)

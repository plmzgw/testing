import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.
class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose 
		pub_date is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(question_text="What's up?", pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(question_text="What's your name?", pub_date=time)
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() should return True for questions whose
		pub_date is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(question_text="What's your age?", pub_date=time)
		self.assertEqual(recent_question.was_published_recently(), True)


# class QuestionViewTests(TestCase):

# 	def test_index_view_with_no_questions(self):
# 		"""
# 		If no questions exist, an appropriat message should be displayed
# 		"""
# 		response = self.client.get()

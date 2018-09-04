import unittest
from survey import anonSurvey

class TestAnonSurvey(unittest.TestCase):
    def test_store_single_res(self):
        question = "what language did you first learn to code in?"
        my_survey = anonSurvey(question)
        my_survey.store_res("JavaScript")

        self.assertIn("JavaScript", my_survey.responses)

    def test_store_mult_res(self):
        question = "what language did you first learn to code in?"
        my_survey = anonSurvey(question)
        responses = ["JavaScript", "Python", "Ruby"]
        for response in responses:
            my_survey.store_res(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()

# Setup() Method
class TestAnonSurvey(unittest.TestCase):

    def setUp(self):
        question = "what language did you first learn to code in?"
        self.my_survey = anonSurvey(question)
        self.responses = ["JavaScript", "Python", "Ruby"]

    def test_store_single_res(self):
        self.my_survey.store_res(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_multi_res(self):
        for response in self.responses:
            self.my_survey.store_res(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

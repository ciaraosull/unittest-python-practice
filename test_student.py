""" practice using different unittest methods"""
import unittest
from datetime import timedelta
from unittest.mock import patch
from student import Student


class TestStudent(unittest.TestCase):
    "TestStudent class"

    @classmethod
    # use @classmethod and pass (cls) instead of (self)
    # acts on the class instead of an instance of the class
    def setUpClass(cls):  # to use if want to populate test database with data
        print("setUpClass")  # will only run once at start

    @classmethod
    # use @classmethod and pass (cls) instead of (self)
    # acts on the class instead of an instance of the class
    def tearDownClass(cls):  # to use if to populate test database with data
        print("tearDownClass")  # will only run once at end

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        "Test to check if method prints full name"
        # student = Student("John", "Doe") not needed if setUp used
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email(self):
        "Test to check student email method"
        # student = Student("John", "Doe") not needed if setUp used
        print("test_email")
        self.assertAlmostEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        "Test to check alert santa method"
        # student = Student("John",  "Doe") not needed if setUp used
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        """ To test a students end date if given an extension"""
        print("test_apply_extension")
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(
            self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        """
        Test to see if response from api successful using patch method
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        - it will need to match
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")


if __name__ == "__main__":
    unittest.main()

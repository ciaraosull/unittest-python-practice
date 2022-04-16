import unittest
from student import Student


class TestStudent(unittest.TestCase):
    "TestStudent class"
    def test_full_name(self):
        "Test to check if method prints full name"
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")

    def test_email(self):
        student = Student("John", "Doe")

        self.assertAlmostEqual(student.email, 'john.doe@email.com')


    def test_alert_santa(self):
        "Test to check alert santa method"
        student = Student("John",  "Doe")
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()

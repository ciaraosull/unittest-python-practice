import unittest
from student import Student


class TestStudent(unittest.TestCase):
    "TestStudent class"

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


if __name__ == "__main__":
    unittest.main()

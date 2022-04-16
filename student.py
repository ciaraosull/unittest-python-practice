""" Practice student class for running unittest """
from datetime import date, timedelta


class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """ Returns a students full name as a string """
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        """ Returns a students email in lowercase as a string """
        return (
            f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
        )

    def alert_santa(self):
        """ Method that sets naughty list to True"""
        self.naughty_list = True

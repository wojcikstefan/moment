#!/usr/bin/env python

from unittest import TestCase, main
from datetime import datetime
import moment


class SimpleAPI(TestCase):

    def test_date_function_takes_a_string(self):
        d = moment.date("December 18, 2012", "MMMM D, YYYY")
        self.assertEquals(d.to_date(), datetime(2012, 12, 18))

    def test_date_function_with_datetime(self):
        d = moment.date(datetime(2012, 12, 18))
        self.assertEquals(d.datetime(), datetime(2012, 12, 18))

    def test_date_function_with_iterable(self):
        d = moment.date((2012, 12, 18))
        self.assertEquals(d.datetime(), datetime(2012, 12, 18))

    def test_now_function_with_current_date(self):
        d = moment.now().to_date()
        now = datetime.now()
        self.assertEquals(d.year, now.year)
        self.assertEquals(d.month, now.month)
        self.assertEquals(d.day, now.day)
        self.assertEquals(d.hour, now.hour)
        self.assertEquals(d.second, now.second)

    def test_utcnow_function(self):
        d = moment.utcnow().to_date()
        now = datetime.utcnow()
        self.assertEquals(d.year, now.year)
        self.assertEquals(d.month, now.month)
        self.assertEquals(d.day, now.day)
        self.assertEquals(d.hour, now.hour)
        self.assertEquals(d.second, now.second)

    def test_moment_can_transfer_between_datetime_and_moment(self):
        d = moment.now().to_date()
        self.assertEquals(d, moment.date(d).to_date())


class Weekdays(TestCase):

    def test_weekdays_can_be_manipulated(self):
        d = moment.date([2012, 12, 19])
        yesterday = moment.date([2012, 12, 18])
        self.assertEquals(d.to_date().isoweekday(), 3)
        self.assertEquals(d.weekday(3).to_date(), d.to_date())
        self.assertEquals(d.weekday(2).to_date(), yesterday.to_date())

    def test_week_addition_equals_weekday_manipulation(self):
        d = moment.date([2012, 12, 19])
        upcoming = d.clone().add('weeks', 1)
        expecting = moment.date([2012, 12, 26]).to_date()
        self.assertEquals(upcoming.to_date(), expecting)
        self.assertEquals(d.weekday(10).to_date(), upcoming.to_date())

    def test_weekdays_with_zeros(self):
        d = moment.date([2012, 12, 19])
        sunday = moment.date([2012, 12, 16]).to_date()
        self.assertEquals(d.weekday(0).to_date(), sunday)

    def test_weekdays_with_negative_numbers(self):
        d = moment.date((2012, 12, 19))
        expecting = moment.date([2012, 12, 9]).to_date()
        self.assertEquals(d.weekday(-7).to_date(), expecting)

    def test_weekdays_with_larger_number_into_new_year(self):
        d = moment.date((2012, 12, 19))
        expecting = moment.date("2013-01-09", "YYYY-MM-DD").to_date()
        self.assertEquals(d.weekday(24).to_date(), expecting)


if __name__ == '__main__':
    main()

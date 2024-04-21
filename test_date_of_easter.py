#!/usr/bin/env python3

import unittest as UT
import src.practical_astronomy.pa_datetime as DOE

def test_input(isVerbose):
	inputYear = 2009

	easterMonth,easterDay,easterYear = DOE.get_date_of_easter(inputYear)
	if isVerbose == True:
		print("__Test Date of Easter functions__")
		print(f"[Test Inputs] Given a year of {inputYear}, the date of Easter is {easterMonth}/{easterDay}/{easterYear}")

	return inputYear,easterMonth,easterDay,easterYear

class test_doe(UT.TestCase):
	@classmethod
	def setUpClass(cls):
		test_input(True)

	def setUp(self):
		inputYear,easterMonth,easterDay,easterYear = test_input(False)
		self.easterMonth = easterMonth
		self.easterDay = easterDay
		self.easterYear = easterYear

	def test_date_result(self):
		self.assertEqual(self.easterMonth,4,"Incorrect month")
		self.assertEqual(self.easterDay,12,"Incorrect day")
		self.assertEqual(self.easterYear,2009,"Incorrect year")


if __name__ == '__main__':
	UT.main()

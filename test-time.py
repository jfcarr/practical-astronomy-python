#!/usr/bin/python3

import lib.pa_datetime as PD
import unittest as UT

def get_civil_time(hours,minutes,seconds):
	decimalHours = PD.civil_time_to_decimal_hours(hours,minutes,seconds)

	return round(decimalHours,8)

class test_civil_time(UT.TestCase):
	def setUp(self):
		self.hours = 18
		self.minutes = 31
		self.seconds = 27
		self.decimalHours = get_civil_time(self.hours,self.minutes,self.seconds)

	def test_civil_time_to_decimal_hours(self):
		print(f"Decimal hours for {self.hours}:{self.minutes}:{self.seconds} is {self.decimalHours}")

		self.assertEqual(self.decimalHours,18.52416667,"Decimal Hours")

	def test_decimal_hours_to_civil_time(self):
		revertHours,revertMinutes,revertSeconds = PD.decimal_hours_to_civil_time(self.decimalHours)
		print(f"Converting {self.decimalHours} back to Civil Time gives {revertHours}:{revertMinutes}:{revertSeconds}")

		self.assertEqual(revertHours,18,"Civil Time: Hours")
		self.assertEqual(revertMinutes,31,"Civil Time: Minutes")
		self.assertEqual(revertSeconds,27,"Civil Time: Seconds")

	def test_decimal_time_parts(self):
		hourPart = PD.decimal_hour_hour(self.decimalHours)
		minutesPart = PD.decimal_hour_minutes(self.decimalHours)
		secondsPart = PD.decimal_hour_seconds(self.decimalHours)

		print(f"The hour part of {self.decimalHours} is {hourPart}")
		print(f"The minutes part of {self.decimalHours} is {minutesPart}")
		print(f"The seconds part of {self.decimalHours} is {secondsPart}")

		self.assertEqual(hourPart,18,"Hour Part")
		self.assertEqual(minutesPart,31,"Minutes Part")
		self.assertEqual(secondsPart,27,"Seconds Part")

class test_local_civil_time(UT.TestCase):
	def setUp(self):
		self.hours = 3
		self.minutes = 37
		self.seconds = 0
		self.isDaylightSavings = True
		self.zoneCorrection = 4
		self.day = 1
		self.month = 7
		self.year = 2013

	def test_local_civil_time_to_universal_time(self):
		utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear = PD.local_civil_time_to_universal_time(self.hours,self.minutes,self.seconds,self.isDaylightSavings,self.zoneCorrection,self.day,self.month,self.year)

		print(f"[LCT]{self.hours}:{self.minutes}:{self.seconds} [DS]{self.isDaylightSavings} [ZC]{self.zoneCorrection} [LD]{self.month}/{self.day}/{self.year} = [UT]{utHours}:{utMinutes}:{utSeconds} [GWD]{gwMonth}/{gwDay}/{gwYear}")

		self.assertEqual(utHours,22,"UT Hours")
		self.assertEqual(utMinutes,37,"UT Minutes")
		self.assertEqual(utSeconds,0,"UT Seconds")
		self.assertEqual(gwDay,30,"Greenwich Day")
		self.assertEqual(gwMonth,6,"Greenwich Month")
		self.assertEqual(gwYear,2013,"Greenwich Year")

	def test_universal_time_to_local_civil_time(self):
		utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear = PD.local_civil_time_to_universal_time(self.hours,self.minutes,self.seconds,self.isDaylightSavings,self.zoneCorrection,self.day,self.month,self.year)

		revertLCTHours,revertLCTMinutes,revertLCTSeconds,revertDay,revertMonth,revertYear = PD.universal_time_to_local_civil_time(utHours,utMinutes,utSeconds,self.isDaylightSavings,self.zoneCorrection,gwDay,gwMonth,gwYear)

		print(f"[UT]{utHours}:{utMinutes}:{utSeconds} [DS]{self.isDaylightSavings} [ZC]{self.zoneCorrection} [GWD]{gwMonth}/{gwDay}/{gwYear} = [LCT]{revertLCTHours}:{revertLCTMinutes}:{revertLCTSeconds} [LD]{self.month}/{self.day}/{self.year}")

		self.assertEqual(revertLCTHours,3,"LCT Hours")
		self.assertEqual(revertLCTMinutes,37, "LCT Minutes")
		self.assertEqual(revertLCTSeconds,0, "LCT Seconds")
		self.assertEqual(revertDay,1,"Local Day")
		self.assertEqual(revertMonth,7,"Local Month")
		self.assertEqual(revertYear,2013,"Local Year")

class test_sidereal_time_universal_time(UT.TestCase):
	def setUp(self):
		self.utHours = 14
		self.utMinutes = 36
		self.utSeconds = 51.67
		self.greenwichDay = 22
		self.greenwichMonth = 4
		self.greenwichYear = 1980

	def test_universal_time_to_greenwich_sidereal_time(self):
		gstHours,gstMinutes,gstSeconds = PD.universal_time_to_greenwich_sidereal_time(self.utHours,self.utMinutes,self.utSeconds,self.greenwichDay,self.greenwichMonth,self.greenwichYear)
		
		print(f"[UT] {self.utHours}:{self.utMinutes}:{self.utSeconds} {self.greenwichMonth}/{self.greenwichDay}/{self.greenwichYear} = [GST] {gstHours}:{gstMinutes}:{gstSeconds}")

		self.assertEqual(gstHours,4,"GST Hours")
		self.assertEqual(gstMinutes,40,"GST Minutes")
		self.assertEqual(gstSeconds,5.23,"GST Seconds")

	def test_greenwich_sidereal_time_to_universal_time(self):
		gstHours,gstMinutes,gstSeconds = PD.universal_time_to_greenwich_sidereal_time(self.utHours,self.utMinutes,self.utSeconds,self.greenwichDay,self.greenwichMonth,self.greenwichYear)
		
		revertUTHours,revertUTMinutes,revertUTSeconds,statusMessage = PD.greenwich_sidereal_time_to_universal_time(gstHours,gstMinutes,gstSeconds,self.greenwichDay,self.greenwichMonth,self.greenwichYear)

		print(f"[GST] {gstHours}:{gstMinutes}:{gstSeconds} {self.greenwichMonth}/{self.greenwichDay}/{self.greenwichYear} = [UT] {revertUTHours}:{revertUTMinutes}:{revertUTSeconds} [Status] {statusMessage}")

		self.assertEqual(revertUTHours,14,"UT Hours")
		self.assertEqual(revertUTMinutes,36,"UT Minutes")
		self.assertEqual(revertUTSeconds,51.67,"UT Seconds")
		self.assertIn(statusMessage,["OK","Warning"],"Status Message")

class test_sidereal_time_local_time(UT.TestCase):
	def setUp(self):
		self.gstHours = 4
		self.gstMinutes = 40
		self.gstSeconds = 5.23
		self.geographicalLongitude = -64

	def test_greenwich_sidereal_time_to_local_sidereal_time(self):
		lstHours,lstMinutes,lstSeconds = PD.greenwich_sidereal_time_to_local_sidereal_time(self.gstHours,self.gstMinutes,self.gstSeconds,self.geographicalLongitude)

		print(f"[GST] {self.gstHours}:{self.gstMinutes}:{self.gstSeconds} [LON] {self.geographicalLongitude} = [LST] {lstHours}:{lstMinutes}:{lstSeconds}")

		self.assertEqual(lstHours,0,"LST Hours")
		self.assertEqual(lstMinutes,24,"LST Minutes")
		self.assertEqual(lstSeconds,5.23,"LST Seconds")

	def test_local_sidereal_time_to_greenwich_sidereal_time(self):
		lstHours,lstMinutes,lstSeconds = PD.greenwich_sidereal_time_to_local_sidereal_time(self.gstHours,self.gstMinutes,self.gstSeconds,self.geographicalLongitude)

		revertGSTHours,revertGSTMinutes,revertGSTSeconds = PD.local_sidereal_time_to_greenwich_sidereal_time(lstHours,lstMinutes,lstSeconds,self.geographicalLongitude)

		print(f"[LST] {lstHours}:{lstMinutes}:{lstSeconds} [LON] {self.geographicalLongitude} = [GST] {revertGSTHours}:{revertGSTMinutes}:{revertGSTSeconds}")

		self.assertEqual(revertGSTHours,4,"GST Hours")
		self.assertEqual(revertGSTMinutes,40,"GST Minutes")
		self.assertEqual(revertGSTSeconds,5.23,"GST Seconds")
	

if __name__ == '__main__':
	UT.main()

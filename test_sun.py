#!/usr/bin/env python3

import src.practical_astronomy.pa_sun as PS
import unittest as UT

class test_approximate_position_of_sun(UT.TestCase):
	def setUp(self):
		self.lct_hours = 0
		self.lct_minutes = 0
		self.lct_seconds = 0
		self.local_day = 27
		self.local_month = 7
		self.local_year = 2003
		self.is_daylight_saving = False
		self.zone_correction = 0

	def test_approximate_position_of_sun(self):
		sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec = PS.approximate_position_of_sun(self.lct_hours, self.lct_minutes, self.lct_seconds, self.local_day, self.local_month, self.local_year, self.is_daylight_saving, self.zone_correction)

		print(f"Approximate position of the sun: [Local Time] {self.lct_hours}:{self.lct_minutes}:{self.lct_seconds} [Local Day] {self.local_month}/{self.local_day}/{self.local_year} [DST] {self.is_daylight_saving} [Zone Correction] {self.zone_correction} = [Sun] [RA] {sun_ra_hour}:{sun_ra_min}:{sun_ra_sec} [Dec] {sun_dec_deg}d {sun_dec_min}m {sun_dec_sec}s")

		self.assertEqual(sun_ra_hour,8,"Sun RA Hour")
		self.assertEqual(sun_ra_min,23,"Sun RA Minutes")
		self.assertEqual(sun_ra_sec,33.73,"Sun RA Seconds")
		self.assertEqual(sun_dec_deg,19,"Sun Dec Degrees")
		self.assertEqual(sun_dec_min,21,"Sun Dec Minutes")
		self.assertEqual(sun_dec_sec,14.33,"Sun Dec Seconds")

class test_precise_position_of_sun(UT.TestCase):
	def setUp(self):
		self.lct_hours = 0
		self.lct_minutes = 0
		self.lct_seconds = 0
		self.local_day = 27
		self.local_month = 7
		self.local_year = 1988
		self.is_daylight_saving = False
		self.zone_correction = 0

	def test_precise_position_of_sun(self):
		sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec = PS.precise_position_of_sun(self.lct_hours, self.lct_minutes, self.lct_seconds, self.local_day, self.local_month, self.local_year, self.is_daylight_saving, self.zone_correction)

		print(f"Precise position of the sun: [Local Time] {self.lct_hours}:{self.lct_minutes}:{self.lct_seconds} [Local Day] {self.local_month}/{self.local_day}/{self.local_year} [DST] {self.is_daylight_saving} [Zone Correction] {self.zone_correction} = [Sun] [RA] {sun_ra_hour}:{sun_ra_min}:{sun_ra_sec} [Dec] {sun_dec_deg}d {sun_dec_min}m {sun_dec_sec}s")

		self.assertEqual(sun_ra_hour,8,"Sun RA Hour")
		self.assertEqual(sun_ra_min,26,"Sun RA Minutes")
		self.assertEqual(sun_ra_sec,3.83,"Sun RA Seconds")
		self.assertEqual(sun_dec_deg,19,"Sun Dec Degrees")
		self.assertEqual(sun_dec_min,12,"Sun Dec Minutes")
		self.assertEqual(sun_dec_sec,49.72,"Sun Dec Seconds")

class test_sun_distance_and_angular_size(UT.TestCase):
	def setUp(self):
		self.lct_hours = 0
		self.lct_minutes = 0
		self.lct_seconds = 0
		self.local_day = 27
		self.local_month = 7
		self.local_year = 1988
		self.is_daylight_saving = False
		self.zone_correction = 0

	def test_sun_distance_and_angular_size(self):
		sun_dist_km,sun_ang_size_deg,sun_ang_size_min,sun_ang_size_sec = PS.sun_distance_and_angular_size(self.lct_hours, self.lct_minutes, self.lct_seconds, self.local_day, self.local_month, self.local_year, self.is_daylight_saving, self.zone_correction)

		print(f"Sun's distance and angular size: [Local Time] {self.lct_hours}:{self.lct_minutes}:{self.lct_seconds} [Local Day] {self.local_month}/{self.local_day}/{self.local_year} [DST] {self.is_daylight_saving} [Zone Correction] {self.zone_correction} = [Sun] [Dist km] {sun_dist_km} [Angular size] {sun_ang_size_deg}d {sun_ang_size_min}m {sun_ang_size_sec}s")

		self.assertEqual(sun_dist_km,151920100,"Sun Distance in km")
		self.assertEqual(sun_ang_size_deg,0,"Sun Angular Size Degrees")
		self.assertEqual(sun_ang_size_min,31,"Sun Angular Size Minutes")
		self.assertEqual(sun_ang_size_sec,29.93,"Sun Angular Size Seconds")

class test_sunrise_and_sunset(UT.TestCase):
	def setUp(self):
		self.local_day = 10
		self.local_month = 3
		self.local_year = 1986
		self.is_daylight_saving = False
		self.zone_correction = -5
		self.geographical_long_deg = -71.05
		self.geographical_lat_deg = 42.37

	def test_sunrise_and_sunset(self):
		local_sunrise_hour,local_sunrise_minute,local_sunset_hour,local_sunset_minute,azimuth_of_sunrise_deg,azimuth_of_sunset_deg,status = PS.sunrise_and_sunset(self.local_day, self.local_month, self.local_year, self.is_daylight_saving, self.zone_correction, self.geographical_long_deg, self.geographical_lat_deg)

		print(f"Sunrise and sunset: [Local date] {self.local_month}/{self.local_day}/{self.local_year} [DST?] {self.is_daylight_saving} [TZ Correction] {self.zone_correction} [Lat/Long] {self.geographical_lat_deg}/{self.geographical_long_deg} = [Sunrise] [time] {local_sunrise_hour}:{local_sunrise_minute} [Azimuth] {azimuth_of_sunrise_deg}, [Sunset] [time] {local_sunset_hour}:{local_sunset_minute} [Azimuth] {azimuth_of_sunset_deg}, [Status] {status}")

		self.assertEqual(local_sunrise_hour,6,"Local Sunrise Hour")
		self.assertEqual(local_sunrise_minute,5,"Local Sunrise Minute")
		self.assertEqual(local_sunset_hour,17,"Local Sunset Hour")
		self.assertEqual(local_sunset_minute,45,"Local Sunset Minute")
		self.assertEqual(azimuth_of_sunrise_deg,94.83,"Azimuth of Sunrise (degrees)")
		self.assertEqual(azimuth_of_sunset_deg,265.43,"Azimuth of Sunset (degrees)")
		self.assertEqual(status,"OK","Status of Calculation")

class test_morning_and_evening_twilight(UT.TestCase):
	def setUp(self):
		self.local_day = 7
		self.local_month = 9
		self.local_year = 1979
		self.is_daylight_saving = False
		self.zone_correction = 0
		self.geographical_long_deg = 0
		self.geographical_lat_deg = 52
		self.twilight_type = "A"

	def test_morning_and_evening_twilight(self):
		am_twilight_begins_hour,am_twilight_begins_min,pm_twilight_ends_hour,pm_twilight_ends_min,status = PS.morning_and_evening_twilight(self.local_day, self.local_month, self.local_year, self.is_daylight_saving, self.zone_correction, self.geographical_long_deg, self.geographical_lat_deg, self.twilight_type)

		print(f"Morning and evening twilight: [Local date] {self.local_month}/{self.local_day}/{self.local_year} [DST?] {self.is_daylight_saving} [TZ Correction] {self.zone_correction} [Lat/Long] {self.geographical_lat_deg}/{self.geographical_long_deg} [Twilight Type] {self.twilight_type} = [AM Twilight Begins] {am_twilight_begins_hour}:{am_twilight_begins_min} [PM Twilight Ends] {pm_twilight_ends_hour}:{pm_twilight_ends_min}, [Status] {status}")

		self.assertEqual(am_twilight_begins_hour,3,"AM Twilight Begins (hour)")
		self.assertEqual(am_twilight_begins_min,17,"AM Twilight Begins (minute)")
		self.assertEqual(pm_twilight_ends_hour,20,"PM Twilight Ends (hour)")
		self.assertEqual(pm_twilight_ends_min,37,"PM Twilight Ends (minute)")
		self.assertEqual(status,"OK","Status of Calculation")

class test_equation_of_time(UT.TestCase):
	def setUp(self):
		self.gwdate_day = 27
		self.gwdate_month = 7
		self.gwdate_year = 2010

	def test_equation_of_time(self):
		equation_of_time_min, equation_of_time_sec = PS.equation_of_time(self.gwdate_day,self.gwdate_month,self.gwdate_year)

		print(f"Equation of Time:  [Greenwich Date] {self.gwdate_month}/{self.gwdate_day}/{self.gwdate_year} = [Equation of Time] {equation_of_time_min}:{equation_of_time_sec}")

		self.assertEqual(equation_of_time_min,6,"Equation of Time (min)")
		self.assertEqual(equation_of_time_sec,31.52,"Equation of Time (sec)")

class test_solar_elongation(UT.TestCase):
	def setUp(self):
		self.ra_hour = 10
		self.ra_min = 6
		self.ra_sec = 45
		self.dec_deg = 11
		self.dec_min = 57
		self.dec_sec = 27
		self.gwdate_day = 27.8333333
		self.gwdate_month = 7
		self.gwdate_year = 2010

	def test_solar_elongation(self):
		solar_elongation_deg = PS.solar_elongation(self.ra_hour,self.ra_min,self.ra_sec,self.dec_deg,self.dec_min,self.dec_sec,self.gwdate_day,self.gwdate_month,self.gwdate_year)

		print(f"Solar elongation: [Right Ascension] {self.ra_hour}:{self.ra_min}:{self.ra_sec} [Declination] {self.dec_deg}d {self.dec_min}m {self.dec_sec}s [Greenwich Date] {self.gwdate_month}/{self.gwdate_day}/{self.gwdate_year} = [Solar Elongation (degrees)] {solar_elongation_deg}")

		self.assertEqual(solar_elongation_deg,24.78,"Solar Elongation (degrees)")


if __name__ == '__main__':
	UT.main()

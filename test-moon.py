#!/usr/bin/python3

import lib.pa_moon as PMO
import unittest as UT

class test_moon_position_and_info(UT.TestCase):
	def setUp(self):
		self.lct_hour = 0 
		self.lct_min = 0 
		self.lct_sec = 0 
		self.is_daylight_saving = False 
		self.zone_correction_hours = 0 
		self.local_date_day = 1 
		self.local_date_month = 9 
		self.local_date_year = 2003 

	def test_approximate_position_of_moon(self):
		moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec = PMO.approximate_position_of_moon(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Approximate position of Moon: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Right Ascension] {moon_ra_hour}h {moon_ra_min}m {moon_ra_sec}s [Declination] {moon_dec_deg}d {moon_dec_min}m {moon_dec_sec}s")

		self.assertEqual(moon_ra_hour,14,"Moon RA (hour)")
		self.assertEqual(moon_ra_min,12,"Moon RA (minutes)")
		self.assertEqual(moon_ra_sec,42.31,"Moon RA (seconds)")
		self.assertEqual(moon_dec_deg,-11, "Moon Declination (degrees)")
		self.assertEqual(moon_dec_min,31,"Moon Declination (minutes)")
		self.assertEqual(moon_dec_sec,38.27,"Moon Declination (seconds)")

	def test_precise_position_of_moon(self):
		moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec, earth_moon_dist_km, moon_hor_parallax_deg = PMO.precise_position_of_moon(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Precise position of Moon: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Right Ascension] {moon_ra_hour}h {moon_ra_min}m {moon_ra_sec}s [Declination] {moon_dec_deg}d {moon_dec_min}m {moon_dec_sec}s [Earth-Moon distance] {earth_moon_dist_km} km [Horizontal Parallax] {moon_hor_parallax_deg} degrees")

		self.assertEqual(moon_ra_hour,14,"Moon RA (hour)")
		self.assertEqual(moon_ra_min,12,"Moon RA (minutes)")
		self.assertEqual(moon_ra_sec,10.21,"Moon RA (seconds)")
		self.assertEqual(moon_dec_deg,-11, "Moon Declination (degrees)")
		self.assertEqual(moon_dec_min,34,"Moon Declination (minutes)")
		self.assertEqual(moon_dec_sec,57.83,"Moon Declination (seconds)")
		self.assertEqual(earth_moon_dist_km,367964,"Earth-Moon distance (km)")
		self.assertEqual(moon_hor_parallax_deg,0.993191,"Moon Horizontal Parallax (degrees)")

	def test_moon_phase(self):
		moon_phase, pa_bright_limb_deg = PMO.moon_phase(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Moon phase: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Phase] {moon_phase} [Position Angle of Bright Limb] {pa_bright_limb_deg}")

		self.assertEqual(moon_phase,0.22,"Moon Phase")
		self.assertEqual(pa_bright_limb_deg,-71.58,"Position Angle of Bright Limb")

	def test_moon_dist_ang_diam_hor_parallax(self):
		earth_moon_dist, ang_diameter_deg, ang_diameter_min, hor_parallax_deg, hor_parallax_min, hor_parallax_sec = PMO.moon_dist_ang_diam_hor_parallax(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Moon distance, angular diameter, and horizontal parallax: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Earth-Moon Dist] {earth_moon_dist} km [Angular Diameter] {ang_diameter_deg}d {ang_diameter_min}m [Horizontal Parallax] {hor_parallax_deg}d {hor_parallax_min}m {hor_parallax_sec}s")

		self.assertEqual(earth_moon_dist,367960,"Earth-Moon distance (km)")
		self.assertEqual(ang_diameter_deg,0,"Angular diameter (degrees part)")
		self.assertEqual(ang_diameter_min,32,"Angular diameter (minutes part)")
		self.assertEqual(hor_parallax_deg,0,"Horizontal parallax (degrees part)")
		self.assertEqual(hor_parallax_min,59,"Horizontal parallax (minutes part)")
		self.assertEqual(hor_parallax_sec,35.49,"Horizontal parallax (seconds part)")

class test_new_moon_and_full_moon(UT.TestCase):
	def setUp(self):
		self.is_daylight_saving = False 
		self.zone_correction_hours = 0 
		self.local_date_day = 1 
		self.local_date_month = 9 
		self.local_date_year = 2003 

	def test_times_of_new_moon_and_full_moon(self):
		nm_local_time_hour, nm_local_time_min, nm_local_date_day, nm_local_date_month, nm_local_date_year, fm_local_time_hour, fm_local_time_min, fm_local_date_day, fm_local_date_month, fm_local_date_year = PMO.times_of_new_moon_and_full_moon(self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)
	
		print(f"New moon and full moon: [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [New Moon] {nm_local_time_hour}:{nm_local_time_min} on {nm_local_date_month}/{nm_local_date_day}/{nm_local_date_year} [Full Moon] {fm_local_time_hour}:{fm_local_time_min} on {fm_local_date_month}/{fm_local_date_day}/{fm_local_date_year}")

		self.assertEqual(nm_local_time_hour,17,"new Moon instant - local time (hour)")
		self.assertEqual(nm_local_time_min,27,"new Moon instant - local time (minutes)")
		self.assertEqual(nm_local_date_day,27,"new Moon instance - local date (day)")
		self.assertEqual(nm_local_date_month,8,"new Moon instance - local date (month)")
		self.assertEqual(nm_local_date_year,2003,"new Moon instance - local date (year)")
		self.assertEqual(fm_local_time_hour,16,"full Moon instant - local time (hour)")
		self.assertEqual(fm_local_time_min,36,"full Moon instant - local time (minutes)")
		self.assertEqual(fm_local_date_day,10,"full Moon instance - local date (day)")
		self.assertEqual(fm_local_date_month,9,"full Moon instance - local date (month)")
		self.assertEqual(fm_local_date_year,2003,"full Moon instance - local date (year)")

class test_moonrise_moonset(UT.TestCase):
	def setUp(self):
		self.local_date_day = 6
		self.local_date_month = 3
		self.local_date_year = 1986
		self.is_daylight_saving = False
		self.zone_correction_hours = -5
		self.geog_long_deg = -71.05
		self.geog_lat_deg = 42.3667

	def test_moonrise_moonset(self):
		mr_lt_hour, mr_lt_min, mr_local_date_day, mr_local_date_month, mr_local_date_year, mr_azimuth_deg, ms_lt_hour, ms_lt_min, ms_local_date_day, ms_local_date_month, ms_local_date_year, ms_azimuth_deg = PMO.moonrise_and_moonset(self.local_date_day,self.local_date_month,self.local_date_year,self.is_daylight_saving,self.zone_correction_hours,self.geog_long_deg,self.geog_lat_deg)

		print(f"Moonrise and moonset: [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Geographical Coordinates] [Longitude] {self.geog_long_deg} degrees [Latitude] {self.geog_lat_deg} degrees = [Moonrise] [Time] {mr_lt_hour}:{mr_lt_min} [Date] {mr_local_date_month}/{mr_local_date_day}/{mr_local_date_year} [Azimuth] {mr_azimuth_deg} degrees [Moonset] [Time] {ms_lt_hour}:{ms_lt_min} [Date] {ms_local_date_month}/{ms_local_date_day}/{ms_local_date_year} [Azimuth] {ms_azimuth_deg} degrees")

		self.assertEqual(mr_lt_hour,4,"Moonrise - Local Time (hours)")
		self.assertEqual(mr_lt_min,21,"Moonrise - Local Time (minutes)")
		self.assertEqual(mr_local_date_day,6,"Moonrise - Local Date (day)")
		self.assertEqual(mr_local_date_month,3,"Moonrise - Local Date (month)")
		self.assertEqual(mr_local_date_year,1986,"Moonrise - Local Date (year)")
		self.assertEqual(mr_azimuth_deg,127.34,"Moonrise - Azimuth (degrees)")
		self.assertEqual(ms_lt_hour,13,"Moonset - Local Time (hours)")
		self.assertEqual(ms_lt_min,8,"Moonset - Local Time (minutes)")
		self.assertEqual(ms_local_date_day,6,"Moonset - Local Date (day)")
		self.assertEqual(ms_local_date_month,3,"Moonset - Local Date (month)")
		self.assertEqual(ms_local_date_year,1986,"Moonset - Local Date (year)")
		self.assertEqual(ms_azimuth_deg,234.05,"Moonset - Azimuth (degrees)")


if __name__ == '__main__':
	UT.main()

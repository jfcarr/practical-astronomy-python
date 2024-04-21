#!/usr/bin/env python3

import src.practical_astronomy.pa_comet as PC
import src.practical_astronomy.pa_planet as PP
import src.practical_astronomy.pa_binary as PB
import unittest as UT

class test_position_of_planet(UT.TestCase):
	def setUp(self):
		self.lct_hour = 0 
		self.lct_min = 0 
		self.lct_sec = 0 
		self.is_daylight_saving = False 
		self.zone_correction_hours = 0 
		self.local_date_day = 22 
		self.local_date_month = 11 
		self.local_date_year = 2003 
		self.planet_name = "Jupiter"

	def test_approximate_position_of_planet(self):
		planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec = PP.approximate_position_of_planet(self.lct_hour,self.lct_min,self.lct_sec,self.is_daylight_saving,self.zone_correction_hours,self.local_date_day,self.local_date_month,self.local_date_year,self.planet_name)

		print(f"Approximate position of planet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Planet] {self.planet_name} = [Right Ascension] {planet_ra_hour}h {planet_ra_min}m {planet_ra_sec}s [Declination] {planet_dec_deg}d {planet_dec_min}m {planet_dec_sec}s")

		self.assertEqual(planet_ra_hour,11,"Planet Right Ascension (hour)")
		self.assertEqual(planet_ra_min,11,"Planet Right Ascension (minutes)")
		self.assertEqual(planet_ra_sec,13.8,"Planet Right Ascension (seconds)")
		self.assertEqual(planet_dec_deg,6,"Planet Declination (degrees)")
		self.assertEqual(planet_dec_min,21,"Planet Declination (minutes)")
		self.assertEqual(planet_dec_sec,25.1,"Planet Declination (seconds)")

	def test_precise_position_of_planet(self):
		planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec = PP.precise_position_of_planet(self.lct_hour,self.lct_min,self.lct_sec,self.is_daylight_saving,self.zone_correction_hours,self.local_date_day,self.local_date_month,self.local_date_year,self.planet_name)

		print(f"Precise position of planet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Planet] {self.planet_name} = [Right Ascension] {planet_ra_hour}h {planet_ra_min}m {planet_ra_sec}s [Declination] {planet_dec_deg}d {planet_dec_min}m {planet_dec_sec}s")

		self.assertEqual(planet_ra_hour,11,"Planet Right Ascension (hour)")
		self.assertEqual(planet_ra_min,10,"Planet Right Ascension (minutes)")
		self.assertEqual(planet_ra_sec,30.99,"Planet Right Ascension (seconds)")
		self.assertEqual(planet_dec_deg,6,"Planet Declination (degrees)")
		self.assertEqual(planet_dec_min,25,"Planet Declination (minutes)")
		self.assertEqual(planet_dec_sec,49.46,"Planet Declination (seconds)")

	def test_visual_aspects_of_a_planet(self):
		distance_au, ang_dia_arcsec, phase, light_time_hour, light_time_minutes, light_time_seconds, pos_angle_bright_limb_deg, approximate_magnitude = PP.visual_aspects_of_a_planet(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year, self.planet_name)

		print(f"Visual aspects of planet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Planet] {self.planet_name} = [Distance] {distance_au} au [Angular Diameter] {ang_dia_arcsec} arcsec [Phase] {phase} [Light Time] {light_time_hour}:{light_time_minutes}:{light_time_seconds} [Position Angle of Bright Limb] {pos_angle_bright_limb_deg}d [Magnitude] {approximate_magnitude}")

		self.assertEqual(distance_au,5.59829,"Distance - AU")
		self.assertEqual(ang_dia_arcsec,35.1,"Angular Diameter - arcsec")
		self.assertEqual(phase,0.99,"Phase")
		self.assertEqual(light_time_hour,0,"Light Time - hour part")
		self.assertEqual(light_time_minutes,46,"Light Time - minutes part")
		self.assertEqual(light_time_seconds,33.32,"Light Time - seconds part")
		self.assertEqual(pos_angle_bright_limb_deg,113.2,"Position Angle of Bright Limb - degrees")
		self.assertEqual(approximate_magnitude,-2,"Approximate Magnitude")

class test_position_of_elliptical_comet(UT.TestCase):
	def setUp(self):
		self.lct_hour = 0
		self.lct_min = 0
		self.lct_sec = 0
		self.is_daylight_saving = False
		self.zone_correction_hours = 0
		self.local_date_day = 1
		self.local_date_month = 1
		self.local_date_year = 1984
		self.comet_name = "Halley"

	def test_position_of_elliptical_comet(self):
		comet_ra_hour, comet_ra_min, comet_dec_deg, comet_dec_min, comet_dist_earth = PC.position_of_elliptical_comet(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year, self.comet_name)

		print(f"Position of elliptical comet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Comet] {self.comet_name} = [RA] {comet_ra_hour}h {comet_ra_min}m [Declination] {comet_dec_deg}d {comet_dec_min}m [Distance] {comet_dist_earth} AU")

		self.assertEqual(comet_ra_hour,6,"Comet RA - hour")
		self.assertEqual(comet_ra_min,29,"Comet RA - minutes")
		self.assertEqual(comet_dec_deg,10,"Comet Declination - degrees")
		self.assertEqual(comet_dec_min,13,"Comet Declination - minutes")
		self.assertEqual(comet_dist_earth,8.13,"Comet Distance from Earth - AU")

class test_position_of_parabolic_comet(UT.TestCase):
	def setUp(self):
		self.lct_hour = 0
		self.lct_min = 0
		self.lct_sec = 0
		self.is_daylight_saving = False
		self.zone_correction_hours = 0
		self.local_date_day = 25
		self.local_date_month = 12
		self.local_date_year = 1977
		self.comet_name = "Kohler"

	def test_position_of_parabolic_comet(self):
		comet_ra_hour, comet_ra_min, comet_ra_sec, comet_dec_deg, comet_dec_min, comet_dec_sec, comet_dist_earth = PC.position_of_parabolic_comet(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year, self.comet_name)

		print(f"Position of parabolic comet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Comet] {self.comet_name} = [RA] {comet_ra_hour}h {comet_ra_min}m {comet_ra_sec}s [Declination] {comet_dec_deg}d {comet_dec_min}m {comet_dec_sec}s [Distance] {comet_dist_earth} AU")

		self.assertEqual(comet_ra_hour,23,"Comet RA - hour")
		self.assertEqual(comet_ra_min,17,"Comet RA - minutes")
		self.assertEqual(comet_ra_sec,11.53,"Comet RA - seconds")
		self.assertEqual(comet_dec_deg,-33,"Comet Declination - degrees")
		self.assertEqual(comet_dec_min,42,"Comet Declination - minutes")
		self.assertEqual(comet_dec_sec,26.42,"Comet Declination - seconds")
		self.assertEqual(comet_dist_earth,1.11,"Comet Distance from Earth - AU")

class test_binary_star_orbit(UT.TestCase):
	def setUp(self):
		self.greenwich_date_day = 1
		self.greenwich_date_month = 1
		self.greenwich_date_year = 1980
		self.binary_name = "eta-Cor"

	def test_binary_star_orbit(self):
		position_angle_deg, separation_arcsec = PB.binary_star_orbit(self.greenwich_date_day, self.greenwich_date_month, self.greenwich_date_year, self.binary_name)

		print(f"Binary star orbit: [Greenwich Date] {self.greenwich_date_month}/{self.greenwich_date_day}/{self.greenwich_date_year} [Binary] {self.binary_name} = [Position Angle] {position_angle_deg}d [Separation] {separation_arcsec} arcsec")

		self.assertEqual(position_angle_deg,318.5,"Position Angle (degrees)")
		self.assertEqual(separation_arcsec,0.41,"Separation (arcseconds)")


if __name__ == '__main__':
	UT.main()

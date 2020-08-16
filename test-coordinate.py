#!/usr/bin/python3

import lib.pa_coordinate as PC
import unittest as UT

def get_decimal_degrees(degrees,minutes,seconds):
	resultDecimalDegrees = round(PC.angle_to_decimal_degrees(degrees,minutes,seconds),7)

	return resultDecimalDegrees

class test_angle_decimal_degrees(UT.TestCase):
	def setUp(self):
		self.degrees = 182
		self.minutes = 31
		self.seconds = 27

	def test_angle_to_decimal_degrees(self):
		resultDecimalDegrees = get_decimal_degrees(self.degrees,self.minutes,self.seconds)

		print(f"Angle to Decimal Degrees:  [Angle] {self.degrees}d {self.minutes}m {self.seconds}s = [Decimal Degrees] {resultDecimalDegrees}")

		self.assertEqual(resultDecimalDegrees,182.5241667,"Decimal Degrees")

	def test_decimal_degrees_to_angle(self):
		resultDecimalDegrees = get_decimal_degrees(self.degrees,self.minutes,self.seconds)

		revertDegrees,revertMinutes,revertSeconds = PC.decimal_degrees_to_angle(resultDecimalDegrees)

		print(f"Decimal Degrees to Angle:  [Decimal Degrees] {resultDecimalDegrees} = [Angle] {revertDegrees}d {revertMinutes}m {revertSeconds}s")

		self.assertEqual(revertDegrees,182,"Angle Degrees")
		self.assertEqual(revertMinutes,31,"Angle Minutes")
		self.assertEqual(revertSeconds,27,"Angle Seconds")

class test_right_ascension_hour_angle(UT.TestCase):
	def setUp(self):
		self.ra_hours = 18
		self.ra_minutes = 32
		self.ra_seconds = 21
		self.lct_hours = 14
		self.lct_minutes = 36
		self.lct_seconds = 51.67
		self.is_daylight_saving = False
		self.zone_correction = -4
		self.local_day = 22
		self.local_month = 4
		self.local_year = 1980
		self.geographical_longitude = -64

	def test_right_ascension_to_hour_angle(self):
		hour_angle_hours,hour_angle_minutes,hour_angle_seconds = PC.right_ascension_to_hour_angle(self.ra_hours,self.ra_minutes,self.ra_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		print(f"Right Ascension to Hour Angle:  [RA] {self.ra_hours}:{self.ra_minutes}:{self.ra_seconds} [LCT] {self.lct_hours}:{self.lct_minutes}:{self.lct_seconds} [DS] {self.is_daylight_saving} [ZC] {self.zone_correction} [LD] {self.local_month}/{self.local_day}/{self.local_year} [LON] {self.geographical_longitude} = [HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds}")

		self.assertEqual(hour_angle_hours,9,"Hour Angle Hours")
		self.assertEqual(hour_angle_minutes,52,"Hour Angle Minutes")
		self.assertEqual(hour_angle_seconds,23.66,"Hour Angle Seconds")

	def test_hour_angle_to_right_ascension(self):
		hour_angle_hours,hour_angle_minutes,hour_angle_seconds = PC.right_ascension_to_hour_angle(self.ra_hours,self.ra_minutes,self.ra_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		right_ascension_hours,right_ascension_minutes,right_ascension_seconds = PC.hour_angle_to_right_ascension(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		print(f"Hour Angle to Right Ascension:  [HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds} [LCT] {self.lct_hours}:{self.lct_minutes}:{self.lct_seconds} [DS] {self.is_daylight_saving} [ZC] {self.zone_correction} [LD] {self.local_month}/{self.local_day}/{self.local_year} [LON] {self.geographical_longitude} = [RA] {self.ra_hours}:{self.ra_minutes}:{self.ra_seconds}")

		self.assertEqual(right_ascension_hours,18,"Right Ascension Hours")
		self.assertEqual(right_ascension_minutes,32,"Right Ascension Minutes")
		self.assertEqual(right_ascension_seconds,21,"Right Ascension Seconds")

class test_equatorial_coordinates_horizon_coordinates(UT.TestCase):
	def setUp(self):
		self.hour_angle_hours = 5
		self.hour_angle_minutes = 51
		self.hour_angle_seconds = 44
		self.declination_degrees = 23
		self.declination_minutes = 13
		self.declination_seconds = 10
		self.geographical_latitude = 52

	def test_equatorial_coordinates_to_horizon_coordinates(self):
		azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds = PC.equatorial_coordinates_to_horizon_coordinates(self.hour_angle_hours,self.hour_angle_minutes,self.hour_angle_seconds,self.declination_degrees,self.declination_minutes,self.declination_seconds,self.geographical_latitude)

		print(f"Equatorial Coordinates to Horizon Coordinates:  [HA] {self.hour_angle_hours}:{self.hour_angle_minutes}:{self.hour_angle_seconds} [DEC] {self.declination_degrees}d {self.declination_minutes}m {self.declination_seconds}s [LAT] {self.geographical_latitude} = [AZ] {azimuth_degrees}d {azimuth_minutes}m {azimuth_seconds}s [ALT] {altitude_degrees}d {altitude_minutes}m {altitude_seconds}s")

		self.assertEqual(azimuth_degrees,283,"Azimuth Degrees")
		self.assertEqual(azimuth_minutes,16,"Azimuth Minutes")
		self.assertEqual(azimuth_seconds,15.7,"Azimuth Seconds")
		self.assertEqual(altitude_degrees,19,"Altitude Degrees")
		self.assertEqual(altitude_minutes,20,"Altitude Minutes")
		self.assertEqual(altitude_seconds,3.64,"Altitude Seconds")

	def test_horizon_coordinates_to_equatorial_coordinates(self):
		azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds = PC.equatorial_coordinates_to_horizon_coordinates(self.hour_angle_hours,self.hour_angle_minutes,self.hour_angle_seconds,self.declination_degrees,self.declination_minutes,self.declination_seconds,self.geographical_latitude)

		hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds = PC.horizon_coordinates_to_equatorial_coordinates(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,self.geographical_latitude)

		print(f"Horizon Coordinates to Equatorial Coordinates:  [AZ] {azimuth_degrees}d {azimuth_minutes}m {azimuth_seconds}s [ALT] {altitude_degrees}d {altitude_minutes}m {altitude_seconds}s [LAT] {self.geographical_latitude} = [HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds} [DEC] {declination_degrees}d {declination_minutes}m {declination_seconds}s)")

		self.assertEqual(hour_angle_hours,5,"Hour Angle Hours")
		self.assertEqual(hour_angle_minutes,51,"Hour Angle Minutes")
		self.assertEqual(hour_angle_seconds,44,"Hour Angle Seconds")
		self.assertEqual(declination_degrees,23,"Declination Degrees")
		self.assertEqual(declination_minutes,13,"Declination Minutes")
		self.assertEqual(declination_seconds,10,"Declination Seconds")

class test_ecliptic(UT.TestCase):
	def setUp(self):
		self.ecliptic_longitude_degrees = 139
		self.ecliptic_longitude_minutes = 41
		self.ecliptic_longitude_seconds = 10
		self.ecliptic_latitude_degrees = 4
		self.ecliptic_latitude_minutes = 52
		self.ecliptic_latitude_seconds = 31
		self.greenwich_day = 6
		self.greenwich_month = 7
		self.greenwich_year = 2009

	def test_mean_obliquity_of_the_ecliptic(self):
		g_day = 6
		g_month = 7
		g_year = 2009

		obliquity = PC.mean_obliquity_of_the_ecliptic(g_day,g_month,g_year)
		obliquity = round(obliquity,8)

		print(f"Mean obliquity of the ecliptic:  [Greenwich Date] {g_month}/{g_day}/{g_year} = [Obliquity] {obliquity}")

		self.assertEqual(obliquity,23.43805531,"Obliquity")

	def test_ecliptic_coordinate_to_equatorial_coordinate(self):
		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PC.ecliptic_coordinate_to_equatorial_coordinate(self.ecliptic_longitude_degrees,self.ecliptic_longitude_minutes,self.ecliptic_longitude_seconds,self.ecliptic_latitude_degrees,self.ecliptic_latitude_minutes,self.ecliptic_latitude_seconds,self.greenwich_day,self.greenwich_month,self.greenwich_year)

		print(f"Ecliptic Coordinates to Equatorial Coordinates:  [LON] {self.ecliptic_longitude_degrees}d {self.ecliptic_longitude_minutes}m {self.ecliptic_longitude_seconds}s [LAT] {self.ecliptic_latitude_degrees}d {self.ecliptic_latitude_minutes}m {self.ecliptic_latitude_seconds}s [GD] {self.greenwich_month}/{self.greenwich_day}/{self.greenwich_year} = [RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s")

		self.assertEqual(ra_hours,9,"RA Hours")
		self.assertEqual(ra_minutes,34,"RA Minutes")
		self.assertEqual(ra_seconds,53.4,"RA Seconds")
		self.assertEqual(dec_degrees,19,"Dec Degrees")
		self.assertEqual(dec_minutes,32,"Dec Minutes")
		self.assertEqual(dec_seconds,8.52,"Dec Seconds")

	def test_equatorial_coordinate_to_ecliptic_coordinate(self):
		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PC.ecliptic_coordinate_to_equatorial_coordinate(self.ecliptic_longitude_degrees,self.ecliptic_longitude_minutes,self.ecliptic_longitude_seconds,self.ecliptic_latitude_degrees,self.ecliptic_latitude_minutes,self.ecliptic_latitude_seconds,self.greenwich_day,self.greenwich_month,self.greenwich_year)

		ecl_long_deg,ecl_long_min,ecl_long_sec,ecl_lat_deg,ecl_lat_min,ecl_lat_sec = PC.equatorial_coordinate_to_ecliptic_coordinate(ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds,self.greenwich_day,self.greenwich_month,self.greenwich_year)

		print(f"Equatorial Coordinates to Ecliptic Coordinates:  [RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s [GD] {self.greenwich_month}/{self.greenwich_day}/{self.greenwich_year} = [LON] {ecl_long_deg}d {ecl_long_min}m {ecl_long_sec}s [LAT] {ecl_lat_deg}d {ecl_lat_min}m {ecl_lat_sec}s")

		self.assertEqual(ecl_long_deg,139,"Ecliptic Longitude Degrees")
		self.assertEqual(ecl_long_min,41,"Ecliptic Longitude Minutes")
		self.assertEqual(ecl_long_sec,9.97,"Ecliptic Longitude Seconds")
		self.assertEqual(ecl_lat_deg,4,"Ecliptic Latitude Degrees")
		self.assertEqual(ecl_lat_min,52,"Ecliptic Latitude Minutes")
		self.assertEqual(ecl_lat_sec,30.99,"Ecliptic Latitude Seconds")

class test_galactic(UT.TestCase):
	def setUp(self):
		self.ra_hours = 10
		self.ra_minutes = 21
		self.ra_seconds = 0
		self.dec_degrees = 10
		self.dec_minutes = 3
		self.dec_seconds = 11

	def test_equatorial_coordinate_to_galactic_coordinate(self):
		gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec = PC.equatorial_coordinate_to_galactic_coordinate(self.ra_hours,self.ra_minutes,self.ra_seconds,self.dec_degrees,self.dec_minutes,self.dec_seconds)

		print(f"Equatorial Coordinates to Galactic Coordinates:  [EQ] [RA] {self.ra_hours}:{self.ra_minutes}:{self.ra_seconds} [DEC] {self.dec_degrees}d {self.dec_minutes}m {self.dec_seconds}s = [GAL] [LON] {gal_long_deg}d {gal_long_min}m {gal_long_sec}s [LAT] {gal_lat_deg}d {gal_lat_min}m {gal_lat_sec}s")

		self.assertEqual(gal_long_deg,232,"Galactic Longitude Degrees")
		self.assertEqual(gal_long_min,14,"Galactic Longitude Minutes")
		self.assertEqual(gal_long_sec,52.38,"Galactic Longitude Seconds")
		self.assertEqual(gal_lat_deg,51,"Galactic Latitude Degrees")
		self.assertEqual(gal_lat_min,7,"Galactic Latitude Minutes")
		self.assertEqual(gal_lat_sec,20.16,"Galactic Latitude Seconds")

	def test_galactic_coordinate_to_equatorial_coordinate(self):
		gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec = PC.equatorial_coordinate_to_galactic_coordinate(self.ra_hours,self.ra_minutes,self.ra_seconds,self.dec_degrees,self.dec_minutes,self.dec_seconds)

		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PC.galactic_coordinate_to_equatorial_coordinate(gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec)

		print(f"Galactic Coordinates to Equatorial Coordinates:  [GAL] [LON] {gal_long_deg}d {gal_long_min}m {gal_long_sec}s [LAT] {gal_lat_deg}d {gal_lat_min}m {gal_lat_sec}s = [EQ] [RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s")

		self.assertEqual(ra_hours,10,"Right Ascension Hours")
		self.assertEqual(ra_minutes,21,"Right Ascension Minutes")
		self.assertEqual(ra_seconds,0,"Right Ascension Seconds")
		self.assertEqual(dec_degrees,10,"Declination Degrees")
		self.assertEqual(dec_minutes,3,"Declination Degrees")
		self.assertEqual(dec_seconds,11,"Declination Seconds")

class test_object_angles(UT.TestCase):
	def setUp(self):
		self.ra_long_1_hour_deg = 5
		self.ra_long_1_min = 13
		self.ra_long_1_sec = 31.7
		self.dec_lat_1_deg = -8
		self.dec_lat_1_min = 13
		self.dec_lat_1_sec = 30
		self.ra_long_2_hour_deg = 6
		self.ra_long_2_min = 44
		self.ra_long_2_sec = 13.4
		self.dec_lat_2_deg = -16
		self.dec_lat_2_min = 41
		self.dec_lat_2_sec = 11
		self.hour_or_degree = "H"

	def test_angle_between_two_objects(self):

		angle_deg,angle_min,angle_sec = PC.angle_between_two_objects(self.ra_long_1_hour_deg,self.ra_long_1_min,self.ra_long_1_sec,self.dec_lat_1_deg,self.dec_lat_1_min,self.dec_lat_1_sec,self.ra_long_2_hour_deg,self.ra_long_2_min,self.ra_long_2_sec,self.dec_lat_2_deg,self.dec_lat_2_min,self.dec_lat_2_sec,self.hour_or_degree)

		print (f"Angle between two objects:  [OBJ 1] [RA LON] {self.ra_long_1_hour_deg}h/d {self.ra_long_1_min}m {self.ra_long_1_sec}s [DEC LAT] {self.dec_lat_1_deg}d {self.dec_lat_1_min}m {self.dec_lat_1_sec}s [OBJ 2] [RA LON] {self.ra_long_2_hour_deg}h/d {self.ra_long_2_min}m {self.ra_long_2_sec}s [DEC LAT] {self.dec_lat_2_deg}d {self.dec_lat_2_min}m {self.dec_lat_2_sec}s [TYPE] {self.hour_or_degree} = [ANGLE] {angle_deg}d {angle_min}m {angle_sec}s")

		self.assertEqual(angle_deg,23,"Angle Degrees")
		self.assertEqual(angle_min,40,"Angle Minutes")
		self.assertEqual(angle_sec,25.86,"Angle Seconds")

class test_rise_set(UT.TestCase):
	def setUp(self):
		self.ra_hours = 23
		self.ra_minutes = 39
		self.ra_seconds = 20
		self.dec_deg = 21
		self.dec_min = 42
		self.dec_sec = 0
		self.gw_date_day = 24
		self.gw_date_month = 8
		self.gw_date_year = 2010
		self.geog_long_deg = 64
		self.geog_lat_deg = 30
		self.vert_shift_deg = 0.5667

	def test_rising_and_setting(self):
		rise_set_status,ut_rise_hour,ut_rise_min,ut_set_hour,ut_set_min,az_rise,az_set = PC.rising_and_setting(self.ra_hours,self.ra_minutes,self.ra_seconds,self.dec_deg,self.dec_min,self.dec_sec,self.gw_date_day,self.gw_date_month,self.gw_date_year,self.geog_long_deg,self.geog_lat_deg,self.vert_shift_deg)

		print(f"Rising and setting times:  [RA] {self.ra_hours}:{self.ra_minutes}:{self.ra_seconds} [DEC] {self.dec_deg}d {self.dec_min}m {self.dec_sec}s [GWD] {self.gw_date_month}/{self.gw_date_day}/{self.gw_date_year} [LON] {self.geog_long_deg} [LAT] {self.geog_lat_deg} [VS] {self.vert_shift_deg} = [STATUS] {rise_set_status} [UT] [RISE] {ut_rise_hour}:{ut_rise_min} [SET] {ut_set_hour}:{ut_set_min} [AZ] [RISE] {az_rise} [SET] {az_set}")

		self.assertEqual(rise_set_status,"OK","Rise/Set Status")
		self.assertEqual(ut_rise_hour,14,"UT Rise Hour")
		self.assertEqual(ut_rise_min,16,"UT Rise Minute")
		self.assertEqual(ut_set_hour,4,"UT Set Hour")
		self.assertEqual(ut_set_min,10,"UT Set Minute")
		self.assertEqual(az_rise,64.36,"AZ Rise")
		self.assertEqual(az_set,295.64,"AZ Set")

class test_precession(UT.TestCase):
	def setUp(self):
		self.ra_hour = 9
		self.ra_minutes = 10
		self.ra_seconds = 43
		self.dec_deg = 14
		self.dec_minutes = 23
		self.dec_seconds = 25
		self.epoch1_day = 0.923
		self.epoch1_month = 1
		self.epoch1_year = 1950
		self.epoch2_day = 1
		self.epoch2_month = 6
		self.epoch2_year = 1979

	def test_precession(self):
		corrected_ra_hour,corrected_ra_minutes,corrected_ra_seconds,corrected_dec_deg,corrected_dec_minutes,corrected_dec_seconds = PC.correct_for_precession(self.ra_hour,self.ra_minutes,self.ra_seconds,self.dec_deg,self.dec_minutes,self.dec_seconds,self.epoch1_day,self.epoch1_month,self.epoch1_year,self.epoch2_day,self.epoch2_month,self.epoch2_year)

		print(f"Precession:  [RA] {self.ra_hour}:{self.ra_minutes}:{self.ra_seconds} [DEC] {self.dec_deg}d {self.dec_minutes}m {self.dec_seconds}s [EPOCH 1] {self.epoch1_month}/{self.epoch1_day}/{self.epoch1_year} [EPOCH 2] {self.epoch2_month}/{self.epoch2_day}/{self.epoch2_year} = [Corrected] [RA] {corrected_ra_hour}:{corrected_ra_minutes}:{corrected_ra_seconds} [DEC] {corrected_dec_deg}d {corrected_dec_minutes}m {corrected_dec_seconds}s")

		self.assertEqual(corrected_ra_hour,9,"Corrected Right Ascension Hour")
		self.assertEqual(corrected_ra_minutes,12,"Corrected Right Ascension Minutes")
		self.assertEqual(corrected_ra_seconds,20.18,"Corrected Right Ascension Seconds")
		self.assertEqual(corrected_dec_deg,14,"Corrected Declination Hour")
		self.assertEqual(corrected_dec_minutes,16,"Corrected Declination Minutes")
		self.assertEqual(corrected_dec_seconds,9.12,"Corrected Declination Seconds")

class test_nutation(UT.TestCase):
	def setUp(self):
		self.greenwich_day = 1
		self.greenwich_month = 9
		self.greenwich_year = 1988

	def test_nutation(self):
		nut_in_long_deg,nut_in_obl_deg = PC.nutation_in_ecliptic_longitude_and_obliquity(self.greenwich_day,self.greenwich_month,self.greenwich_year)

		nut_in_long_deg = round(nut_in_long_deg,9)
		nut_in_obl_deg = round(nut_in_obl_deg,7)

		print(f"Nutation:  [GWDATE] {self.greenwich_month}/{self.greenwich_day}/{self.greenwich_year} = [NUTATION] [LON] {nut_in_long_deg} [OBL] {nut_in_obl_deg}")

		self.assertEqual(nut_in_long_deg,0.001525808,"Nutation in Longitude (degrees)")
		self.assertEqual(nut_in_obl_deg,0.0025671,"Nutation in Obliquity (degrees)")

class test_aberration(UT.TestCase):
	def setUp(self):
		self.ut_hour = 0
		self.ut_minutes = 0
		self.ut_seconds = 0
		self.gw_day = 8
		self.gw_month = 9
		self.gw_year = 1988
		self.true_ecl_long_deg = 352
		self.true_ecl_long_min = 37
		self.true_ecl_long_sec = 10.1
		self.true_ecl_lat_deg = -1
		self.true_ecl_lat_min = 32
		self.true_ecl_lat_sec = 56.4

	def test_correct_for_aberration(self):
		apparent_ecl_long_deg,apparent_ecl_long_min,apparent_ecl_long_sec,apparent_ecl_lat_deg,apparent_ecl_lat_min,apparent_ecl_lat_sec = PC.correct_for_aberration(self.ut_hour,self.ut_minutes,self.ut_seconds,self.gw_day,self.gw_month,self.gw_year,self.true_ecl_long_deg,self.true_ecl_long_min,self.true_ecl_long_sec,self.true_ecl_lat_deg,self.true_ecl_lat_min,self.true_ecl_lat_sec)

		print(f"Aberration:  [UT] {self.ut_hour}:{self.ut_minutes}:{self.ut_seconds} [GWD] {self.gw_month}/{self.gw_day}/{self.gw_year} [ECL] [LON] {self.true_ecl_long_deg}d {self.true_ecl_long_min}m {self.true_ecl_long_sec}s [LAT] {self.true_ecl_lat_deg}d {self.true_ecl_lat_min}m {self.true_ecl_lat_sec}s = [Apparent ECL] [LON] {apparent_ecl_long_deg}d {apparent_ecl_long_min}m {apparent_ecl_long_sec}s [LAT] {apparent_ecl_lat_deg}d {apparent_ecl_lat_min}m {apparent_ecl_lat_sec}s")

		self.assertEqual(apparent_ecl_long_deg,352,"Apparent Ecliptic Longitude Degrees")
		self.assertEqual(apparent_ecl_long_min,37,"Apparent Ecliptic Longitude Minutes")
		self.assertEqual(apparent_ecl_long_sec,30.45,"Apparent Ecliptic Longitude Seconds")
		self.assertEqual(apparent_ecl_lat_deg,-1,"Apparent Ecliptic Latitude Degrees")
		self.assertEqual(apparent_ecl_lat_min,32,"Apparent Ecliptic Latitude Minutes")
		self.assertEqual(apparent_ecl_lat_sec,56.33,"Apparent Ecliptic Latitude Seconds")

class test_atmospheric_refraction(UT.TestCase):
	def setUp(self):
		self.true_ra_hour = 23
		self.true_ra_min = 14
		self.true_ra_sec = 0
		self.true_dec_deg = 40
		self.true_dec_min = 10
		self.true_dec_sec = 0
		self.coordinate_type = "TRUE"
		self.geog_long_deg = 0.17
		self.geog_lat_deg = 51.2036110
		self.daylight_saving_hours = 0
		self.timezone_hours = 0
		self.lcd_day = 23
		self.lcd_month = 3
		self.lcd_year = 1987
		self.lct_hour = 1
		self.lct_min = 1
		self.lct_sec = 24
		self.atmospheric_pressure_mbar = 1012
		self.atmospheric_temperature_celsius = 21.7

	def test_atmospheric_refraction(self):
		corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec = PC.atmospheric_refraction(self.true_ra_hour,self.true_ra_min,self.true_ra_sec,self.true_dec_deg,self.true_dec_min,self.true_dec_sec,self.coordinate_type,self.geog_long_deg,self.geog_lat_deg,self.daylight_saving_hours,self.timezone_hours,self.lcd_day,self.lcd_month,self.lcd_year,self.lct_hour,self.lct_min,self.lct_sec,self.atmospheric_pressure_mbar,self.atmospheric_temperature_celsius)

		print(f"Refraction:  [RA] {self.true_ra_hour}:{self.true_ra_min}:{self.true_ra_sec} [DEC] {self.true_dec_deg}d {self.true_dec_min}m {self.true_dec_sec}s [COORD TYPE] {self.coordinate_type} [GEOG LON/LAT] {self.geog_long_deg}d/{self.geog_lat_deg}d [DS HOURS] {self.daylight_saving_hours} [TZ HOURS] {self.timezone_hours} [LCD] {self.lcd_month}/{self.lcd_day}/{self.lcd_year} [LCT] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [ATM] [PRESS MBR] {self.atmospheric_pressure_mbar} [TEMP C] {self.atmospheric_temperature_celsius} = [CORRECTED] [RA] {corrected_ra_hour}:{corrected_ra_min}:{corrected_ra_sec} [DEC] {corrected_dec_deg}d {corrected_dec_min}m {corrected_dec_sec}s")

		self.assertEqual(corrected_ra_hour,23,"Corrected RA Hours")
		self.assertEqual(corrected_ra_min,13,"Corrected RA Minutes")
		self.assertEqual(corrected_ra_sec,44.74,"Corrected RA Seconds")
		self.assertEqual(corrected_dec_deg,40,"Corrected Declination Degrees")
		self.assertEqual(corrected_dec_min,19,"Corrected Declination Minutes")
		self.assertEqual(corrected_dec_sec,45.76,"Corrected Declination Seconds")

class test_geocentric_parallax(UT.TestCase):
	def setUp(self):
		self.ra_hour = 22
		self.ra_min = 35
		self.ra_sec = 19
		self.dec_deg = -7
		self.dec_min = 41
		self.dec_sec = 13
		self.coordinate_type = "TRUE"
		self.equatorial_hor_parallax_deg = 1.019167
		self.geog_long_deg = -100
		self.geog_lat_deg = 50
		self.height_m = 60
		self.daylight_saving = 0
		self.timezone_hours = -6
		self.lcd_day = 26
		self.lcd_month = 2
		self.lcd_year = 1979
		self.lct_hour = 10
		self.lct_min = 45
		self.lct_sec = 0
	
	def test_corrections_for_geocentric_parallax(self):
		corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec = PC.corrections_for_geocentric_parallax(self.ra_hour,self.ra_min,self.ra_sec,self.dec_deg,self.dec_min,self.dec_sec,self.coordinate_type,self.equatorial_hor_parallax_deg,self.geog_long_deg,self.geog_lat_deg,self.height_m,self.daylight_saving,self.timezone_hours,self.lcd_day,self.lcd_month,self.lcd_year,self.lct_hour,self.lct_min,self.lct_sec)

		print(f"Geocentric parallax:  [RA] {self.ra_hour}:{self.ra_min}:{self.ra_sec} [DEC] {self.dec_deg}d {self.dec_min}m {self.dec_sec}s [COORD TYPE] {self.coordinate_type} [EQ HOR PARA DEG] {self.equatorial_hor_parallax_deg} [GEOG] [LON] {self.geog_long_deg} [LAT] {self.geog_lat_deg} [HEIGHT] {self.height_m} [DS] {self.daylight_saving} [TZ] {self.timezone_hours} [LCD] {self.lcd_month}/{self.lcd_day}/{self.lcd_year} [LCT] {self.lct_hour}:{self.lct_min}:{self.lct_sec} = [CORRECTED] [RA] {corrected_ra_hour}:{corrected_ra_min}:{corrected_ra_sec} [DEC] {corrected_dec_deg}d {corrected_dec_min}m {corrected_dec_sec}s")

		self.assertEqual(corrected_ra_hour,22,"Corrected RA Hours")
		self.assertEqual(corrected_ra_min,36,"Corrected RA Minutes")
		self.assertEqual(corrected_ra_sec,43.22,"Corrected RA Seconds")
		self.assertEqual(corrected_dec_deg,-8,"Corrected Declination Degrees")
		self.assertEqual(corrected_dec_min,32,"Corrected Declination Minutes")
		self.assertEqual(corrected_dec_sec,17.4,"Corrected Declination Seconds")

class test_heliographic_coordinates(UT.TestCase):
	def setUp(self):
		self.helio_position_angle_deg = 220
		self.helio_displacement_arcmin = 10.5
		self.gwdate_day = 1
		self.gwdate_month = 5
		self.gwdate_year = 1988

	def test_heliographic_coordinates(self):
		helio_long_deg,helio_lat_deg = PC.heliographic_coordinates(self.helio_position_angle_deg,self.helio_displacement_arcmin,self.gwdate_day,self.gwdate_month,self.gwdate_year)

		print(f"Heliographic coordinates:  [helio] [pos angle] {self.helio_position_angle_deg} [displ arcmin] {self.helio_displacement_arcmin}, [GW Date] {self.gwdate_month}/{self.gwdate_day}/{self.gwdate_year} = [helio] [lon] {helio_long_deg}d [lat] {helio_lat_deg}d")

		self.assertEqual(helio_long_deg,142.59,"Heliographic Longitude - degrees")
		self.assertEqual(helio_lat_deg,-19.94,"Heliographic Latitude - degrees")

class test_carrington_rotation_number(UT.TestCase):
	def setUp(self):
		self.gwdate_day = 27
		self.gwdate_month = 1
		self.gwdate_year = 1975

	def test_carrington_rotation_number(self):
		crn = PC.carrington_rotation_number(self.gwdate_day,self.gwdate_month,self.gwdate_year)

		print(f"Carrington Rotation Number:  [GW Date] {self.gwdate_month}/{self.gwdate_day}/{self.gwdate_year} = [CRN] {crn}")

		self.assertEqual(crn,1624,"Carrington Rotation Number")

class test_selenographic_coordinates(UT.TestCase):
	def setUp(self):
		self.gwdate_day = 1
		self.gwdate_month = 5
		self.gwdate_year = 1988

	def test_selenographic_coordinates_1(self):
		sub_earth_longitude,sub_earth_latitude,position_angle_of_pole = PC.selenographic_coordinates_1(self.gwdate_day,self.gwdate_month,self.gwdate_year)

		print(f"Selenographic Coordinates 1:  [GW Date] {self.gwdate_month}/{self.gwdate_day}/{self.gwdate_year} = [Sub Earth] [LON] {sub_earth_longitude} [LAT] {sub_earth_latitude}, [POS ANGLE OF POLE] {position_angle_of_pole}")

		self.assertEqual(sub_earth_longitude,-4.88,"Sub-Earth Longitude")
		self.assertEqual(sub_earth_latitude,4.04,"Sub-Earth Latitude")
		self.assertEqual(position_angle_of_pole,19.78,"Position Angle of Pole")

	def test_selenographic_coordinates_2(self):
		sub_solar_longitude,sub_solar_colongitude,sub_solar_latitude = PC.selenographic_coordinates_2(self.gwdate_day,self.gwdate_month,self.gwdate_year)

		print(f"Selenographic Coordinates 2:  [GW Date] {self.gwdate_month}/{self.gwdate_day}/{self.gwdate_year} = [Sub Solar] [LON] {sub_solar_longitude} [COLN] {sub_solar_colongitude} [LAT] {sub_solar_latitude}")

		self.assertEqual(sub_solar_longitude,6.81,"Sub-Solar Longitude")
		self.assertEqual(sub_solar_colongitude,83.19,"Sub-Solar Colongitude")
		self.assertEqual(sub_solar_latitude,1.19,"Sub-Solar Latitude")
	
if __name__ == '__main__':
	UT.main()

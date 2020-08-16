import math
from . import pa_macro as PM

def angle_to_decimal_degrees(degrees, minutes, seconds):
	""" Convert an Angle (degrees, minutes, and seconds) to Decimal Degrees """
	A = abs(seconds)/60
	B = (abs(minutes)+A)/60
	C = abs(degrees)+B
	D = -(C) if degrees < 0 or minutes < 0 or seconds < 0 else C

	return D

def decimal_degrees_to_angle(decimalDegrees):
	"""
	Convert Decimal Degrees to an Angle (degrees, minutes, and seconds)
	
	Returns:
		degrees, minutes, seconds
	"""
	unsignedDecimal = abs(decimalDegrees)
	totalSeconds = unsignedDecimal * 3600
	seconds2dp = round(totalSeconds % 60, 2)
	correctedSeconds = 0 if seconds2dp == 60 else seconds2dp
	correctedRemainder = totalSeconds + 60 if seconds2dp == 60 else totalSeconds
	minutes = math.floor(correctedRemainder/60) % 60
	unsignedDegrees = math.floor(correctedRemainder / 3600)
	signedDegrees = -1 * unsignedDegrees if decimalDegrees < 0 else unsignedDegrees

	return signedDegrees,minutes,math.floor(correctedSeconds)

def right_ascension_to_hour_angle(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, is_daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude):
	""" Convert Right Ascension to Hour Angle """
	daylight_saving = 1 if is_daylight_saving == True else 0

	hour_angle = PM.ra_ha(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude)

	hour_angle_hours = PM.dh_hour(hour_angle)
	hour_angle_minutes = PM.dh_min(hour_angle)
	hour_angle_seconds = PM.dh_sec(hour_angle)

	return hour_angle_hours,hour_angle_minutes,hour_angle_seconds

def hour_angle_to_right_ascension(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,is_daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude):
	""" Convert Hour Angle to Right Ascension """
	daylight_saving = 1 if is_daylight_saving == True else 0

	right_ascension = PM.ha_ra(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude)

	right_ascension_hours = PM.dh_hour(right_ascension)
	right_ascension_minutes = PM.dh_min(right_ascension)
	right_ascension_seconds = PM.dh_sec(right_ascension)

	return right_ascension_hours,right_ascension_minutes,right_ascension_seconds

def equatorial_coordinates_to_horizon_coordinates(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	""" Convert Equatorial Coordinates to Horizon Coordinates """
	azimuth_in_decimal_degrees = PM.eq_az(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude)

	altitude_in_decimal_degrees = PM.eq_alt(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude)

	azimuth_degrees = PM.dd_deg(azimuth_in_decimal_degrees)
	azimuth_minutes = PM.dd_min(azimuth_in_decimal_degrees)
	azimuth_seconds = PM.dd_sec(azimuth_in_decimal_degrees)

	altitude_degrees = PM.dd_deg(altitude_in_decimal_degrees)
	altitude_minutes = PM.dd_min(altitude_in_decimal_degrees)
	altitude_seconds = PM.dd_sec(altitude_in_decimal_degrees)

	return azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds

def horizon_coordinates_to_equatorial_coordinates(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	""" Convert Horizon Coordinates to Equatorial Coordinates """
	hour_angle_in_decimal_degrees = PM.hor_ha(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude)

	declination_in_decimal_degrees = PM.hor_dec(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude)

	hour_angle_hours = PM.dh_hour(hour_angle_in_decimal_degrees)
	hour_angle_minutes = PM.dh_min(hour_angle_in_decimal_degrees)
	hour_angle_seconds = PM.dh_sec(hour_angle_in_decimal_degrees)

	declination_degrees = PM.dd_deg(declination_in_decimal_degrees)
	declination_minutes = PM.dd_min(declination_in_decimal_degrees)
	declination_seconds = PM.dd_sec(declination_in_decimal_degrees)

	return hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds

def mean_obliquity_of_the_ecliptic(greenwich_day,greenwich_month,greenwich_year):
	""" Calculate Mean Obliquity of the Ecliptic for a Greenwich Date """
	JD = PM.cd_jd(greenwich_day,greenwich_month,greenwich_year)
	MJD = JD - 2451545
	T = MJD / 36525
	DE1 = T * (46.815 + T * (0.0006 - (T * 0.00181)))
	DE2 = DE1 / 3600

	return 23.439292 - DE2

def ecliptic_coordinate_to_equatorial_coordinate(ecliptic_longitude_degrees,ecliptic_longitude_minutes,ecliptic_longitude_seconds,ecliptic_latitude_degrees,ecliptic_latitude_minutes,ecliptic_latitude_seconds,greenwich_day,greenwich_month,greenwich_year):
	""" Convert Ecliptic Coordinates to Equatorial Coordinates """
	eclon_deg = PM.dms_dd(ecliptic_longitude_degrees,ecliptic_longitude_minutes,ecliptic_longitude_seconds)
	eclat_deg = PM.dms_dd(ecliptic_latitude_degrees,ecliptic_latitude_minutes,ecliptic_latitude_seconds)
	eclon_rad = math.radians(eclon_deg)
	eclat_rad = math.radians(eclat_deg)
	obliq_deg = PM.obliq(greenwich_day,greenwich_month,greenwich_year)
	obliq_rad = math.radians(obliq_deg)
	sin_dec = math.sin(eclat_rad) * math.cos(obliq_rad) + math.cos(eclat_rad) * math.sin(obliq_rad) * math.sin(eclon_rad)
	dec_rad = math.asin(sin_dec)
	dec_deg = PM.degrees(dec_rad)
	y = math.sin(eclon_rad) * math.cos(obliq_rad) - math.tan(eclat_rad) * math.sin(obliq_rad)
	x = math.cos(eclon_rad)
	ra_rad = math.atan2(y,x)
	ra_deg1 = PM.degrees(ra_rad)
	ra_deg2 = ra_deg1 - 360 * math.floor(ra_deg1/360)
	ra_hours = PM.dd_dh(ra_deg2)

	out_ra_hours = PM.dh_hour(ra_hours)
	out_ra_minutes = PM.dh_min(ra_hours)
	out_ra_seconds = PM.dh_sec(ra_hours)
	out_dec_degrees = PM.dd_deg(dec_deg)
	out_dec_minutes = PM.dd_min(dec_deg)
	out_dec_seconds = PM.dd_sec(dec_deg)

	return out_ra_hours,out_ra_minutes,out_ra_seconds,out_dec_degrees,out_dec_minutes,out_dec_seconds

def equatorial_coordinate_to_ecliptic_coordinate(ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds,gw_day,gw_month,gw_year):
	""" Convert Equatorial Coordinates to Ecliptic Coordinates """
	ra_deg = PM.dh_dd(PM.hms_dh(ra_hours,ra_minutes,ra_seconds))
	dec_deg = PM.dms_dd(dec_degrees,dec_minutes,dec_seconds)
	ra_rad = math.radians(ra_deg)
	dec_rad = math.radians(dec_deg)
	obliq_deg = PM.obliq(gw_day,gw_month,gw_year)
	obliq_rad = math.radians(obliq_deg)
	sin_ecl_lat = math.sin(dec_rad) * math.cos(obliq_rad) - math.cos(dec_rad) * math.sin(obliq_rad) * math.sin(ra_rad)
	ecl_lat_rad = math.asin(sin_ecl_lat)
	ecl_lat_deg = PM.degrees(ecl_lat_rad)
	y = math.sin(ra_rad) * math.cos(obliq_rad) + math.tan(dec_rad) * math.sin(obliq_rad)
	x = math.cos(ra_rad)
	ecl_long_rad = math.atan2(y,x)
	ecl_long_deg1 = PM.degrees(ecl_long_rad)
	ecl_long_deg2 = ecl_long_deg1 - 360 * math.floor(ecl_long_deg1/360)

	out_ecl_long_deg = PM.dd_deg(ecl_long_deg2)
	out_ecl_long_min = PM.dd_min(ecl_long_deg2)
	out_ecl_long_sec = PM.dd_sec(ecl_long_deg2)
	out_ecl_lat_deg = PM.dd_deg(ecl_lat_deg)
	out_ecl_lat_min = PM.dd_min(ecl_lat_deg)
	out_ecl_lat_sec = PM.dd_sec(ecl_lat_deg)

	return out_ecl_long_deg,out_ecl_long_min,out_ecl_long_sec,out_ecl_lat_deg,out_ecl_lat_min,out_ecl_lat_sec

def equatorial_coordinate_to_galactic_coordinate(ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds):
	""" Convert Equatorial Coordinates to Galactic Coordinates """
	ra_deg = PM.dh_dd(PM.hms_dh(ra_hours,ra_minutes,ra_seconds))
	dec_deg = PM.dms_dd(dec_degrees,dec_minutes,dec_seconds)
	ra_rad = math.radians(ra_deg)
	dec_rad = math.radians(dec_deg)
	sin_b = math.cos(dec_rad) * math.cos(math.radians(27.4)) * math.cos(ra_rad - math.radians(192.25)) + math.sin(dec_rad) * math.sin(math.radians(27.4))
	b_radians = math.asin(sin_b)
	b_deg = PM.degrees(b_radians)
	y = math.sin(dec_rad) - sin_b * math.sin(math.radians(27.4))
	x = math.cos(dec_rad) * math.sin(ra_rad - math.radians(192.25)) * math.cos(math.radians(27.4))
	long_deg1 = PM.degrees(math.atan2(y,x)) + 33
	long_deg2 = long_deg1 - 360 * math.floor(long_deg1/360)

	gal_long_deg = PM.dd_deg(long_deg2)
	gal_long_min = PM.dd_min(long_deg2)
	gal_long_sec = PM.dd_sec(long_deg2)
	gal_lat_deg = PM.dd_deg(b_deg)
	gal_lat_min = PM.dd_min(b_deg)
	gal_lat_sec = PM.dd_sec(b_deg)

	return gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec

def galactic_coordinate_to_equatorial_coordinate(gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec):
	""" Convert Galactic Coordinates to Equatorial Coordinates """
	glong_deg = PM.dms_dd(gal_long_deg,gal_long_min,gal_long_sec)
	glat_deg = PM.dms_dd(gal_lat_deg,gal_lat_min,gal_lat_sec)
	glong_rad = math.radians(glong_deg)
	glat_rad = math.radians(glat_deg)
	sin_dec = math.cos(glat_rad) * math.cos(math.radians(27.4)) * math.sin(glong_rad - math.radians(33)) + math.sin(glat_rad) * math.sin(math.radians(27.4))
	dec_radians = math.asin(sin_dec)
	dec_deg = PM.degrees(dec_radians)
	y = math.cos(glat_rad) *math.cos(glong_rad - math.radians(33))
	x = math.sin(glat_rad) * math.cos(math.radians(27.4)) - math.cos(glat_rad) * math.sin(math.radians(27.4)) * math.sin(glong_rad - math.radians(33))
	
	ra_deg1 = PM.degrees(math.atan2(y,x)) + 192.25
	ra_deg2 = ra_deg1 - 360 * math.floor(ra_deg1/360)
	ra_hours1 = PM.dd_dh(ra_deg2)

	ra_hours = PM.dh_hour(ra_hours1)
	ra_minutes = PM.dh_min(ra_hours1)
	ra_seconds = PM.dh_sec(ra_hours1)
	dec_degrees = PM.dd_deg(dec_deg)
	dec_minutes = PM.dd_min(dec_deg)
	dec_seconds = PM.dd_sec(dec_deg)

	return ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds

def angle_between_two_objects(ra_long_1_hour_deg,ra_long_1_min,ra_long_1_sec,dec_lat_1_deg,dec_lat_1_min,dec_lat_1_sec,ra_long_2_hour_deg,ra_long_2_min,ra_long_2_sec,dec_lat_2_deg,dec_lat_2_min,dec_lat_2_sec,hour_or_degree):
	""" Calculate the angle between two celestial objects """
	ra_long_1_decimal = PM.hms_dh(ra_long_1_hour_deg,ra_long_1_min,ra_long_1_sec) if hour_or_degree == "H" else PM.dms_dd(ra_long_1_hour_deg,ra_long_1_min,ra_long_1_sec)
	ra_long_1_deg = PM.dh_dd(ra_long_1_decimal) if hour_or_degree == "H" else ra_long_1_decimal
	ra_long_1_rad = math.radians(ra_long_1_deg)
	dec_lat_1_deg1 = PM.dms_dd(dec_lat_1_deg,dec_lat_1_min,dec_lat_1_sec)
	dec_lat_1_rad = math.radians(dec_lat_1_deg1)

	ra_long_2_decimal = PM.hms_dh(ra_long_2_hour_deg,ra_long_2_min,ra_long_2_sec) if hour_or_degree == "H" else PM.dms_dd(ra_long_2_hour_deg,ra_long_2_min,ra_long_2_sec)
	ra_long_2_deg = PM.dh_dd(ra_long_2_decimal) if hour_or_degree == "H" else ra_long_2_decimal
	ra_long_2_rad = math.radians(ra_long_2_deg)
	dec_lat_2_deg1 = PM.dms_dd(dec_lat_2_deg,dec_lat_2_min,dec_lat_2_sec)
	dec_lat_2_rad = math.radians(dec_lat_2_deg1)

	cos_d = math.sin(dec_lat_1_rad) * math.sin(dec_lat_2_rad) + math.cos(dec_lat_1_rad) * math.cos(dec_lat_2_rad) * math.cos(ra_long_1_rad - ra_long_2_rad)
	d_rad = math.acos(cos_d)
	d_deg = PM.degrees(d_rad)

	angle_deg = PM.dd_deg(d_deg)
	angle_min = PM.dd_min(d_deg)
	angle_sec = PM.dd_sec(d_deg)

	return angle_deg,angle_min,angle_sec

def rising_and_setting(ra_hours,ra_minutes,ra_seconds,dec_deg,dec_min,dec_sec,gw_date_day,gw_date_month,gw_date_year,geog_long_deg,geog_lat_deg,vert_shift_deg):
	"""
	Rising and setting times

	Arguments:
		ra_hours -- Right Ascension, in hours.
		ra_minutes -- Right Ascension, in minutes.
		ra_seconds -- Right Ascension, in seconds.
		dec_deg -- Declination, in degrees.
		dec_min -- Declination, in minutes.
		dec_sec -- Declination, in seconds.
		gw_date_day -- Greenwich Date, day part.
		gw_date_month -- Greenwich Date, month part.
		gw_date_year -- Greenwich Date, year part.
		geog_long_deg -- Geographical Longitude, in degrees.
		geog_lat_deg -- Geographical Latitude, in degrees.
		vert_shift_deg -- Vertical Shift, in degrees.

	Returns:
		rise_set_status -- "Never Rises", "Circumpolar", or "OK".
		ut_rise_hour -- Rise time, UT, hour part.
		ut_rise_min -- Rise time, UT, minute part.
		ut_set_hour -- Set time, UT, hour part.
		ut_set_min -- Set time, UT, minute part.
		az_rise -- Azimuth angle, at rise.
		az_set -- Azimuth angle, at set.
	"""
	ra_hours1 = PM.hms_dh(ra_hours,ra_minutes,ra_seconds)
	dec_rad = math.radians(PM.dms_dd(dec_deg,dec_min,dec_sec))
	vertical_displ_radians = math.radians(vert_shift_deg)
	geo_lat_radians = math.radians(geog_lat_deg)
	cos_h = -(math.sin(vertical_displ_radians) + math.sin(geo_lat_radians) * math.sin(dec_rad)) / (math.cos(geo_lat_radians) * math.cos(dec_rad))
	h_hours = PM.dd_dh(PM.degrees(math.acos(cos_h)))
	lst_rise_hours = (ra_hours1-h_hours)-24*math.floor((ra_hours1-h_hours)/24)
	lst_set_hours = (ra_hours1+h_hours)-24*math.floor((ra_hours1+h_hours)/24)
	a_deg = PM.degrees(math.acos((math.sin(dec_rad)+math.sin(vertical_displ_radians)*math.sin(geo_lat_radians))/(math.cos(vertical_displ_radians)*math.cos(geo_lat_radians))))
	az_rise_deg = a_deg - 360 * math.floor(a_deg/360)
	az_set_deg = (360-a_deg)-360*math.floor((360-a_deg)/360)
	ut_rise_hours1 = PM.gst_ut(PM.lst_gst(lst_rise_hours,0,0,geog_long_deg),0,0,gw_date_day,gw_date_month,gw_date_year)
	ut_set_hours1 = PM.gst_ut(PM.lst_gst(lst_set_hours,0,0,geog_long_deg),0,0,gw_date_day,gw_date_month,gw_date_year)
	ut_rise_adjusted_hours = ut_rise_hours1 + 0.008333
	ut_set_adjusted_hours = ut_set_hours1 + 0.008333

	rise_set_status = "never rises" if cos_h > 1 else "circumpolar" if cos_h < -1 else "OK"
	ut_rise_hour = PM.dh_hour(ut_rise_adjusted_hours) if rise_set_status == "OK" else None
	ut_rise_min = PM.dh_min(ut_rise_adjusted_hours) if rise_set_status == "OK" else None
	ut_set_hour = PM.dh_hour(ut_set_adjusted_hours) if rise_set_status == "OK" else None
	ut_set_min = PM.dh_min(ut_set_adjusted_hours) if rise_set_status == "OK" else None
	az_rise = round(az_rise_deg,2) if rise_set_status == "OK" else None
	az_set = round(az_set_deg,2) if rise_set_status == "OK" else None

	return rise_set_status,ut_rise_hour,ut_rise_min,ut_set_hour,ut_set_min,az_rise,az_set

def correct_for_precession(ra_hour,ra_minutes,ra_seconds,dec_deg,dec_minutes,dec_seconds,epoch1_day,epoch1_month,epoch1_year,epoch2_day,epoch2_month,epoch2_year):
	"""
	Calculate precession (corrected coordinates between two epochs)

	Returns:
		corrected RA hour
		corrected RA minutes
		corrected RA seconds
		corrected Declination degrees
		corrected Declination minutes
		corrected Declination seconds
	"""
	ra_1_rad = math.radians(PM.dh_dd(PM.hms_dh(ra_hour,ra_minutes,ra_seconds)))
	dec_1_rad = math.radians(PM.dms_dd(dec_deg,dec_minutes,dec_seconds))
	t_centuries = (PM.cd_jd(epoch1_day,epoch1_month,epoch1_year)-2415020)/36525
	m_sec = 3.07234+(0.00186*t_centuries)
	n_arcsec = 20.0468-(0.0085*t_centuries)
	n_years = (PM.cd_jd(epoch2_day,epoch2_month,epoch2_year)-PM.cd_jd(epoch1_day,epoch1_month,epoch1_year))/365.25
	s1_hours = ((m_sec+(n_arcsec*math.sin(ra_1_rad)*math.tan(dec_1_rad)/15))*n_years)/3600
	ra_2_hours = PM.hms_dh(ra_hour,ra_minutes,ra_seconds)+s1_hours
	s2_deg = (n_arcsec*math.cos(ra_1_rad)*n_years)/3600
	dec_2_deg = PM.dms_dd(dec_deg,dec_minutes,dec_seconds)+s2_deg

	corrected_ra_hour = PM.dh_hour(ra_2_hours)
	corrected_ra_minutes = PM.dh_min(ra_2_hours)
	corrected_ra_seconds = PM.dh_sec(ra_2_hours)
	corrected_dec_deg = PM.dd_deg(dec_2_deg)
	corrected_dec_minutes = PM.dd_min(dec_2_deg)
	corrected_dec_seconds = PM.dd_sec(dec_2_deg)

	return corrected_ra_hour,corrected_ra_minutes,corrected_ra_seconds,corrected_dec_deg,corrected_dec_minutes,corrected_dec_seconds

def nutation_in_ecliptic_longitude_and_obliquity(greenwich_day, greenwich_month, greenwich_year):
	"""
	Calculate nutation for two values: ecliptic longitude and obliquity, for a Greenwich date.

	Returns:
		nutation in ecliptic longitude (degrees)
		nutation in obliquity (degrees)
	"""
	jd_days = PM.cd_jd(greenwich_day,greenwich_month,greenwich_year)
	t_centuries = (jd_days - 2415020) /36525
	a_deg = 100.0021358 * t_centuries
	l_1_deg = 279.6967 + (0.000303 * t_centuries * t_centuries)
	l_deg1 = l_1_deg + 360 * (a_deg - math.floor(a_deg))
	l_deg2 = l_deg1 - 360 * math.floor(l_deg1/360)
	l_rad = math.radians(l_deg2)
	b_deg = 5.372617 * t_centuries
	n_deg1 = 259.1833 - 360 * (b_deg - math.floor(b_deg))
	n_deg2 = n_deg1 - 360 * (math.floor(n_deg1/360))
	n_rad = math.radians(n_deg2)
	nut_in_long_arcsec = -17.2 * math.sin(n_rad) - 1.3 * math.sin(2 * l_rad)
	nut_in_obl_arcsec = 9.2 * math.cos(n_rad) + 0.5 * math.cos(2 * l_rad)

	nut_in_long_deg = nut_in_long_arcsec / 3600
	nut_in_obl_deg = nut_in_obl_arcsec / 3600

	return nut_in_long_deg,nut_in_obl_deg

def correct_for_aberration(ut_hour,ut_minutes,ut_seconds,gw_day,gw_month,gw_year,true_ecl_long_deg,true_ecl_long_min,true_ecl_long_sec,true_ecl_lat_deg,true_ecl_lat_min,true_ecl_lat_sec):
	"""
	Correct ecliptic coordinates for the effects of aberration.

	Returns:
		apparent ecliptic longitude (degrees, minutes, seconds)
		apparent ecliptic latitude (degrees, minutes, seconds)
	"""
	true_long_deg = PM.dms_dd(true_ecl_long_deg,true_ecl_long_min,true_ecl_long_sec)
	true_lat_deg = PM.dms_dd(true_ecl_lat_deg,true_ecl_lat_min,true_ecl_lat_sec)
	sun_true_long_deg = PM.sun_long(ut_hour,ut_minutes,ut_seconds,0,0,gw_day,gw_month,gw_year)
	dlong_arcsec = -20.5 * math.cos(math.radians(sun_true_long_deg-true_long_deg))/math.cos(math.radians(true_lat_deg))
	dlat_arcsec = -20.5 * math.sin(math.radians(sun_true_long_deg-true_long_deg))*math.sin(math.radians(true_lat_deg))
	apparent_long_deg = true_long_deg + (dlong_arcsec/3600)
	apparent_lat_deg = true_lat_deg + (dlat_arcsec / 3600)

	apparent_ecl_long_deg = PM.dd_deg(apparent_long_deg)
	apparent_ecl_long_min = PM.dd_min(apparent_long_deg)
	apparent_ecl_long_sec = PM.dd_sec(apparent_long_deg)
	apparent_ecl_lat_deg = PM.dd_deg(apparent_lat_deg)
	apparent_ecl_lat_min = PM.dd_min(apparent_lat_deg)
	apparent_ecl_lat_sec = PM.dd_sec(apparent_lat_deg)

	return apparent_ecl_long_deg,apparent_ecl_long_min,apparent_ecl_long_sec,apparent_ecl_lat_deg,apparent_ecl_lat_min,apparent_ecl_lat_sec

def atmospheric_refraction(true_ra_hour,true_ra_min,true_ra_sec,true_dec_deg,true_dec_min,true_dec_sec,coordinate_type,geog_long_deg,geog_lat_deg,daylight_saving_hours,timezone_hours,lcd_day,lcd_month,lcd_year,lct_hour,lct_min,lct_sec,atmospheric_pressure_mbar,atmospheric_temperature_celsius):
	"""
	Calculate corrected RA/Dec, accounting for atmospheric refraction.

	NOTE: Valid values for coordinate_type are "TRUE" and "APPARENT".

	Returns:
		corrected RA hours,minutes,seconds
		corrected Declination degrees,minutes,seconds
	"""
	ha_hour = PM.ra_ha(true_ra_hour,true_ra_min,true_ra_sec,lct_hour,lct_min,lct_sec,daylight_saving_hours,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)

	azimuth_deg = PM.eq_az(ha_hour,0,0,true_dec_deg,true_dec_min,true_dec_sec,geog_lat_deg)

	altitude_deg = PM.eq_alt(ha_hour,0,0,true_dec_deg,true_dec_min,true_dec_sec,geog_lat_deg)
	
	corrected_altitude_deg = PM.refract(altitude_deg,coordinate_type,atmospheric_pressure_mbar,atmospheric_temperature_celsius)

	corrected_ha_hour = PM.hor_ha(azimuth_deg,0,0,corrected_altitude_deg,0,0,geog_lat_deg)
	corrected_ra_hour1 = PM.ha_ra(corrected_ha_hour,0,0,lct_hour,lct_min,lct_sec,daylight_saving_hours,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)
	corrected_dec_deg1 = PM.hor_dec(azimuth_deg,0,0,corrected_altitude_deg,0,0,geog_lat_deg)

	corrected_ra_hour = PM.dh_hour(corrected_ra_hour1)
	corrected_ra_min = PM.dh_min(corrected_ra_hour1)
	corrected_ra_sec = PM.dh_sec(corrected_ra_hour1)
	corrected_dec_deg = PM.dd_deg(corrected_dec_deg1)
	corrected_dec_min = PM.dd_min(corrected_dec_deg1)
	corrected_dec_sec = PM.dd_sec(corrected_dec_deg1)

	return corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec

def corrections_for_geocentric_parallax(ra_hour,ra_min,ra_sec,dec_deg,dec_min,dec_sec,coordinate_type,equatorial_hor_parallax_deg,geog_long_deg,geog_lat_deg,height_m,daylight_saving,timezone_hours,lcd_day,lcd_month,lcd_year,lct_hour,lct_min,lct_sec):
	"""
	Calculate corrected RA/Dec, accounting for geocentric parallax.

	NOTE: Valid values for coordinate_type are "TRUE" and "APPARENT".

	Returns:
		corrected RA hours,minutes,seconds
		corrected Declination degrees,minutes,seconds
	"""
	ha_hours = PM.ra_ha(ra_hour,ra_min,ra_sec,lct_hour,lct_min,lct_sec,daylight_saving,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)

	corrected_ha_hours = PM.parallax_ha(ha_hours,0,0,dec_deg,dec_min,dec_sec,coordinate_type,geog_lat_deg,height_m,equatorial_hor_parallax_deg)

	corrected_ra_hours = PM.ha_ra(corrected_ha_hours,0,0,lct_hour,lct_min,lct_sec,daylight_saving,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)

	corrected_dec_deg1 = PM.parallax_dec(ha_hours,0,0,dec_deg,dec_min,dec_sec,coordinate_type,geog_lat_deg,height_m,equatorial_hor_parallax_deg)

	corrected_ra_hour = PM.dh_hour(corrected_ra_hours)
	corrected_ra_min = PM.dh_min(corrected_ra_hours)
	corrected_ra_sec = PM.dh_sec(corrected_ra_hours)
	corrected_dec_deg = PM.dd_deg(corrected_dec_deg1)
	corrected_dec_min = PM.dd_min(corrected_dec_deg1)
	corrected_dec_sec = PM.dd_sec(corrected_dec_deg1)

	return corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec

def heliographic_coordinates(helio_position_angle_deg,helio_displacement_arcmin,gwdate_day,gwdate_month,gwdate_year):
	"""
	Calculate heliographic coordinates for a given Greenwich date, with a given heliographic position angle and heliographic displacement in arc minutes.

	Returns:
		heliographic longitude and heliographic latitude, in degrees
	"""
	julian_date_days = PM.cd_jd(gwdate_day,gwdate_month,gwdate_year)
	t_centuries = (julian_date_days-2415020)/36525
	long_asc_node_deg = PM.dms_dd(74,22,0)+(84*t_centuries/60)
	sun_long_deg = PM.sun_long(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	y = math.sin(math.radians(long_asc_node_deg-sun_long_deg))*math.cos(math.radians(PM.dms_dd(7,15,0)))
	x = -math.cos(math.radians(long_asc_node_deg-sun_long_deg))
	a_deg = PM.degrees(math.atan2(y,x))
	m_deg1 = 360-(360*(julian_date_days-2398220)/25.38)
	m_deg2 = m_deg1-360*math.floor(m_deg1/360)
	l0_deg1 = m_deg2 + a_deg
	l0_deg2 = l0_deg1-360*math.floor(l0_deg1/360)
	b0_rad = math.asin(math.sin(math.radians(sun_long_deg-long_asc_node_deg))*math.sin(math.radians(PM.dms_dd(7,15,0))))
	theta1_rad = math.atan(-math.cos(math.radians(sun_long_deg))*math.tan(math.radians(PM.obliq(gwdate_day,gwdate_month,gwdate_year))))
	theta2_rad = math.atan(-math.cos(math.radians(long_asc_node_deg-sun_long_deg))*math.tan(math.radians(PM.dms_dd(7,15,0))))
	p_deg = PM.degrees(theta1_rad+theta2_rad)
	rho1_deg = helio_displacement_arcmin/60
	rho_rad = math.asin(2*rho1_deg/PM.sun_dia(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year))-math.radians(rho1_deg)
	b_rad = math.asin(math.sin(b0_rad)*math.cos(rho_rad)+math.cos(b0_rad)*math.sin(rho_rad)*math.cos(math.radians(p_deg-helio_position_angle_deg)))
	b_deg = PM.degrees(b_rad)
	l_deg1 = PM.degrees(math.asin(math.sin(rho_rad)*math.sin(math.radians(p_deg-helio_position_angle_deg))/math.cos(b_rad)))+l0_deg1
	l_deg2 = l_deg1-360*math.floor(l_deg1/360)

	helio_long_deg = round(l_deg2,2)
	helio_lat_deg = round(b_deg,2)

	return helio_long_deg,helio_lat_deg

def carrington_rotation_number(gwdate_day,gwdate_month,gwdate_year):
	"""
	Calculate carrington rotation number for a Greenwich date

	Returns:
			carrington rotation number
	"""
	julian_date_days = PM.cd_jd(gwdate_day,gwdate_month,gwdate_year)
	crn = 1690 + round((julian_date_days-2444235.34)/27.2753,0)

	return crn

def selenographic_coordinates_1(gwdate_day,gwdate_month,gwdate_year):
	"""
	Calculate selenographic (lunar) coordinates (sub-Earth)

	Returns:
		sub-earth longitude
		sub-earth latitude
		position angle of pole
	"""
	julian_date_days = PM.cd_jd(gwdate_day,gwdate_month,gwdate_year)
	t_centuries = (julian_date_days-2451545)/36525
	long_asc_node_deg = 125.044522-1934.136261*t_centuries
	F1 = 93.27191+483202.0175*t_centuries
	F2 = F1-360*math.floor(F1/360)
	geocentric_moon_long_deg = PM.moon_long(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	geocentric_moon_lat_rad = math.radians(PM.moon_lat(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year))
	inclination_rad = math.radians(PM.dms_dd(1,32,32.7))
	node_long_rad = math.radians(long_asc_node_deg-geocentric_moon_long_deg)
	sin_be = -math.cos(inclination_rad)*math.sin(geocentric_moon_lat_rad)+math.sin(inclination_rad)*math.cos(geocentric_moon_lat_rad)*math.sin(node_long_rad)
	sub_earth_lat_deg = PM.degrees(math.asin(sin_be))
	a_rad = math.atan2(-math.sin(geocentric_moon_lat_rad)*math.sin(inclination_rad)-math.cos(geocentric_moon_lat_rad)*math.cos(inclination_rad)*math.sin(node_long_rad),math.cos(geocentric_moon_lat_rad)*math.cos(node_long_rad))
	a_deg = PM.degrees(a_rad)
	sub_earth_long_deg1 = a_deg - F2
	sub_earth_long_deg2 = sub_earth_long_deg1-360*math.floor(sub_earth_long_deg1/360)
	sub_earth_long_deg3 = (sub_earth_long_deg2 - 360) if sub_earth_long_deg2 > 180 else sub_earth_long_deg2
	c1_rad = math.atan(math.cos(node_long_rad)*math.sin(inclination_rad)/(math.cos(geocentric_moon_lat_rad)*math.cos(inclination_rad)+math.sin(geocentric_moon_lat_rad)*math.sin(inclination_rad)*math.sin(node_long_rad)))
	obliquity_rad = math.radians(PM.obliq(gwdate_day,gwdate_month,gwdate_year))
	c2_rad = math.atan(math.sin(obliquity_rad)*math.cos(math.radians(geocentric_moon_long_deg))/(math.sin(obliquity_rad)*math.sin(geocentric_moon_lat_rad)*math.sin(math.radians(geocentric_moon_long_deg))-math.cos(obliquity_rad)*math.cos(geocentric_moon_lat_rad)))
	c_deg = PM.degrees(c1_rad+c2_rad)

	sub_earth_longitude = round(sub_earth_long_deg3,2)
	sub_earth_latitude = round(sub_earth_lat_deg,2)
	position_angle_of_pole = round(c_deg,2)

	return sub_earth_longitude,sub_earth_latitude,position_angle_of_pole

def selenographic_coordinates_2(gwdate_day,gwdate_month,gwdate_year):
	"""
	Calculate selenographic (lunar) coordinates (sub-Solar)

	Returns:
		sub-solar longitude
		sub-solar colongitude
		sub-solar latitude
	"""
	julian_date_days = PM.cd_jd(gwdate_day,gwdate_month,gwdate_year)
	t_centuries = (julian_date_days-2451545)/36525
	long_asc_node_deg = 125.044522-1934.136261*t_centuries
	F1 = 93.27191+483202.0175*t_centuries
	F2 = F1-360*math.floor(F1/360)
	sun_geocentric_long_deg = PM.sun_long(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	moon_equ_hor_parallax_arc_min = PM.moon_hp(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)*60
	sun_earth_dist_au = PM.sun_dist(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	geocentric_moon_lat_rad = math.radians(PM.moon_lat(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year))
	geocentric_moon_long_deg = PM.moon_long(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	adjusted_moon_long_deg = sun_geocentric_long_deg+180+(26.4*math.cos(geocentric_moon_lat_rad)*math.sin(math.radians(sun_geocentric_long_deg-geocentric_moon_long_deg))/(moon_equ_hor_parallax_arc_min*sun_earth_dist_au))
	adjusted_moon_lat_rad = 0.14666*geocentric_moon_lat_rad/(moon_equ_hor_parallax_arc_min*sun_earth_dist_au)
	inclination_rad = math.radians(PM.dms_dd(1,32,32.7))
	node_long_rad = math.radians(long_asc_node_deg-adjusted_moon_long_deg)
	sin_bs = -math.cos(inclination_rad)*math.sin(adjusted_moon_lat_rad)+math.sin(inclination_rad)*math.cos(adjusted_moon_lat_rad)*math.sin(node_long_rad)
	sub_solar_lat_deg = PM.degrees(math.asin(sin_bs))
	a_rad = math.atan2(-math.sin(adjusted_moon_lat_rad)*math.sin(inclination_rad)-math.cos(adjusted_moon_lat_rad)*math.cos(inclination_rad)*math.sin(node_long_rad),math.cos(adjusted_moon_lat_rad)*math.cos(node_long_rad))
	a_deg = PM.degrees(a_rad)
	sub_solar_long_deg1 = a_deg - F2
	sub_solar_long_deg2 = sub_solar_long_deg1-360*math.floor(sub_solar_long_deg1/360)
	sub_solar_long_deg3 = sub_solar_long_deg2 - 360 if sub_solar_long_deg2 > 180 else sub_solar_long_deg2
	sub_solar_colong_deg = 90 - sub_solar_long_deg3

	sub_solar_longitude = round(sub_solar_long_deg3,2)
	sub_solar_colongitude = round(sub_solar_colong_deg,2)
	sub_solar_latitude = round(sub_solar_lat_deg,2)

	return sub_solar_longitude,sub_solar_colongitude,sub_solar_latitude

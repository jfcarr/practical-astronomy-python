import math
from . import pa_macro as PM

def approximate_position_of_sun(lct_hours, lct_minutes, lct_seconds, local_day, local_month, local_year, is_daylight_saving, zone_correction):
	"""
	Calculate approximate position of the sun for a local date and time.

	Arguments:
		lct_hours -- Local civil time, in hours.
		lct_minutes -- Local civil time, in minutes.
		lct_seconds -- Local civil time, in seconds.
		local_day -- Local date, day part.
		local_month -- Local date, month part.
		local_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction -- Time zone correction, in hours.

	Returns:
		sun_ra_hour -- Right Ascension of Sun, hour part
		sun_ra_min -- Right Ascension of Sun, minutes part
		sun_ra_sec -- Right Ascension of Sun, seconds part
		sun_dec_deg -- Declination of Sun, degrees part
		sun_dec_min -- Declination of Sun, minutes part
		sun_dec_sec -- Declination of Sun, seconds part
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	greenwich_date_day = PM.lct_gday(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	greenwich_date_month = PM.lct_gmonth(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	greenwich_date_year = PM.lct_gyear(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	ut_hours = PM.lct_ut(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	ut_days = ut_hours / 24
	jd_days = PM.cd_jd(greenwich_date_day,greenwich_date_month,greenwich_date_year) + ut_days
	d_days = jd_days - PM.cd_jd(0,1,2010)
	n_deg = 360 * d_days / 365.242191
	m_deg1 = n_deg + PM.sun_e_long(0,1,2010) - PM.sun_peri(0,1,2010)
	m_deg2 = m_deg1 - 360 * math.floor(m_deg1/360)
	e_c_deg = 360 * PM.sun_ecc(0,1,2010) * math.sin(math.radians(m_deg2)) / math.pi
	l_s_deg1 = n_deg + e_c_deg + PM.sun_e_long(0,1,2010)
	l_s_deg2 = l_s_deg1 - 360 * math.floor(l_s_deg1/360)
	ra_deg = PM.ec_ra(l_s_deg2,0,0,0,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year)
	ra_hours = PM.dd_dh(ra_deg)
	dec_deg = PM.ec_dec(l_s_deg2,0,0,0,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year)

	sun_ra_hour = PM.dh_hour(ra_hours)
	sun_ra_min = PM.dh_min(ra_hours)
	sun_ra_sec = PM.dh_sec(ra_hours)
	sun_dec_deg = PM.dd_deg(dec_deg)
	sun_dec_min = PM.dd_min(dec_deg)
	sun_dec_sec = PM.dd_sec(dec_deg)

	return sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec

def precise_position_of_sun(lct_hours, lct_minutes, lct_seconds, local_day, local_month, local_year, is_daylight_saving, zone_correction):
	"""
	Calculate precise position of the sun for a local date and time.

	Arguments:
		lct_hours -- Local civil time, in hours.
		lct_minutes -- Local civil time, in minutes.
		lct_seconds -- Local civil time, in seconds.
		local_day -- Local date, day part.
		local_month -- Local date, month part.
		local_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction -- Time zone correction, in hours.

	Returns:
		sun_ra_hour -- Right Ascension of Sun, hour part
		sun_ra_min -- Right Ascension of Sun, minutes part
		sun_ra_sec -- Right Ascension of Sun, seconds part
		sun_dec_deg -- Declination of Sun, degrees part
		sun_dec_min -- Declination of Sun, minutes part
		sun_dec_sec -- Declination of Sun, seconds part
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	g_day = PM.lct_gday(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_month = PM.lct_gmonth(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_year = PM.lct_gyear(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	sun_ecliptic_longitude_deg = PM.sun_long(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	ra_deg = PM.ec_ra(sun_ecliptic_longitude_deg,0,0,0,0,0,g_day,g_month,g_year)
	ra_hours = PM.dd_dh(ra_deg)
	dec_deg = PM.ec_dec(sun_ecliptic_longitude_deg,0,0,0,0,0,g_day,g_month,g_year)

	sun_ra_hour = PM.dh_hour(ra_hours)
	sun_ra_min = PM.dh_min(ra_hours)
	sun_ra_sec = PM.dh_sec(ra_hours)
	sun_dec_deg = PM.dd_deg(dec_deg)
	sun_dec_min = PM.dd_min(dec_deg)
	sun_dec_sec = PM.dd_sec(dec_deg)

	return sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec

def sun_distance_and_angular_size(lct_hours, lct_minutes, lct_seconds, local_day, local_month, local_year, is_daylight_saving, zone_correction):
	"""
	Calculate distance to the Sun (in km), and angular size.

	Arguments:
		lct_hours -- Local civil time, in hours.
		lct_minutes -- Local civil time, in minutes.
		lct_seconds -- Local civil time, in seconds.
		local_day -- Local date, day part.
		local_month -- Local date, month part.
		local_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction -- Time zone correction, in hours.

	Returns:
		sun_dist_km -- Sun's distance, in kilometers
		sun_ang_size_deg -- Sun's angular size (degrees part)
		sun_ang_size_min -- Sun's angular size (minutes part)
		sun_ang_size_sec -- Sun's angular size (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	g_day = PM.lct_gday(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_month = PM.lct_gmonth(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_year = PM.lct_gyear(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	true_anomaly_deg = PM.sun_true_anomaly(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	true_anomaly_rad = math.radians(true_anomaly_deg)
	eccentricity = PM.sun_ecc(g_day,g_month,g_year)
	f = (1 + eccentricity * math.cos(true_anomaly_rad)) / (1 - eccentricity * eccentricity)
	r_km = 149598500 / f
	theta_deg = f * 0.533128

	sun_dist_km = round(r_km,-2)
	sun_ang_size_deg = PM.dd_deg(theta_deg)
	sun_ang_size_min = PM.dd_min(theta_deg)
	sun_ang_size_sec = PM.dd_sec(theta_deg)

	return sun_dist_km,sun_ang_size_deg,sun_ang_size_min,sun_ang_size_sec

def sunrise_and_sunset(local_day, local_month, local_year, is_daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg):
	"""
	Calculate local sunrise and sunset.

	Arguments:
		local_day -- Local date, day part.
		local_month -- Local date, month part.
		local_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction -- Time zone correction, in hours.
		geographical_long_deg -- Geographical longitude, in degrees.
		geographical_lat_deg -- Geographical latitude, in degrees.

	Returns:
		local_sunrise_hour -- Local sunrise, hour part
		local_sunrise_minute -- Local sunrise, minutes part
		local_sunset_hour -- Local sunset, hour part
		local_sunset_minute -- Local sunset, minutes part
		azimuth_of_sunrise_deg -- Azimuth (horizon direction) of sunrise, in degrees
		azimuth_of_sunset_deg -- Azimuth (horizon direction) of sunset, in degrees
		status -- Calculation status
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	local_sunrise_hours = PM.sunrise_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	local_sunset_hours = PM.sunset_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	sun_rise_set_status = PM.e_sun_rs(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	adjusted_sunrise_hours = local_sunrise_hours + 0.008333
	adjusted_sunset_hours = local_sunset_hours + 0.008333
	azimuth_of_sunrise_deg1 = PM.sunrise_az(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)
	azimuth_of_sunset_deg1 = PM.sunset_az(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	local_sunrise_hour = PM.dh_hour(adjusted_sunrise_hours) if sun_rise_set_status == "OK" else None
	local_sunrise_minute = PM.dh_min(adjusted_sunrise_hours) if sun_rise_set_status == "OK" else None
	local_sunset_hour = PM.dh_hour(adjusted_sunset_hours) if sun_rise_set_status == "OK" else None
	local_sunset_minute = PM.dh_min(adjusted_sunset_hours) if sun_rise_set_status == "OK" else None
	azimuth_of_sunrise_deg = round(azimuth_of_sunrise_deg1,2) if sun_rise_set_status == "OK" else None
	azimuth_of_sunset_deg = round(azimuth_of_sunset_deg1,2) if sun_rise_set_status == "OK" else None
	status = sun_rise_set_status

	return local_sunrise_hour,local_sunrise_minute,local_sunset_hour,local_sunset_minute,azimuth_of_sunrise_deg,azimuth_of_sunset_deg,status

def morning_and_evening_twilight(local_day, local_month, local_year, is_daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type):
	"""
	Calculate times of morning and evening twilight.

	Arguments:
		local_day -- Local date, day part.
		local_month -- Local date, month part.
		local_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction -- Time zone correction, in hours.
		geographical_long_deg -- Geographical longitude, in degrees.
		geographical_lat_deg -- Geographical latitude, in degrees.
		twilight_type -- "C" (civil), "N" (nautical), or "A" (astronomical)

	Returns:
		am_twilight_begins_hour -- Beginning of AM twilight (hour part)
		am_twilight_begins_min -- Beginning of AM twilight (minutes part)
		pm_twilight_ends_hour -- Ending of PM twilight (hour part)
		pm_twilight_ends_min -- Ending of PM twilight (minutes part)
		status -- Calculation status
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	start_of_am_twilight_hours = PM.twilight_am_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type)

	end_of_pm_twilight_hours = PM.twilight_pm_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type)

	twilight_status = PM.e_twilight(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type)

	adjusted_am_start_time = start_of_am_twilight_hours + 0.008333
	adjusted_pm_start_time = end_of_pm_twilight_hours + 0.008333

	am_twilight_begins_hour = PM.dh_hour(adjusted_am_start_time) if twilight_status == "OK" else None
	am_twilight_begins_min = PM.dh_min(adjusted_am_start_time) if twilight_status == "OK" else None
	pm_twilight_ends_hour = PM.dh_hour(adjusted_pm_start_time) if twilight_status == "OK" else None
	pm_twilight_ends_min = PM.dh_min(adjusted_pm_start_time) if twilight_status == "OK" else None
	status = twilight_status

	return am_twilight_begins_hour,am_twilight_begins_min,pm_twilight_ends_hour,pm_twilight_ends_min,status

def equation_of_time(gwdate_day, gwdate_month, gwdate_year):
	"""
	Calculate the equation of time. (The difference between the real Sun time and the mean Sun time.)
	
	Arguments:
		gwdate_day -- Greenwich date (day part)
		gwdate_month -- Greenwich date (month part)
		gwdate_year -- Greenwich date (year part)

	Returns:
		equation_of_time_min -- equation of time (minute part)
		equation_of_time_sec -- equation of time (seconds part)
	"""
	sun_longitude_deg = PM.sun_long(12,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	sun_ra_hours = PM.dd_dh(PM.ec_ra(sun_longitude_deg,0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year))
	equivalent_ut_hours = PM.gst_ut(sun_ra_hours,0,0,gwdate_day,gwdate_month,gwdate_year)
	equation_of_time_hours = equivalent_ut_hours - 12

	equation_of_time_min = PM.dh_min(equation_of_time_hours)
	equation_of_time_sec = PM.dh_sec(equation_of_time_hours)

	return equation_of_time_min,equation_of_time_sec

def solar_elongation(ra_hour, ra_min, ra_sec, dec_deg, dec_min, dec_sec, gwdate_day, gwdate_month, gwdate_year):
	"""
	Calculate solar elongation for a celestial body.

	Solar elongation is the angle between the lines of sight from the Earth to the Sun and from the Earth to the celestial body.

	Arguments:
		ra_hour -- Right Ascension, hour part
		ra_min -- Right Ascension, minutes part
		ra_sec -- Right Ascension, seconds part
		dec_deg -- Declination, degrees part
		dec_min -- Declination, minutes part
		dec_sec -- Declination, seconds part
		gwdate_day -- Greenwich Date, day part
		gwdate_month -- Greenwich Date, month part
		gwdate_year -- Greenwich Date, year part

	Returns:
		solar_elongation_deg -- Solar elongation, in degrees
	"""
	sun_longitude_deg = PM.sun_long(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	sun_ra_hours = PM.dd_dh(PM.ec_ra(sun_longitude_deg,0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year))
	sun_dec_deg = PM.ec_dec(sun_longitude_deg,0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	solar_elongation_deg = PM.angle(sun_ra_hours,0,0,sun_dec_deg,0,0,ra_hour,ra_min,ra_sec,dec_deg,dec_min,dec_sec,"H")

	return round(solar_elongation_deg,2)
	
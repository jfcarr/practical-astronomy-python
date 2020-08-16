import math
from . import pa_macro as PM

def approximate_position_of_moon(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year):
	"""
	Calculate approximate position of the Moon.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.

	Returns:
		moon_ra_hour -- Right ascension of Moon (hour part)
		moon_ra_min -- Right ascension of Moon (minutes part)
		moon_ra_sec -- Right ascension of Moon (seconds part)
		moon_dec_deg -- Declination of Moon (degrees part)
		moon_dec_min -- Declination of Moon (minutes part)
		moon_dec_sec -- Declination of Moon (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	l0 = 91.9293359879052
	p0 = 130.143076320618
	n0 = 291.682546643194
	i = 5.145396

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	ut_hours = PM.lct_ut(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	d_days = PM.cd_jd(gdate_day,gdate_month,gdate_year)-PM.cd_jd(0,1,2010)+ut_hours/24
	sun_long_deg = PM.sun_long(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	sun_mean_anomaly_rad = PM.sun_mean_anomaly(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	lm_deg = PM.unwind_deg(13.1763966*d_days+l0)
	mm_deg = PM.unwind_deg(lm_deg-0.1114041*d_days-p0)
	n_deg = PM.unwind_deg(n0-(0.0529539*d_days))
	ev_deg = 1.2739*math.sin(math.radians(2*(lm_deg-sun_long_deg)-mm_deg))
	ae_deg = 0.1858*math.sin(sun_mean_anomaly_rad)
	a3_deg = 0.37*math.sin(sun_mean_anomaly_rad)
	mmd_deg = mm_deg+ev_deg-ae_deg-a3_deg
	ec_deg = 6.2886*math.sin(math.radians(mmd_deg))
	a4_deg = 0.214*math.sin(2*math.radians(mmd_deg))
	ld_deg = lm_deg+ev_deg+ec_deg-ae_deg+a4_deg
	v_deg = 0.6583*math.sin(2*math.radians(ld_deg-sun_long_deg))
	ldd_deg = ld_deg + v_deg
	nd_deg = n_deg-0.16*math.sin(sun_mean_anomaly_rad)
	y = math.sin(math.radians(ldd_deg-nd_deg))*math.cos(math.radians(i))
	x = math.cos(math.radians(ldd_deg-nd_deg))

	moon_long_deg = PM.unwind_deg(PM.degrees(math.atan2(y,x))+nd_deg)
	moon_lat_deg = PM.degrees(math.asin(math.sin(math.radians(ldd_deg-nd_deg))*math.sin(math.radians(i))))
	moon_ra_hours1 = PM.dd_dh(PM.ec_ra(moon_long_deg,0,0,moon_lat_deg,0,0,gdate_day,gdate_month,gdate_year))
	moon_dec_deg1 = PM.ec_dec(moon_long_deg,0,0,moon_lat_deg,0,0,gdate_day,gdate_month,gdate_year)

	moon_ra_hour = PM.dh_hour(moon_ra_hours1)
	moon_ra_min = PM.dh_min(moon_ra_hours1)
	moon_ra_sec = PM.dh_sec(moon_ra_hours1)
	moon_dec_deg = PM.dd_deg(moon_dec_deg1)
	moon_dec_min = PM.dd_min(moon_dec_deg1)
	moon_dec_sec = PM.dd_sec(moon_dec_deg1)

	return moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec

def precise_position_of_moon(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year):
	"""
	Calculate approximate position of the Moon.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.

	Returns:
		moon_ra_hour -- Right ascension of Moon (hour part)
		moon_ra_min -- Right ascension of Moon (minutes part)
		moon_ra_sec -- Right ascension of Moon (seconds part)
		moon_dec_deg -- Declination of Moon (degrees part)
		moon_dec_min -- Declination of Moon (minutes part)
		moon_dec_sec -- Declination of Moon (seconds part)
		earth_moon_dist_km -- Distance from Earth to Moon (km)
		moon_hor_parallax_deg -- Horizontal parallax of Moon (degrees)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	ut_hours = PM.lct_ut(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	moon_ecliptic_longitude_deg, moon_ecliptic_latitude_deg, moon_horizontal_parallax_deg = PM.moon_long_lat_hp(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	nutation_in_longitude_deg = PM.nutat_long(gdate_day,gdate_month,gdate_year)
	corrected_long_deg = moon_ecliptic_longitude_deg + nutation_in_longitude_deg
	earth_moon_distance_km = 6378.14/math.sin(math.radians(moon_horizontal_parallax_deg))
	moon_ra_hours_1 = PM.dd_dh(PM.ec_ra(corrected_long_deg,0,0,moon_ecliptic_latitude_deg,0,0,gdate_day,gdate_month,gdate_year))
	moon_dec_deg1 = PM.ec_dec(corrected_long_deg,0,0,moon_ecliptic_latitude_deg,0,0,gdate_day,gdate_month,gdate_year)

	moon_ra_hour = PM.dh_hour(moon_ra_hours_1)
	moon_ra_min = PM.dh_min(moon_ra_hours_1)
	moon_ra_sec = PM.dh_sec(moon_ra_hours_1)
	moon_dec_deg = PM.dd_deg(moon_dec_deg1)
	moon_dec_min = PM.dd_min(moon_dec_deg1)
	moon_dec_sec = PM.dd_sec(moon_dec_deg1)
	earth_moon_dist_km = round(earth_moon_distance_km,0)
	moon_hor_parallax_deg = round(moon_horizontal_parallax_deg,6)

	return moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec, earth_moon_dist_km, moon_hor_parallax_deg

def moon_phase(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, accuracy_level = "A"):
	"""
	Calculate Moon phase and position angle of bright limb.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		accuracy_level -- "A" (approximate) or "P" (precise)

	Returns:
		moon_phase -- Phase of Moon, between 0 and 1, where 0 is New and 1 is Full.
		pa_bright_limb_deg -- Position angle of the bright limb (degrees)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	sun_long_deg = PM.sun_long(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	moon_ecliptic_longitude_deg, moon_ecliptic_latitude_deg, moon_horizontal_parallax_deg = PM.moon_long_lat_hp(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	d_rad = math.radians(moon_ecliptic_longitude_deg - sun_long_deg)

	moon_phase1 = PM.moon_phase(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year) if accuracy_level == "P" else (1-math.cos(d_rad))/2

	sun_ra_rad = math.radians(PM.ec_ra(sun_long_deg,0,0,0,0,0,gdate_day,gdate_month,gdate_year))
	moon_ra_rad = math.radians(PM.ec_ra(moon_ecliptic_longitude_deg,0,0,moon_ecliptic_latitude_deg,0,0,gdate_day,gdate_month,gdate_year))
	sun_dec_rad = math.radians(PM.ec_dec(sun_long_deg,0,0,0,0,0,gdate_day,gdate_month,gdate_year))
	moon_dec_rad = math.radians(PM.ec_dec(moon_ecliptic_longitude_deg,0,0,moon_ecliptic_latitude_deg,0,0,gdate_day,gdate_month,gdate_year))

	y = math.cos(sun_dec_rad)*math.sin(sun_ra_rad-moon_ra_rad)
	x = math.cos(moon_dec_rad)*math.sin(sun_dec_rad)-math.sin(moon_dec_rad)*math.cos(sun_dec_rad)*math.cos(sun_ra_rad-moon_ra_rad)

	chi_deg = PM.degrees(math.atan2(y,x))

	moon_phase = round(moon_phase1,2)
	pa_bright_limb_deg = round(chi_deg,2)

	return moon_phase, pa_bright_limb_deg

def times_of_new_moon_and_full_moon(is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year):
	"""
	Calculate new moon and full moon instances.

	Arguments:
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.

	Returns:
		nm_local_time_hour -- new Moon instant - local time (hour)
		nm_local_time_min -- new Moon instant - local time (minutes)
		nm_local_date_day -- new Moon instance - local date (day)
		nm_local_date_month -- new Moon instance - local date (month)
		nm_local_date_year -- new Moon instance - local date (year)
		fm_local_time_hour -- full Moon instant - local time (hour)
		fm_local_time_min -- full Moon instant - local time (minutes)
		fm_local_date_day -- full Moon instance - local date (day)
		fm_local_date_month -- full Moon instance - local date (month)
		fm_local_date_year -- full Moon instance - local date (year)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	jd_of_new_moon_days = PM.new_moon(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	jd_of_full_moon_days = PM.full_moon(3,zone_correction_hours,local_date_day,local_date_month,local_date_year)

	g_date_of_new_moon_day = PM.jdc_day(jd_of_new_moon_days)
	integer_day1 = math.floor(g_date_of_new_moon_day)
	g_date_of_new_moon_month = PM.jdc_month(jd_of_new_moon_days)
	g_date_of_new_moon_year = PM.jdc_year(jd_of_new_moon_days)

	g_date_of_full_moon_day = PM.jdc_day(jd_of_full_moon_days)
	integer_day2 = math.floor(g_date_of_full_moon_day)
	g_date_of_full_moon_month = PM.jdc_month(jd_of_full_moon_days)
	g_date_of_full_moon_year = PM.jdc_year(jd_of_full_moon_days)

	ut_of_new_moon_hours = 24*(g_date_of_new_moon_day-integer_day1)
	ut_of_full_moon_hours = 24*(g_date_of_full_moon_day-integer_day2)
	lct_of_new_moon_hours = PM.ut_lct(ut_of_new_moon_hours+0.008333,0,0,daylight_saving,zone_correction_hours,integer_day1,g_date_of_new_moon_month,g_date_of_new_moon_year)
	lct_of_full_moon_hours = PM.ut_lct(ut_of_full_moon_hours+0.008333,0,0,daylight_saving,zone_correction_hours,integer_day2,g_date_of_full_moon_month,g_date_of_full_moon_year)

	nm_local_time_hour = PM.dh_hour(lct_of_new_moon_hours)
	nm_local_time_min = PM.dh_min(lct_of_new_moon_hours)
	nm_local_date_day = PM.ut_lc_day(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day1,g_date_of_new_moon_month,g_date_of_new_moon_year)
	nm_local_date_month = PM.ut_lc_month(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day1,g_date_of_new_moon_month,g_date_of_new_moon_year)
	nm_local_date_year = PM.ut_lc_year(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day1,g_date_of_new_moon_month,g_date_of_new_moon_year)
	fm_local_time_hour = PM.dh_hour(lct_of_full_moon_hours)
	fm_local_time_min = PM.dh_min(lct_of_full_moon_hours)
	fm_local_date_day = PM.ut_lc_day(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day2,g_date_of_full_moon_month,g_date_of_full_moon_year)
	fm_local_date_month = PM.ut_lc_month(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day2,g_date_of_full_moon_month,g_date_of_full_moon_year)
	fm_local_date_year = PM.ut_lc_year(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day2,g_date_of_full_moon_month,g_date_of_full_moon_year)

	return nm_local_time_hour, nm_local_time_min, nm_local_date_day, nm_local_date_month, nm_local_date_year, fm_local_time_hour, fm_local_time_min, fm_local_date_day, fm_local_date_month, fm_local_date_year

def moon_dist_ang_diam_hor_parallax(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year):
	"""
	Calculate Moon's distance, angular diameter, and horizontal parallax.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.

	Returns:
		earth_moon_dist -- Earth-Moon distance (km)
		ang_diameter_deg -- Angular diameter (degrees part)
		ang_diameter_min -- Angular diameter (minutes part)
		hor_parallax_deg -- Horizontal parallax (degrees part)
		hor_parallax_min -- Horizontal parallax (minutes part)
		hor_parallax_sec -- Horizontal parallax (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	moon_distance = PM.moon_dist(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	moon_angular_diameter = PM.moon_size(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	moon_horizontal_parallax = PM.moon_hp(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	earth_moon_dist = round(moon_distance,-1)
	ang_diameter_deg = PM.dd_deg(moon_angular_diameter+0.008333)
	ang_diameter_min = PM.dd_min(moon_angular_diameter+0.008333)
	hor_parallax_deg = PM.dd_deg(moon_horizontal_parallax)
	hor_parallax_min = PM.dd_min(moon_horizontal_parallax)
	hor_parallax_sec = PM.dd_sec(moon_horizontal_parallax)

	return earth_moon_dist, ang_diameter_deg, ang_diameter_min, hor_parallax_deg, hor_parallax_min, hor_parallax_sec

def moonrise_and_moonset(local_date_day, local_date_month, local_date_year, is_daylight_saving, zone_correction_hours, geog_long_deg, geog_lat_deg):
	"""
	Calculate date/time of local moonrise and moonset.

	Arguments:
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		geog_long_deg -- Geographical longitude, in degrees.
		geog_lat_deg -- Geographical latitude, in degrees.

	Returns:
		mr_lt_hour -- Moonrise, local time (hour part)
		mr_lt_min -- Moonrise, local time (minutes part)
		mr_local_date_day -- Moonrise, local date (day)
		mr_local_date_month -- Moonrise, local date (month)
		mr_local_date_year -- Moonrise, local date (year)
		mr_azimuth_deg -- Moonrise, azimuth (degrees)
		ms_lt_hour -- Moonset, local time (hour part)
		ms_lt_min -- Moonset, local time (minutes part)
		ms_local_date_day -- Moonset, local date (day)
		ms_local_date_month -- Moonset, local date (month)
		ms_local_date_year -- Moonset, local date (year)
		ms_azimuth_deg -- Moonset, azimuth (degrees)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	local_time_of_moonrise_hours = PM.moon_rise_lct(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)
	local_moonrise_status1 = PM.e_moon_rise(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)
	local_date_of_moonrise_day,local_date_of_moonrise_month,local_date_of_moonrise_year = PM.moon_rise_lc_dmy(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)
	local_azimuth_deg1 = PM.moon_rise_az(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)

	local_time_of_moonset_hours = PM.moon_set_lct(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)
	local_moonset_status1 = PM.e_moon_set(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)
	local_date_of_moonset_day,local_date_of_moonset_month,local_date_of_moonset_year = PM.moon_set_lc_dmy(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)
	local_azimuth_deg2 = PM.moon_set_az(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_long_deg,geog_lat_deg)

	mr_lt_hour = PM.dh_hour(local_time_of_moonrise_hours + 0.008333)
	mr_lt_min = PM.dh_min(local_time_of_moonrise_hours + 0.008333)
	mr_local_date_day = local_date_of_moonrise_day
	mr_local_date_month = local_date_of_moonrise_month
	mr_local_date_year = local_date_of_moonrise_year
	mr_azimuth_deg = round(local_azimuth_deg1,2)
	ms_lt_hour = PM.dh_hour(local_time_of_moonset_hours + 0.008333)
	ms_lt_min = PM.dh_min(local_time_of_moonset_hours + 0.008333)
	ms_local_date_day = local_date_of_moonset_day
	ms_local_date_month = local_date_of_moonset_month
	ms_local_date_year = local_date_of_moonset_year
	ms_azimuth_deg = round(local_azimuth_deg2,2)

	return mr_lt_hour, mr_lt_min, mr_local_date_day, mr_local_date_month, mr_local_date_year, mr_azimuth_deg, ms_lt_hour, ms_lt_min, ms_local_date_day, ms_local_date_month, ms_local_date_year, ms_azimuth_deg
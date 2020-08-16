import math
from . import pa_macro as PM
from . import pa_planet_data as PPD

def approximate_position_of_planet(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, planet_name):
	"""
	Calculate approximate position of a planet.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		planet_name -- Name of planet, e.g., "Jupiter"

	Returns:
		planet_ra_hour -- Right ascension of planet (hour part)
		planet_ra_min -- Right ascension of planet (minutes part)
		planet_ra_sec -- Right ascension of planet (seconds part)
		planet_dec_deg -- Declination of planet (degrees part)
		planet_dec_min -- Declination of planet (minutes part)
		planet_dec_sec -- Declination of planet (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	planet_tp_from_table = PPD.get_planet_data(planet_name)['Tp']
	planet_long_from_table = PPD.get_planet_data(planet_name)['Long']
	planet_peri_from_table = PPD.get_planet_data(planet_name)['Peri']
	planet_ecc_from_table = PPD.get_planet_data(planet_name)['Ecc']
	planet_axis_from_table = PPD.get_planet_data(planet_name)['Axis']
	planet_incl_from_table = PPD.get_planet_data(planet_name)['Incl']
	planet_node_from_table = PPD.get_planet_data(planet_name)['Node']

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	ut_hours = PM.lct_ut(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	d_days = PM.cd_jd(gdate_day+(ut_hours/24),gdate_month,gdate_year) - PM.cd_jd(0,1,2010)
	np_deg1 = 360 * d_days / (365.242191 * planet_tp_from_table)
	np_deg2 = np_deg1 - 360 * math.floor(np_deg1/360)
	mp_deg = np_deg2 + planet_long_from_table - planet_peri_from_table
	lp_deg1 = np_deg2 + (360 * planet_ecc_from_table * math.sin(math.radians(mp_deg)) / math.pi) + planet_long_from_table
	lp_deg2 = lp_deg1 - 360 * math.floor(lp_deg1/360)
	planet_true_anomaly_deg = lp_deg2 - planet_peri_from_table
	r_au = planet_axis_from_table * (1 - (planet_ecc_from_table)**2) / (1 + planet_ecc_from_table * math.cos(math.radians(planet_true_anomaly_deg)))

	earth_tp_from_table = PPD.get_planet_data("Earth")['Tp']
	earth_long_from_table = PPD.get_planet_data("Earth")['Long']
	earth_peri_from_table = PPD.get_planet_data("Earth")['Peri']
	earth_ecc_from_table = PPD.get_planet_data("Earth")['Ecc']
	earth_axis_from_table = PPD.get_planet_data("Earth")['Axis']
	
	ne_deg1 = 360*d_days/(365.242191*earth_tp_from_table)
	ne_deg2 = ne_deg1-360*math.floor(ne_deg1/360)
	me_deg = ne_deg2+earth_long_from_table-earth_peri_from_table
	le_deg1 = ne_deg2+earth_long_from_table+360*earth_ecc_from_table*math.sin(math.radians(me_deg))/math.pi
	le_deg2 = le_deg1-360*math.floor(le_deg1/360)
	earth_true_anomaly_deg = le_deg2-earth_peri_from_table
	r_au2 = earth_axis_from_table*(1-(earth_ecc_from_table)**2)/(1+earth_ecc_from_table*math.cos(math.radians(earth_true_anomaly_deg)))
	lp_node_rad = math.radians(lp_deg2-planet_node_from_table)
	psi_rad = math.asin(math.sin(lp_node_rad)*math.sin(math.radians(planet_incl_from_table)))
	y = math.sin(lp_node_rad)*math.cos(math.radians(planet_incl_from_table))
	x = math.cos(lp_node_rad)
	ld_deg = PM.degrees(math.atan2(y,x))+planet_node_from_table
	rd_au = r_au*math.cos(psi_rad)
	le_ld_rad = math.radians(le_deg2-ld_deg)
	atan2_type_1 = math.atan2(rd_au*math.sin(le_ld_rad),r_au2-rd_au*math.cos(le_ld_rad))
	atan2_type_2 = math.atan2(r_au2*math.sin(-le_ld_rad),rd_au-r_au2*math.cos(le_ld_rad))
	a_rad = atan2_type_1 if rd_au < 1 else atan2_type_2 
	lamda_deg1 =  180 + le_deg2 + PM.degrees(a_rad) if rd_au < 1 else PM.degrees(a_rad) + ld_deg
	lamda_deg2 = lamda_deg1-360*math.floor(lamda_deg1/360)
	beta_deg = PM.degrees(math.atan(rd_au*math.tan(psi_rad)*math.sin(math.radians(lamda_deg2-ld_deg))/(r_au2*math.sin(-le_ld_rad))))
	ra_hours = PM.dd_dh(PM.ec_ra(lamda_deg2,0,0,beta_deg,0,0,gdate_day,gdate_month,gdate_year))
	dec_deg = PM.ec_dec(lamda_deg2,0,0,beta_deg,0,0,gdate_day,gdate_month,gdate_year)

	planet_ra_hour = PM.dh_hour(ra_hours)
	planet_ra_min = PM.dh_min(ra_hours)
	planet_ra_sec = PM.dh_sec(ra_hours)
	planet_dec_deg = PM.dd_deg(dec_deg)
	planet_dec_min = PM.dd_min(dec_deg)
	planet_dec_sec = PM.dd_sec(dec_deg)

	return planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec

def precise_position_of_planet(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, planet_name):
	"""
	Calculate precise position of a planet.

	Arguments:
		lct_hour -- Local civil time, hour part.
		lct_min -- Local civil time, minutes part.
		lct_sec -- Local civil time, seconds part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		planet_name -- Name of planet, e.g., "Jupiter"

	Returns:
		planet_ra_hour -- Right ascension of planet (hour part)
		planet_ra_min -- Right ascension of planet (minutes part)
		planet_ra_sec -- Right ascension of planet (seconds part)
		planet_dec_deg -- Declination of planet (degrees part)
		planet_dec_min -- Declination of planet (minutes part)
		planet_dec_sec -- Declination of planet (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	planet_ecl_long_deg,planet_ecl_lat_deg,planet_distance_au,planet_h_long1,planet_h_long2,planet_h_lat,planet_r_vect = PM.planet_coordinates(lct_hour,lct_min,lct_sec,daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year,planet_name)

	planet_ra_hours = PM.dd_dh(PM.ec_ra(planet_ecl_long_deg,0,0,planet_ecl_lat_deg,0,0,local_date_day,local_date_month,local_date_year))
	planet_dec_deg1 = PM.ec_dec(planet_ecl_long_deg,0,0,planet_ecl_lat_deg,0,0,local_date_day,local_date_month,local_date_year)

	planet_ra_hour = PM.dh_hour(planet_ra_hours)
	planet_ra_min = PM.dh_min(planet_ra_hours)
	planet_ra_sec = PM.dh_sec(planet_ra_hours)
	planet_dec_deg = PM.dd_deg(planet_dec_deg1)
	planet_dec_min = PM.dd_min(planet_dec_deg1)
	planet_dec_sec = PM.dd_sec(planet_dec_deg1)

	return planet_ra_hour,planet_ra_min,planet_ra_sec,planet_dec_deg,planet_dec_min,planet_dec_sec

def visual_aspects_of_a_planet(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, planet_name):
	"""
	Calculate several visual aspects of a planet.

	Arguments:
		lct_hour -- Local civil time, hour part.
		lct_min -- Local civil time, minutes part.
		lct_sec -- Local civil time, seconds part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		planet_name -- Name of planet, e.g., "Jupiter"

	Returns:
		distance_au -- Planet's distance from Earth, in AU.
		ang_dia_arcsec -- Angular diameter of the planet.
		phase -- Illuminated fraction of the planet.
		light_time_hour -- Light travel time from planet to Earth, hour part.
		light_time_minutes -- Light travel time from planet to Earth, minutes part.
		light_time_seconds -- Light travel time from planet to Earth, seconds part.
		pos_angle_bright_limb_deg -- Position-angle of the bright limb.
		approximate_magnitude -- Apparent brightness of the planet.
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	greenwich_date_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	greenwich_date_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	greenwich_date_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	planet_ecl_long_deg,planet_ecl_lat_deg,planet_dist_au,planet_h_long1,temp3,temp4,planet_r_vect = PM.planet_coordinates(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, planet_name)

	planet_ra_rad = math.radians(PM.ec_ra(planet_ecl_long_deg,0,0,planet_ecl_lat_deg,0,0,local_date_day,local_date_month,local_date_year))
	planet_dec_rad = math.radians(PM.ec_dec(planet_ecl_long_deg,0,0,planet_ecl_lat_deg,0,0,local_date_day,local_date_month,local_date_year))

	light_travel_time_hours = planet_dist_au*0.1386
	angular_diameter_arcsec = PPD.get_planet_data(planet_name)['Theta0'] / planet_dist_au
	phase1 = 0.5*(1+math.cos(math.radians(planet_ecl_long_deg-planet_h_long1)))

	sun_ecl_long_deg = PM.sun_long(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	sun_ra_rad = math.radians(PM.ec_ra(sun_ecl_long_deg,0,0,0,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year))
	sun_dec_rad = math.radians(PM.ec_dec(sun_ecl_long_deg,0,0,0,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year))

	y = math.cos(sun_dec_rad) * math.sin(sun_ra_rad-planet_ra_rad)
	x = math.cos(planet_dec_rad) * math.sin(sun_dec_rad) - math.sin(planet_dec_rad) * math.cos(sun_dec_rad) * math.cos(sun_ra_rad-planet_ra_rad)

	chi_deg = PM.degrees(math.atan2(y,x))
	radius_vector_au = planet_r_vect
	approximate_magnitude1 = 5 * math.log10(radius_vector_au*planet_dist_au/math.sqrt(phase1)) + PPD.get_planet_data(planet_name)['V0']

	distance_au = round(planet_dist_au,5)
	ang_dia_arcsec = round(angular_diameter_arcsec,1)
	phase = round(phase1,2)
	light_time_hour = PM.dh_hour(light_travel_time_hours)
	light_time_minutes = PM.dh_min(light_travel_time_hours)
	light_time_seconds = PM.dh_sec(light_travel_time_hours)
	pos_angle_bright_limb_deg = round(chi_deg,1)
	approximate_magnitude = round(approximate_magnitude1,1)

	return distance_au, ang_dia_arcsec, phase, light_time_hour, light_time_minutes, light_time_seconds, pos_angle_bright_limb_deg, approximate_magnitude

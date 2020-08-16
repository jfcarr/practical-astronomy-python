import math
from . import pa_macro as PM
from . import pa_comet_data as PCD

def position_of_elliptical_comet(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, comet_name):
	"""
	Calculate position of an elliptical comet.

	Arguments:
		lct_hour -- Local civil time, hour part.
		lct_min -- Local civil time, minutes part.
		lct_sec -- Local civil time, seconds part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		comet_name -- Name of comet, e.g., "Halley"

	Returns:
		comet_ra_hour -- Right ascension of comet (hour part)
		comet_ra_min -- Right ascension of comet (minutes part)
		comet_dec_deg -- Declination of comet (degrees part)
		comet_dec_min -- Declination of comet (minutes part)
		comet_dist_earth -- Comet's distance from Earth (AU)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	greenwich_date_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	greenwich_date_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	greenwich_date_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	time_since_epoch_years = (PM.cd_jd(greenwich_date_day,greenwich_date_month,greenwich_date_year)-PM.cd_jd(0,1,greenwich_date_year))/365.242191+greenwich_date_year-PCD.get_comet_data_elliptical("Halley")['Epoch']
	mc_deg = 360*time_since_epoch_years/PCD.get_comet_data_elliptical("Halley")['Period']
	mc_rad = math.radians(mc_deg-360*math.floor(mc_deg/360))
	eccentricity = PCD.get_comet_data_elliptical("Halley")['Ecc']
	true_anomaly_deg = PM.degrees(PM.true_anomaly(mc_rad,eccentricity))
	lc_deg = true_anomaly_deg + PCD.get_comet_data_elliptical("Halley")['Peri']
	r_au = PCD.get_comet_data_elliptical("Halley")['Axis'] * (1-eccentricity*eccentricity)/(1+eccentricity*math.cos(math.radians(true_anomaly_deg)))
	lc_node_rad = math.radians(lc_deg - PCD.get_comet_data_elliptical("Halley")['Node'])
	psi_rad = math.asin(math.sin(lc_node_rad)*math.sin(math.radians(PCD.get_comet_data_elliptical("Halley")['Incl'])))

	y = math.sin(lc_node_rad)*math.cos(math.radians(PCD.get_comet_data_elliptical("Halley")['Incl']))
	x = math.cos(lc_node_rad)

	ld_deg = PM.degrees(math.atan2(y,x)) + PCD.get_comet_data_elliptical("Halley")['Node']
	rd_au = r_au * math.cos(psi_rad)

	earth_longitude_le_deg = PM.sun_long(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year) + 180
	earth_radius_vector_au = PM.sun_dist(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	le_ld_rad = math.radians(earth_longitude_le_deg - ld_deg)
	a_rad = math.atan2(rd_au*math.sin(le_ld_rad),earth_radius_vector_au-rd_au*math.cos(le_ld_rad)) if rd_au < earth_radius_vector_au else math.atan2(earth_radius_vector_au*math.sin(-le_ld_rad),rd_au-earth_radius_vector_au*math.cos(le_ld_rad))

	comet_long_deg1 = 180 + earth_longitude_le_deg + PM.degrees(a_rad) if rd_au < earth_radius_vector_au else PM.degrees(a_rad) + ld_deg
	comet_long_deg = comet_long_deg1 - 360 * math.floor(comet_long_deg1/360)
	comet_lat_deg = PM.degrees(math.atan((rd_au*math.tan(psi_rad)*math.sin(math.radians(comet_long_deg1-ld_deg))/(earth_radius_vector_au*math.sin(-le_ld_rad)))))
	comet_ra_hours1 = PM.dd_dh(PM.ec_ra(comet_long_deg,0,0,comet_lat_deg,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year))
	comet_dec_deg1 = PM.ec_dec(comet_long_deg,0,0,comet_lat_deg,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year)
	comet_distance_au = math.sqrt(earth_radius_vector_au**2+r_au**2-2*earth_radius_vector_au*r_au*math.cos(math.radians(lc_deg-earth_longitude_le_deg))*math.cos(psi_rad))

	comet_ra_hour = PM.dh_hour(comet_ra_hours1+0.008333)
	comet_ra_min = PM.dh_min(comet_ra_hours1+0.008333)
	comet_dec_deg = PM.dd_deg(comet_dec_deg1+0.008333)
	comet_dec_min = PM.dd_min(comet_dec_deg1+0.008333)
	comet_dist_earth = round(comet_distance_au,2)

	return comet_ra_hour, comet_ra_min, comet_dec_deg, comet_dec_min, comet_dist_earth

def position_of_parabolic_comet(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, comet_name):
	"""
	Calculate position of a parabolic comet.

	Arguments:
		lct_hour -- Local civil time, hour part.
		lct_min -- Local civil time, minutes part.
		lct_sec -- Local civil time, seconds part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		comet_name -- Name of comet, e.g., "Kohler"

	Returns:
		comet_ra_hour -- Right ascension of comet (hour part)
		comet_ra_min -- Right ascension of comet (minutes part)
		comet_ra_sec -- Right ascension of comet (seconds part)
		comet_dec_deg -- Declination of comet (degrees part)
		comet_dec_min -- Declination of comet (minutes part)
		comet_dec_sec -- Declination of comet (seconds part)
		comet_dist_earth -- Comet's distance from Earth (AU)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	greenwich_date_day = PM.lct_gday(lct_hour,lct_min,lct_sec,daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	greenwich_date_month = PM.lct_gmonth(lct_hour,lct_min,lct_sec,daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	greenwich_date_year = PM.lct_gyear(lct_hour,lct_min,lct_sec,daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)

	ut_hours = PM.lct_ut(lct_hour,lct_min,lct_sec,daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)

	perihelion_epoch_day = PCD.get_comet_data_parabolic(comet_name)["EpochPeriDay"]
	perihelion_epoch_month = PCD.get_comet_data_parabolic(comet_name)["EpochPeriMonth"]
	perihelion_epoch_year = PCD.get_comet_data_parabolic(comet_name)["EpochPeriYear"]
	q_au = PCD.get_comet_data_parabolic(comet_name)["PeriDist"]
	inclination_deg = PCD.get_comet_data_parabolic(comet_name)["Incl"]
	perihelion_deg = PCD.get_comet_data_parabolic(comet_name)["ArgPeri"]
	node_deg = PCD.get_comet_data_parabolic(comet_name)["Node"]

	comet_long_deg, comet_lat_deg, comet_dist_au = PM.p_comet_long_lat_dist(lct_hour,lct_min,lct_sec,daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year,perihelion_epoch_day,perihelion_epoch_month,perihelion_epoch_year,q_au,inclination_deg,perihelion_deg,node_deg)

	comet_ra_hours = PM.dd_dh(PM.ec_ra(comet_long_deg,0,0,comet_lat_deg,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year))
	comet_dec_deg1 = PM.ec_dec(comet_long_deg,0,0,comet_lat_deg,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year)

	comet_ra_hour = PM.dh_hour(comet_ra_hours)
	comet_ra_min = PM.dh_min(comet_ra_hours)
	comet_ra_sec = PM.dh_sec(comet_ra_hours)
	comet_dec_deg = PM.dd_deg(comet_dec_deg1)
	comet_dec_min = PM.dd_min(comet_dec_deg1)
	comet_dec_sec = PM.dd_sec(comet_dec_deg1)
	comet_dist_earth = round(comet_dist_au,2)

	return comet_ra_hour, comet_ra_min, comet_ra_sec, comet_dec_deg, comet_dec_min, comet_dec_sec, comet_dist_earth
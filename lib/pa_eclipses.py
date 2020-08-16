import math
from . import pa_macro as PM

def lunar_eclipse_occurrence(local_date_day,local_date_month,local_date_year,is_daylight_saving,zone_correction_hours):
	"""
	Determine if a lunar eclipse is likely to occur.

	Arguments:
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.

	Returns:
		status -- One of "Lunar eclipse certain", "Lunar eclipse possible", or "No lunar eclipse".
		event_date_day -- Date of eclipse event (day).
		event_date_month -- Date of eclipse event (month).
		event_date_year -- Date of eclipse event (year).
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	julian_date_of_full_moon = PM.full_moon(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	g_date_of_full_moon_day = PM.jdc_day(julian_date_of_full_moon)
	integer_day = math.floor(g_date_of_full_moon_day)
	g_date_of_full_moon_month = PM.jdc_month(julian_date_of_full_moon)
	g_date_of_full_moon_year = PM.jdc_year(julian_date_of_full_moon)
	ut_of_full_moon_hours = g_date_of_full_moon_day - integer_day
	local_civil_time_hours = PM.ut_lct(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_day = PM.ut_lc_day(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_month = PM.ut_lc_month(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_year = PM.ut_lc_year(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	eclipse_occurrence = PM.lunar_eclipse_occurrence(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)

	status = eclipse_occurrence
	event_date_day = local_civil_date_day
	event_date_month = local_civil_date_month
	event_date_year = local_civil_date_year

	return status,event_date_day,event_date_month,event_date_year

def lunar_eclipse_circumstances(local_date_day,local_date_month,local_date_year,is_daylight_saving,zone_correction_hours):
	"""
	Calculate the circumstances of a lunar eclipse.

	Arguments:
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.

	Returns:
		lunar_eclipse_certain_date_day -- Lunar eclipse date (day)
		lunar_eclipse_certain_date_month -- Lunar eclipse date (month)
		lunar_eclipse_certain_date_year -- Lunar eclipse date (year)
		ut_start_pen_phase_hour -- Start of penumbral phase (hour)
		ut_start_pen_phase_minutes -- Start of penumbral phase (minutes)
		ut_start_umbral_phase_hour -- Start of umbral phase (hour)
		ut_start_umbral_phase_minutes -- Start of umbral phase (minutes)
		ut_start_total_phase_hour -- Start of total phase (hour)
		ut_start_total_phase_minutes -- Start of total phase (minutes)
		ut_mid_eclipse_hour -- Mid-eclipse (hour)
		ut_mid_eclipse_minutes -- Mid-eclipse (minutes)
		ut_end_total_phase_hour -- End of total phase (hour)
		ut_end_total_phase_minutes -- End of total phase (minutes)
		ut_end_umbral_phase_hour -- End of umbral phase (hour)
		ut_end_umbral_phase_minutes -- End of umbral phase (minutes)
		ut_end_pen_phase_hour -- End of penumbral phase (hour)
		ut_end_pen_phase_minutes -- End of penumbral phase (minutes)
		eclipse_magnitude -- Eclipse magnitude
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	julian_date_of_full_moon = PM.full_moon(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	g_date_of_full_moon_day = PM.jdc_day(julian_date_of_full_moon)
	integer_day = math.floor(g_date_of_full_moon_day)
	g_date_of_full_moon_month = PM.jdc_month(julian_date_of_full_moon)
	g_date_of_full_moon_year = PM.jdc_year(julian_date_of_full_moon)
	ut_of_full_moon_hours = g_date_of_full_moon_day - integer_day
	local_civil_time_hours = PM.ut_lct(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_day = PM.ut_lc_day(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_month = PM.ut_lc_month(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_year = PM.ut_lc_year(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	eclipse_occurrence = PM.lunar_eclipse_occurrence(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	ut_max_eclipse = PM.ut_max_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	ut_first_contact = PM.ut_first_contact_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	ut_last_contact = PM.ut_last_contact_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	ut_start_umbral_phase = PM.ut_start_umbra_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	ut_end_umbral_phase = PM.ut_end_umbra_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	ut_start_total_phase = PM.ut_start_total_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	ut_end_total_phase = PM.ut_end_total_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)
	eclipse_magnitude1 = PM.mag_lunar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours)

	lunar_eclipse_certain_date_day = local_civil_date_day
	lunar_eclipse_certain_date_month = local_civil_date_month
	lunar_eclipse_certain_date_year = local_civil_date_year
	ut_start_pen_phase_hour = None if ut_first_contact == -99 else PM.dh_hour(ut_first_contact+0.008333)
	ut_start_pen_phase_minutes = None if ut_first_contact == -99 else PM.dh_min(ut_first_contact+0.008333)
	ut_start_umbral_phase_hour = None if ut_start_umbral_phase == -99 else PM.dh_hour(ut_start_umbral_phase+0.008333)
	ut_start_umbral_phase_minutes = None if ut_start_umbral_phase == -99 else PM.dh_min(ut_start_umbral_phase+0.008333)
	ut_start_total_phase_hour = None if ut_start_total_phase == -99 else PM.dh_hour(ut_start_total_phase+0.008333)
	ut_start_total_phase_minutes = None if ut_start_total_phase == -99 else PM.dh_min(ut_start_total_phase+0.008333)
	ut_mid_eclipse_hour = None if ut_max_eclipse == -99 else PM.dh_hour(ut_max_eclipse+0.008333)
	ut_mid_eclipse_minutes = None if ut_max_eclipse == -99 else PM.dh_min(ut_max_eclipse+0.008333)
	ut_end_total_phase_hour = None if ut_end_total_phase == -99 else PM.dh_hour(ut_end_total_phase+0.008333)
	ut_end_total_phase_minutes = None if ut_end_total_phase == -99 else PM.dh_min(ut_end_total_phase+0.008333)
	ut_end_umbral_phase_hour = None if ut_end_umbral_phase == -99 else PM.dh_hour(ut_end_umbral_phase+0.008333)
	ut_end_umbral_phase_minutes = None if ut_end_umbral_phase == -99 else PM.dh_min(ut_end_umbral_phase+0.008333)
	ut_end_pen_phase_hour = None if ut_last_contact == -99 else PM.dh_hour(ut_last_contact+0.008333)
	ut_end_pen_phase_minutes = None if ut_last_contact == -99 else PM.dh_min(ut_last_contact+0.008333)
	eclipse_magnitude = None if eclipse_magnitude1 == -99 else round(eclipse_magnitude1,2)

	return lunar_eclipse_certain_date_day, lunar_eclipse_certain_date_month, lunar_eclipse_certain_date_year, ut_start_pen_phase_hour, ut_start_pen_phase_minutes, ut_start_umbral_phase_hour, ut_start_umbral_phase_minutes, ut_start_total_phase_hour, ut_start_total_phase_minutes, ut_mid_eclipse_hour, ut_mid_eclipse_minutes, ut_end_total_phase_hour, ut_end_total_phase_minutes, ut_end_umbral_phase_hour, ut_end_umbral_phase_minutes, ut_end_pen_phase_hour, ut_end_pen_phase_minutes, eclipse_magnitude 

def solar_eclipse_occurrence(local_date_day,local_date_month,local_date_year,is_daylight_saving,zone_correction_hours):
	"""
	Determine if a solar eclipse is likely to occur.

	Arguments:
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.

	Returns:
		status -- One of "Solar eclipse certain", "Solar eclipse possible", or "No solar eclipse".
		event_date_day -- Date of eclipse event (day).
		event_date_month -- Date of eclipse event (month).
		event_date_year -- Date of eclipse event (year).
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	julian_date_of_new_moon = PM.new_moon(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	g_date_of_new_moon_day = PM.jdc_day(julian_date_of_new_moon)
	integer_day = math.floor(g_date_of_new_moon_day)
	g_date_of_new_moon_month = PM.jdc_month(julian_date_of_new_moon)
	g_date_of_new_moon_year = PM.jdc_year(julian_date_of_new_moon)
	ut_of_new_moon_hours = g_date_of_new_moon_day - integer_day
	local_civil_time_hours = PM.ut_lct(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	local_civil_date_day = PM.ut_lc_day(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	local_civil_date_month = PM.ut_lc_month(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	local_civil_date_year = PM.ut_lc_year(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	eclipse_occurrence = PM.solar_eclipse_occurrence(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)

	status = eclipse_occurrence
	event_date_day = local_civil_date_day
	event_date_month = local_civil_date_month
	event_date_year = local_civil_date_year

	return status,event_date_day,event_date_month,event_date_year

def solar_eclipse_circumstances(local_date_day,local_date_month,local_date_year,is_daylight_saving,zone_correction_hours, geog_longitude_deg, geog_latitude_deg):
	"""
	Calculate the circumstances of a lunar eclipse.

	Arguments:
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		geog_longitude_deg -- Geographical longitude of observer.
		geog_latitude_deg -- Geographical latitude of observer.

	Returns:
		solar_eclipse_certain_date_day -- Solar eclipse date (day)
		solar_eclipse_certain_date_month -- Solar eclipse date (month)
		solar_eclipse_certain_date_year -- Solar eclipse date (year)
		ut_first_contact_hour -- First contact of shadow (hour)
		ut_first_contact_minutes -- First contact of shadow (minutes)
		ut_mid_eclipse_hour -- Mid-eclipse (hour)
		ut_mid_eclipse_minutes -- Mid-eclipse (minutes)
		ut_last_contact_hour -- Last contact of shadow (hour)
		ut_last_contact_minutes -- Last contact of shadow (minutes)
		eclipse_magnitude -- Eclipse magnitude
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	julian_date_of_new_moon = PM.new_moon(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	g_date_of_new_moon_day = PM.jdc_day(julian_date_of_new_moon)
	integer_day = math.floor(g_date_of_new_moon_day)
	g_date_of_new_moon_month = PM.jdc_month(julian_date_of_new_moon)
	g_date_of_new_moon_year = PM.jdc_year(julian_date_of_new_moon)
	ut_of_new_moon_hours = g_date_of_new_moon_day - integer_day
	local_civil_time_hours = PM.ut_lct(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	local_civil_date_day = PM.ut_lc_day(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	local_civil_date_month = PM.ut_lc_month(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	local_civil_date_year = PM.ut_lc_year(ut_of_new_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_new_moon_month,g_date_of_new_moon_year)
	eclipse_occurrence = PM.solar_eclipse_occurrence(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	ut_max_eclipse = PM.ut_max_solar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_longitude_deg,geog_latitude_deg)
	ut_first_contact = PM.ut_first_contact_solar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_longitude_deg,geog_latitude_deg)
	ut_last_contact = PM.ut_last_contact_solar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_longitude_deg,geog_latitude_deg)
	magnitude = PM.mag_solar_eclipse(local_date_day,local_date_month,local_date_year,daylight_saving,zone_correction_hours,geog_longitude_deg,geog_latitude_deg)

	solar_eclipse_certain_date_day = local_civil_date_day
	solar_eclipse_certain_date_month = local_civil_date_month
	solar_eclipse_certain_date_year = local_civil_date_year
	ut_first_contact_hour = None if ut_first_contact == -99 else PM.dh_hour(ut_first_contact+0.008333)
	ut_first_contact_minutes = None if ut_first_contact == -99 else PM.dh_min(ut_first_contact+0.008333)
	ut_mid_eclipse_hour = None if ut_max_eclipse == -99 else PM.dh_hour(ut_max_eclipse+0.008333)
	ut_mid_eclipse_minutes = None if ut_max_eclipse == -99 else PM.dh_min(ut_max_eclipse+0.008333)
	ut_last_contact_hour = None if ut_last_contact == -99 else PM.dh_hour(ut_last_contact+0.008333)
	ut_last_contact_minutes = None if ut_last_contact == -99 else PM.dh_min(ut_last_contact+0.008333)
	eclipse_magnitude = None if magnitude == -99 else round(magnitude,3)

	return solar_eclipse_certain_date_day, solar_eclipse_certain_date_month, solar_eclipse_certain_date_year, ut_first_contact_hour, ut_first_contact_minutes, ut_mid_eclipse_hour, ut_mid_eclipse_minutes, ut_last_contact_hour, ut_last_contact_minutes, eclipse_magnitude

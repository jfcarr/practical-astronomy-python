import json
from dateutil.parser import parse
import lib.pa_datetime as PA_DT

def doe_year(year):
	'''
	Calculate date of Easter for a given year.
	'''
	easter_month,easter_day,easter_year = PA_DT.get_date_of_easter(year)
	easter_dict = dict(easterMonth=easter_month, easterDay=easter_day, easterYear=easter_year)

	print(json.dumps(easter_dict))

def cd_to_dn(date_string):
	'''
	Convert civil date to day number.
	'''
	dt = parse(date_string)
	day_number = PA_DT.civil_date_to_day_number(dt.month, dt.day, dt.year)
	day_num_dict = dict(dayNumber=day_number)

	print(json.dumps(day_num_dict))

def gd_to_jd(greenwich_date):
	'''
	Convert Greenwich date to Julian date.
	'''
	dt_split = greenwich_date.split("/")

	julian_date = PA_DT.greenwich_date_to_julian_date(float(dt_split[1]), int(dt_split[0]), int(dt_split[2]))
	julian_date_dict = dict(julianDate=julian_date)

	print(json.dumps(julian_date_dict))

def jd_to_gd(julian_date):
	'''
	Convert Julian date to Greenwich date.
	'''
	day,month,year = PA_DT.julian_date_to_greenwich_date(julian_date)
	greenwich_date_dict = dict(greenwichDay=day, greenwichMonth=month, greenwichYear=year)

	print(json.dumps(greenwich_date_dict))

def ct_to_dh(civil_time):
	'''
	Convert civil time to decimal hours.
	'''
	ct_split = civil_time.split(":")

	decimal_hours = PA_DT.civil_time_to_decimal_hours(int(ct_split[0]), int(ct_split[1]), int(ct_split[2]))
	decimal_hours = round(decimal_hours,8)
	decimal_hours_dict = dict(decimalHours=decimal_hours)

	print(json.dumps(decimal_hours_dict))

def dh_to_ct(decimal_hours):
	'''
	Convert decimal hours to civil time.
	'''
	hours,minutes,seconds = PA_DT.decimal_hours_to_civil_time(decimal_hours)
	civil_time_dict = dict(civilTimeHours=hours, civilTimeMinutes=minutes, civilTimeSeconds=seconds)

	print(json.dumps(civil_time_dict))

def lct_to_ut(civil_date, civil_time, is_dst, zone_correction):
	'''
	Convert local civil time to universal time.
	'''
	cd_split = civil_date.split("/")
	ct_split = civil_time.split(":")
	ut_hours,ut_minutes,ut_seconds,gw_day,gw_month,gw_year = PA_DT.local_civil_time_to_universal_time(int(ct_split[0]), int(ct_split[1]), int(ct_split[2]), is_dst, zone_correction, int(cd_split[1]), int(cd_split[0]), int(cd_split[2]))
	ut_dict = dict(utHours=ut_hours,utMinutes=ut_minutes,utSeconds=ut_seconds,greenwichDay=gw_day,greenwichMonth=gw_month,greenwichYear=gw_year)

	print(json.dumps(ut_dict))

def ut_to_lct(civil_date, universal_time, is_dst, zone_correction):
	'''
	Convert universal time to local civil time.
	'''
	cd_split = civil_date.split("/")
	ut_split = universal_time.split(":")
	lct_hours,lct_minutes,lct_seconds,gw_day,gw_month,gw_year = PA_DT.universal_time_to_local_civil_time(int(ut_split[0]), int(ut_split[1]), int(ut_split[2]), is_dst, zone_correction, int(cd_split[1]), int(cd_split[0]), int(cd_split[2]))
	lct_dict = dict(lctHours=lct_hours,lctMinutes=lct_minutes,lctSeconds=lct_seconds,greenwichDay=gw_day,greenwichMonth=gw_month,greenwichYear=gw_year)

	print(json.dumps(lct_dict))

def ut_to_gst(universal_time, greenwich_date):
	'''
	Convert Universal time to Greenwich sidereal time
	'''
	ut_split = universal_time.split(":")
	gd_split = greenwich_date.split("/")
	gst_hours,gst_minutes,gst_seconds = PA_DT.universal_time_to_greenwich_sidereal_time(int(ut_split[0]), int(ut_split[1]), float(ut_split[2]), int(gd_split[1]), int(gd_split[0]), int(gd_split[2]))
	gst_dict = dict(greenwichSiderealTimeHours=gst_hours, greenwichSiderealTimeMinutes=gst_minutes, greenwichSiderealTimeSeconds=gst_seconds)

	print(json.dumps(gst_dict))

def gst_to_ut(greenwich_sidereal_time, greenwich_date):
	'''
	Convert Greenwich sidereal time to universal time
	'''
	gst_split = greenwich_sidereal_time.split(":")
	gd_split = greenwich_date.split("/")
	ut_hours,ut_minutes,ut_seconds,status_message = PA_DT.greenwich_sidereal_time_to_universal_time(int(gst_split[0]),int(gst_split[1]),float(gst_split[2]),int(gd_split[1]),int(gd_split[0]),int(gd_split[2]))
	ut_dict = dict(utHours=ut_hours,utMinutes=ut_minutes,utSeconds=ut_seconds,statusMessage=status_message)

	print(json.dumps(ut_dict))

def gst_to_lst(greenwich_sidereal_time, geographical_longitude):
	'''
	Convert Greenwich sidereal time to local sidereal time
	'''
	gst_split = greenwich_sidereal_time.split(":")
	lst_hours,lst_minutes,lst_seconds = PA_DT.greenwich_sidereal_time_to_local_sidereal_time(int(gst_split[0]), int(gst_split[1]), float(gst_split[2]), geographical_longitude)
	lst_dict = dict(lstHours=lst_hours,lstMinutes=lst_minutes,lstSeconds=lst_seconds)

	print(json.dumps(lst_dict))

def lst_to_gst(local_sidereal_time, geographical_longitude):
	'''
	Convert local sidereal time to Greenwich sidereal time
	'''
	lst_split = local_sidereal_time.split(":")
	gst_hours,gst_minutes,gst_seconds = PA_DT.local_sidereal_time_to_greenwich_sidereal_time(int(lst_split[0]),int(lst_split[1]),float(lst_split[2]),geographical_longitude)
	gst_dict = dict(gstHours=gst_hours,gstMinutes=gst_minutes,gstSeconds=gst_seconds)

	print(json.dumps(gst_dict))

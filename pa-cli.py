#!/usr/bin/python3

import argparse
import json
import lib.pa_datetime as PA_DT
from dateutil.parser import parse

def display_error(error_description):
	'''
	Return error details for a failed call.
	'''
	error_dict = dict(errorDescription=error_description)

	print(json.dumps(error_dict))

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

def main():
	parser = argparse.ArgumentParser(description='Practical Astronomy CLI.')

	# Add argument groups
	actions_group = parser.add_argument_group(title="Actions")
	inputs_group = parser.add_argument_group(title="Inputs (used by Actions)")
	inputs_tz_group = parser.add_argument_group(title="Inputs (time zone management)")

	# Inputs
	inputs_group.add_argument("--cd", type=str, help="Civil date.  Input format: 'mm/dd/yyyy'")
	inputs_group.add_argument("--ct", type=str, help="Civil time.  Input format:  'hh:mm:ss'")
	inputs_group.add_argument("--dh", type=float, help="Decimal hours.  Input format: floating point number, e.g., 18.52416667")
	inputs_group.add_argument("--gd", type=str, help="Greenwich date.  Input format: 'mm/dd/yyyy'.  Fractional day is allowed, e.g., '6/19.75/2009'")
	inputs_group.add_argument("--gl", type=float, help="Geographical longitude.  Input format: (+/-)##.##, e.g., -64.00")
	inputs_group.add_argument("--gst", type=str, help="Greenwich sidereal time.  Input format: 'hh:mm:ss'")
	inputs_group.add_argument("--lst", type=str, help="Local sidereal time.  Input format: 'hh:mm:ss'")
	inputs_group.add_argument("--jd", type=float, help="Julian date.  Input format: floating point number, e.g., 2455002.25")
	inputs_group.add_argument("--ut", type=str, help="Universal time.  Input format:  'hh:mm:ss'")
	inputs_group.add_argument("--year", type=int, help="Calendar year, e.g. 2019.")

	# Inputs (time zone management)
	inputs_tz_group.add_argument('--dst', dest='is_daylight_savings', action='store_true', help="Observe daylight savings time.")
	inputs_tz_group.add_argument('--st', dest='is_daylight_savings', action='store_false', help="Observe standard time (default)")
	inputs_tz_group.set_defaults(is_daylight_savings=False)
	inputs_tz_group.add_argument("--zc", type=int, help="Offset, in hours, for time zone correction.")

	# Actions
	actions_group.add_argument("--doe", action='store_true', help="Calculate date of Easter, for a given year.")
	actions_group.add_argument("--cd_to_dn", action='store_true', help="Convert civil date to day number.")
	actions_group.add_argument("--gd_to_jd", action='store_true', help="Convert Greenwich date to Julian date.")
	actions_group.add_argument("--jd_to_gd", action='store_true', help="Convert Julian date to Greenwich date.")
	actions_group.add_argument("--ct_to_dh", action='store_true', help="Convert civil time to decimal hours.")
	actions_group.add_argument("--dh_to_ct", action='store_true', help="Convert decimal hours to civil time.")
	actions_group.add_argument("--lct_to_ut", action='store_true', help="Convert local civil time to universal time.")
	actions_group.add_argument("--ut_to_lct", action='store_true', help="Convert universal time to local civil time.")
	actions_group.add_argument("--ut_to_gst", action='store_true', help="Convert universal time to Greenwich sidereal time.")
	actions_group.add_argument("--gst_to_ut", action='store_true', help="Convert Greenwich sidereal time to universal time.")
	actions_group.add_argument("--gst_to_lst", action='store_true', help="Convert Greenwich sidereal time to local sidereal time.")
	actions_group.add_argument("--lst_to_gst", action='store_true', help="Convert local sidereal time to Greenwich sidereal time.")

	args=parser.parse_args()

	if args.doe:
		if not args.year:
			display_error("'year' argument is required.")
		else:
			doe_year(args.year)

	if args.cd_to_dn:
		if not args.cd:
			display_error("'cd' argument is required.")
		else:
			cd_to_dn(args.cd)

	if args.gd_to_jd:
		if not args.gd:
			display_error("'gd' argument is required.")
		else:
			gd_to_jd(args.gd)

	if args.jd_to_gd:
		if not args.jd:
			display_error("'jd' argument is required.")
		else:
			jd_to_gd(args.jd)

	if args.ct_to_dh:
		if not args.ct:
			display_error("'ct' argument is required.")
		else:
			ct_to_dh(args.ct)

	if args.dh_to_ct:
		if not args.dh:
			display_error("'dh' argument is required.")
		else:
			dh_to_ct(args.dh)

	if args.lct_to_ut:
		if not args.cd:
			display_error("'cd', argument is required.")
		elif not args.ct:
			display_error("'ct', argument is required.")
		elif not args.zc:
			display_error("'zc', argument is required.")
		else:
			lct_to_ut(args.cd, args.ct, args.is_daylight_savings, args.zc)

	if args.ut_to_lct:
		if not args.cd:
			display_error("'cd', argument is required.")
		elif not args.ut:
			display_error("'ut', argument is required.")
		elif not args.zc:
			display_error("'zc', argument is required.")
		else:
			ut_to_lct(args.cd, args.ut, args.is_daylight_savings, args.zc)

	if args.ut_to_gst:
		if not args.ut:
			display_error("'ut' argument is required.")
		elif not args.gd:
			display_error("'gd' argument is required.")
		else:
			ut_to_gst(args.ut, args.gd)

	if args.gst_to_ut:
		if not args.gst:
			display_error("'gst' argument is required.")
		elif not args.gd:
			display_error("'gd' argument is required.")
		else:
			gst_to_ut(args.gst, args.gd)

	if args.gst_to_lst:
		if not args.gst:
			display_error("'gst' argument is required.")
		elif not args.gl:
			display_error("'gl' argument is required.")
		else:
			gst_to_lst(args.gst, args.gl)

	if args.lst_to_gst:
		if not args.lst:
			display_error("'lst' argument is required.")
		elif not args.gl:
			display_error("'gl' argument is required.")
		else:
			lst_to_gst(args.lst, args.gl)

if __name__ == "__main__":
    main()

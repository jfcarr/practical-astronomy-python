#!/usr/bin/python3

import argparse
import json
from dateutil.parser import parse
import lib.pa_datetime as PA_DT
import cli_lib.pa_cli_datetime as PA_CLI_DT

def display_error(error_description):
	'''
	Return error details for a failed call.
	'''
	error_dict = dict(errorDescription=error_description)

	print(json.dumps(error_dict))

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
			PA_CLI_DT.doe_year(args.year)
			#doe_year(args.year)

	if args.cd_to_dn:
		if not args.cd:
			display_error("'cd' argument is required.")
		else:
			PA_CLI_DT.cd_to_dn(args.cd)

	if args.gd_to_jd:
		if not args.gd:
			display_error("'gd' argument is required.")
		else:
			PA_CLI_DT.gd_to_jd(args.gd)

	if args.jd_to_gd:
		if not args.jd:
			display_error("'jd' argument is required.")
		else:
			PA_CLI_DT.jd_to_gd(args.jd)

	if args.ct_to_dh:
		if not args.ct:
			display_error("'ct' argument is required.")
		else:
			PA_CLI_DT.ct_to_dh(args.ct)

	if args.dh_to_ct:
		if not args.dh:
			display_error("'dh' argument is required.")
		else:
			PA_CLI_DT.dh_to_ct(args.dh)

	if args.lct_to_ut:
		if not args.cd:
			display_error("'cd', argument is required.")
		elif not args.ct:
			display_error("'ct', argument is required.")
		elif not args.zc:
			display_error("'zc', argument is required.")
		else:
			PA_CLI_DT.lct_to_ut(args.cd, args.ct, args.is_daylight_savings, args.zc)

	if args.ut_to_lct:
		if not args.cd:
			display_error("'cd', argument is required.")
		elif not args.ut:
			display_error("'ut', argument is required.")
		elif not args.zc:
			display_error("'zc', argument is required.")
		else:
			PA_CLI_DT.ut_to_lct(args.cd, args.ut, args.is_daylight_savings, args.zc)

	if args.ut_to_gst:
		if not args.ut:
			display_error("'ut' argument is required.")
		elif not args.gd:
			display_error("'gd' argument is required.")
		else:
			PA_CLI_DT.ut_to_gst(args.ut, args.gd)

	if args.gst_to_ut:
		if not args.gst:
			display_error("'gst' argument is required.")
		elif not args.gd:
			display_error("'gd' argument is required.")
		else:
			PA_CLI_DT.gst_to_ut(args.gst, args.gd)

	if args.gst_to_lst:
		if not args.gst:
			display_error("'gst' argument is required.")
		elif not args.gl:
			display_error("'gl' argument is required.")
		else:
			PA_CLI_DT.gst_to_lst(args.gst, args.gl)

	if args.lst_to_gst:
		if not args.lst:
			display_error("'lst' argument is required.")
		elif not args.gl:
			display_error("'gl' argument is required.")
		else:
			PA_CLI_DT.lst_to_gst(args.lst, args.gl)

if __name__ == "__main__":
    main()

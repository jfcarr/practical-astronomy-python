import math
from . import pa_util as PU
from . import pa_macro as PM

def get_date_of_easter(year):
	"""
	Gets the date of Easter for the year specified.

	Arguments:
		year:	Year for which you'd like the date of Easter.

	Returns:
		month
		day
		year
	"""
	a = year % 19
	b = math.floor(year/100)
	c = year % 100
	d = math.floor(b/4)
	e = b % 4
	f = math.floor((b+8)/25)
	g = math.floor((b-f+1)/3)
	h = ((19*a)+b-d-g+15) % 30
	i = math.floor(c/4)
	k = c % 4
	l = (32 + 2 * (e + i) - h - k) % 7
	m = math.floor((a + (11 * h) + (22 * l)) / 451 )
	n = math.floor((h + l - (7 * m) + 114) / 31)
	p = (h + l - (7 * m) + 114) % 31
	
	day = p + 1
	month = n

	return month,day,year

def civil_date_to_day_number(month, day, year):
	""" Returns the day number for the date specified. """
	if month <= 2:
		month = month - 1
		month = month * 62 if PU.is_leap_year(year) else month * 63
		month = math.floor(month / 2)
	else:
		month = math.floor((month + 1) * 30.6)
		month = month - 62 if PU.is_leap_year(year) else month - 63
	
	return month + day

def greenwich_date_to_julian_date(day, month, year):
	""" Convert a Greenwich Date/Civil Date (day,month,year) to Julian Date """
	return PM.cd_jd(day,month,year)

def julian_date_to_greenwich_date(julianDate):
	""" Convert a Julian Date to Greenwich Date/Civil Date (day,month,year) """
	returnDay = julian_date_day(julianDate)
	returnMonth = julian_date_month(julianDate)
	returnYear = julian_date_year(julianDate)

	return returnDay,returnMonth,returnYear

def julian_date_day(julianDate):
	""" Returns the day part of a Julian Date """
	return PM.jdc_day(julianDate)

def julian_date_month(julianDate):
	""" Returns the month part of a Julian Date """
	return PM.jdc_month(julianDate)

def julian_date_year(julianDate):
	""" Returns the year part of a Julian Date """
	return PM.jdc_year(julianDate)

def julian_date_to_weekday_name(julianDate):
	""" Convert a Julian Date to Day-of-Week (e.g., Sunday) """
	return PM.f_dow(julianDate)

def civil_time_to_decimal_hours(hours,minutes,seconds):
	""" Convert a Civil Time (hours,minutes,seconds) to Decimal Hours """
	return PM.hms_dh(hours,minutes,seconds)

def decimal_hour_hour(decimalHours):
	""" Return the hour part of a Decimal Hours """
	return PM.dh_hour(decimalHours)

def decimal_hour_minutes(decimalHours):
	""" Return the minutes part of a Decimal Hours """
	return PM.dh_min(decimalHours)

def decimal_hour_seconds(decimalHours):
	""" Return the seconds part of a Decimal Hours """
	return PM.dh_sec(decimalHours)

def decimal_hours_to_civil_time(decimalHours):
	""" Convert Decimal Hours to Civil Time """
	hours = PM.dh_hour(decimalHours)
	minutes = PM.dh_min(decimalHours)
	seconds = PM.dh_sec(decimalHours)

	return hours,minutes,seconds

def local_civil_time_to_universal_time(lctHours,lctMinutes,lctSeconds,isDaylightSavings, zoneCorrection, localDay,localMonth,localYear):
	"""
	Convert local Civil Time to Universal Time

	Returns:
		UT hours
		UT mins
		UT secs
		GW day
		GW month
		GW year
	"""
	LCT = civil_time_to_decimal_hours(lctHours,lctMinutes,lctSeconds)
	
	daylightSavingsOffset = 1 if isDaylightSavings == True else 0
	UTinterim = LCT - daylightSavingsOffset - zoneCorrection
	GDayInterim = localDay + (UTinterim / 24)

	JD = PM.cd_jd(GDayInterim,localMonth,localYear)
	
	GDay = julian_date_day(JD)
	GMonth = julian_date_month(JD)
	GYear = julian_date_year(JD)
	
	UT = 24 * (GDay - math.floor(GDay))
	
	return decimal_hour_hour(UT),decimal_hour_minutes(UT),decimal_hour_seconds(UT),math.floor(GDay),GMonth,GYear

def universal_time_to_local_civil_time(utHours,utMinutes,utSeconds,isDayLightSavings, zoneCorrection,gwDay,gwMonth,gwYear):
	"""
	Convert Universal Time to local Civil Time

	Returns:
		LCT hours
		LCT minutes
		LCT seconds
		day
		month
		year
	"""
	UT = civil_time_to_decimal_hours(utHours,utMinutes,utSeconds)
	zoneTime = UT + zoneCorrection
	localTime = zoneTime + (1 if isDayLightSavings == True else 0)
	localJDPlusLocalTime = greenwich_date_to_julian_date(gwDay,gwMonth,gwYear) + (localTime/24)
	localDay = julian_date_day(localJDPlusLocalTime)
	integerDay = math.floor(localDay)
	localMonth = julian_date_month(localJDPlusLocalTime)
	localYear = julian_date_year(localJDPlusLocalTime)
	LCT = 24 * (localDay - integerDay)

	return decimal_hour_hour(LCT),decimal_hour_minutes(LCT),decimal_hour_seconds(LCT),integerDay,localMonth,localYear

def universal_time_to_greenwich_sidereal_time(utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear):
	"""
	Convert Universal Time to Greenwich Sidereal Time

	Returns:
		GST hours
		GST minutes
		GST seconds
	"""
	JD = greenwich_date_to_julian_date(gwDay,gwMonth,gwYear)
	S = JD - 2451545
	T = S / 36525
	T01 = 6.697374558+(2400.051336*T)+(0.000025862*T*T)
	T02 = T01-(24*math.floor(T01/24))
	UT = civil_time_to_decimal_hours(utHours,utMinutes,utSeconds)
	A = UT*1.002737909
	GST1 = T02 + A
	GST2 = GST1 - (24*math.floor(GST1/24))

	gstHours = decimal_hour_hour(GST2)
	gstMinutes = decimal_hour_minutes(GST2)
	gstSeconds = decimal_hour_seconds(GST2)
			
	return gstHours,gstMinutes,gstSeconds

def greenwich_sidereal_time_to_universal_time(gstHours,gstMinutes,gstSeconds,gwDay,gwMonth,gwYear):
	"""
	Convert Greenwich Sidereal Time to Universal Time

	Returns:
		UT hours
		UT minutes
		UT seconds
		Warning Flag
	"""
	JD = greenwich_date_to_julian_date(gwDay,gwMonth,gwYear)
	S = JD - 2451545
	T = S / 36525
	T01 = 6.697374558 + (2400.051336*T) + (0.000025862*T*T)
	T02 = T01-(24*math.floor(T01/24))
	gstHours = civil_time_to_decimal_hours(gstHours,gstMinutes,gstSeconds)
	A = gstHours-T02
	B = A-(24*math.floor(A/24))
	UT = B*0.9972695663	
	
	utHours = decimal_hour_hour(UT)
	utMinutes = decimal_hour_minutes(UT)
	utSeconds = decimal_hour_seconds(UT)
	warningFlag = "Warning" if UT < 0.065574 else "OK"  # TODO: Log this somewhere...

	return utHours,utMinutes,utSeconds,warningFlag

def greenwich_sidereal_time_to_local_sidereal_time(gstHours,gstMinutes,gstSeconds,geographicalLongitude):
	"""
	Convert Greenwich Sidereal Time to Local Sidereal Time

	Returns:
		LST hours
		LST minutes
		LST seconds
	"""
	GST = civil_time_to_decimal_hours(gstHours,gstMinutes,gstSeconds)
	offset = geographicalLongitude / 15
	lstHours1 = GST + offset
	lstHours2 = lstHours1-(24*math.floor(lstHours1/24))
	
	lstHours = decimal_hour_hour(lstHours2)
	lstMinutes = decimal_hour_minutes(lstHours2)
	lstSeconds = decimal_hour_seconds(lstHours2)

	return lstHours,lstMinutes,lstSeconds

def local_sidereal_time_to_greenwich_sidereal_time(lstHours,lstMinutes,lstSeconds,geographicalLongitude):
	"""
	Convert Local Sidereal Time to Greenwich Sidereal Time

	Returns:
		GST hours
		GST minutes
		GST seconds
	"""
	GST = civil_time_to_decimal_hours(lstHours,lstMinutes,lstSeconds)
	longHours = geographicalLongitude / 15
	GST1 = GST - longHours
	GST2 = GST1 - (24*math.floor(GST1/24))
	
	gstHours = decimal_hour_hour(GST2)
	gstMinutes = decimal_hour_minutes(GST2)
	gstSeconds = decimal_hour_seconds(GST2)

	return gstHours,gstMinutes,gstSeconds

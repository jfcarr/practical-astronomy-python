import math
import numpy as np

def cd_jd(day, month, year):
	"""
	Convert a Greenwich Date/Civil Date (day,month,year) to Julian Date

	Original macro name: CDJD
	"""
	Y = year - 1 if month < 3 else year
	M = month + 12 if month < 3 else month

	if year > 1582:
		A = math.floor(Y / 100)
		B = 2 - A + math.floor(A / 4)
	else:
		if year == 1582 and month > 10:
			A = math.floor(Y / 100)
			B = 2 - A + math.floor(A / 4)
		else:
			if year == 1582 and month == 10 and day >= 15:
				A = math.floor(Y / 100)
				B = 2 - A + math.floor(A / 4)
			else:
				B = 0
	
	C = math.floor((365.25 * Y) - 0.75) if Y < 0 else math.floor(365.25 * Y)

	D = math.floor(30.6001 * (M + 1))

	return B + C + D + day + 1720994.5

def jdc_day(julianDate):
	"""
	Returns the day part of a Julian Date

	Original macro name: JDCDay
	"""
	I = math.floor(julianDate + 0.5)
	F = julianDate + 0.5 - I
	A = math.floor((I - 1867216.25) / 36524.25)
	B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
	C = B + 1524
	D = math.floor((C - 122.1) / 365.25)
	E = math.floor(365.25 * D)
	G = math.floor((C - E) / 30.6001)

	return C - E + F - math.floor(30.6001 * G)

def jdc_month(julianDate):
	"""
	Returns the month part of a Julian Date
	
	Original macro name: JDCMonth
	"""
	I = math.floor(julianDate + 0.5)
	F = julianDate + 0.5 - I
	A = math.floor((I - 1867216.25) / 36524.25)
	B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
	C = B + 1524
	D = math.floor((C - 122.1) / 365.25)
	E = math.floor(365.25 * D)
	G = math.floor((C - E) / 30.6001)

	returnValue = G - 1 if G < 13.5 else G - 13
	return returnValue

def jdc_year(julianDate):
	"""
	Returns the year part of a Julian Date
	
	Original macro name: JDCYear
	"""
	I = math.floor(julianDate + 0.5)
	F = julianDate + 0.5 - I
	A = math.floor((I - 1867216.25) / 36524.25)
	B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
	C = B + 1524
	D = math.floor((C - 122.1) / 365.25)
	E = math.floor(365.25 * D)
	G = math.floor((C - E) / 30.6001)
	H = G - 1 if G < 13.5 else G - 13

	returnValue = D - 4716 if H > 2.5 else D - 4715
	return returnValue

def f_dow(julianDate):
	"""
	Convert a Julian Date to Day-of-Week (e.g., Sunday)
	
	Original macro name: FDOW
	"""
	J = math.floor(julianDate - 0.5) + 0.5
	N = (J + 1.5) % 7
	
	if N == 0: return "Sunday"
	if N == 1: return "Monday"
	if N == 2: return "Tuesday"
	if N == 3: return "Wednesday"
	if N == 4: return "Thursday"
	if N == 5: return "Friday"
	if N == 6: return "Saturday"

	return "Unknown"

def hms_dh(hours,minutes,seconds):
	"""
	Convert a Civil Time (hours,minutes,seconds) to Decimal Hours
	
	Original macro name: HMSDH
	"""
	A = abs(seconds) / 60
	B = (abs(minutes) + A) / 60
	C = abs(hours) + B
	
	return -C if ((hours < 0) or (minutes < 0) or (seconds < 0)) else C

def dh_hour(decimalHours):
	"""
	Return the hour part of a Decimal Hours
	
	Original macro name: DHHour
	"""
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return -(math.floor(E / 3600)) if decimalHours < 0 else math.floor(E / 3600)

def dh_min(decimalHours):
	"""
	Return the minutes part of a Decimal Hours
	
	Original macro name: DHMin
	"""
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return math.floor(E / 60) % 60

def dh_sec(decimalHours):
	"""
	Return the seconds part of a Decimal Hours
	
	Original macro name: DHSec
	"""
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C

	return D

def lct_ut(lctHours,lctMinutes,lctSeconds,daylightSaving,zoneCorrection,localDay,localMonth,localYear):
	"""
	Convert Local Civil Time to Universal Time
	 
	Original macro name: LctUT
	"""
	A = hms_dh(lctHours,lctMinutes,lctSeconds)
	B = A - daylightSaving - zoneCorrection
	C = localDay + (B/24)
	D = cd_jd(C, localMonth, localYear)
	E = jdc_day(D)
	E1 = math.floor(E)
	
	return 24 * (E - E1)

def ut_lct(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	"""
	Convert Universal Time to Local Civil Time

	Original macro name: UTLct 	
	"""
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	E = jdc_day(D)
	E1 = math.floor(E)
	
	return 24 * (E - E1)

def ut_lc_day(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	"""
	Get Local Civil Day for Universal Time
	
	Original macro name: UTLcDay
	"""
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	E = jdc_day(D)
	E1 = math.floor(E)
	
	return E1

def ut_lc_month(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	"""
	Get Local Civil Month for Universal Time
	
	Original macro name: UTLcMonth
	"""
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	
	return jdc_month(D)

def ut_lc_year(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	"""
	Get Local Civil Year for Universal Time
	
	Original macro name: UTLcYear
	"""
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	
	return jdc_year(D)

def lct_gday(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	"""
	Determine Greenwich Day for Local Time
	
	Original macro name: LctGDay
	"""
	A = hms_dh(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = cd_jd(C,local_month,local_year)
	E = jdc_day(D)
	
	return math.floor(E)

def lct_gmonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	"""
	Determine Greenwich Month for Local Time
	
	Original macro name: LctGMonth
	"""
	A = hms_dh(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = cd_jd(C,local_month,local_year)
	
	return jdc_month(D)

def lct_gyear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	"""
	Determine Greenwich Year for Local Time
	
	Original macro name: LctGYear
	"""
	A = hms_dh(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = cd_jd(C,local_month,local_year)
	
	return jdc_year(D)

def ut_gst(u_hours,u_minutes,u_seconds,greenwich_day,greenwich_month,greenwich_year):
	"""
	Convert Universal Time to Greenwich Sidereal Time
	
	Original macro name: UTGST
	"""
	A = cd_jd(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = hms_dh(u_hours,u_minutes,u_seconds)
	G = F * 1.002737909
	H = E + G
	
	return H - (24 * math.floor(H / 24))

def gst_lst(greenwich_hours,greenwich_minutes,greenwich_seconds,geographical_longitude):
	"""
	Convert Greenwich Sidereal Time to Local Sidereal Time
	
	Original macro name: GSTLST
	"""
	A = hms_dh(greenwich_hours,greenwich_minutes,greenwich_seconds)
	B = geographical_longitude / 15
	C = A + B

	return C - (24 * math.floor(C / 24))

def lst_gst(local_hours,local_minutes,local_seconds,longitude):
	"""
	Convert Local Sidereal Time to Greenwich Sidereal Time
	
	Original macro name: LSTGST
	"""
	A = hms_dh(local_hours,local_minutes,local_seconds)
	B = longitude / 15
	C = A - B
	
	return C - (24 * math.floor(C / 24))

def gst_ut(greenwich_sidereal_hours,greenwich_sidereal_minutes,greenwich_sidereal_seconds,greenwich_day,greenwich_month,greenwich_year):
	"""
	Convert Greenwich Sidereal Time to Universal Time
	
	Original macro name: GSTUT
	"""
	A = cd_jd(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = hms_dh(greenwich_sidereal_hours,greenwich_sidereal_minutes,greenwich_sidereal_seconds)
	G = F - E
	H = G - (24 * math.floor(G / 24))
	
	return H * 0.9972695663

def e_gst_ut(GSH, GSM, GSS, GD, GM, GY):
	"""
	Status of conversion of Greenwich Sidereal Time to Universal Time.

	Original macro name: eGSTUT
	"""
	A = cd_jd(GD, GM, GY)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = hms_dh(GSH, GSM, GSS)
	G = F - E
	H = G - (24 * math.floor(G / 24))

	return "Warning" if ((H * 0.9972695663) < (4 / 60)) else "OK"

def ra_ha(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude):
	"""
	Convert Right Ascension to Hour Angle
	
	Original macro name: RAHA
	"""
	A = lct_ut(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	B = lct_gday(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	C = lct_gmonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	D = lct_gyear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	E = ut_gst(A, 0, 0, B, C, D)
	F = gst_lst(E, 0, 0, geographical_longitude)
	G = hms_dh(ra_hours, ra_minutes, ra_seconds)
	H = F - G
	
	return 24 + H if H < 0 else H

def ha_ra(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude):
	"""
	Convert Hour Angle to Right Ascension
	
	Original macro name: HARA
	"""
	A = lct_ut(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	B = lct_gday(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	C = lct_gmonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	D = lct_gyear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	E = ut_gst(A, 0, 0, B, C, D)
	F = gst_lst(E, 0, 0, geographical_longitude)
	G = hms_dh(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	H = F - G

	return 24 + H if H < 0 else H

def dms_dd(degrees,minutes,seconds):
	"""
	Convert Degrees Minutes Seconds to Decimal Degrees
	
	Original macro name: DMSDD
	"""
	A = abs(seconds) / 60
	B = (abs(minutes) + A) / 60
	C = abs(degrees) + B

	return -C if degrees < 0 or minutes < 0 or seconds < 0 else C

def dd_deg(decimal_degrees):
	"""
	Return Degrees part of Decimal Degrees
	
	Original macro name: DDDeg
	"""
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C
	E = B = 60 if C == 60 else B

	return -math.floor(E/3600) if decimal_degrees < 0 else math.floor(E/3600)

def dd_min(decimal_degrees):
	"""
	Return Minutes part of Decimal Degrees
	
	Original macro name: DDMin
	"""
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return math.floor(E/60) % 60

def dd_sec(decimal_degrees):
	"""
	Return Seconds part of Decimal Degrees
	
	Original macro name: DDSec
	"""
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C

	return D

def dd_dh(decimal_degrees):
	"""
	Convert Decimal Degrees to Degree-Hours
	
	Original macro name: DDDH
	"""
	return decimal_degrees / 15

def dh_dd(degree_hours):
	"""
	Convert Degree-Hours to Decimal Degrees
	
	Original macro name: DHDD
	"""
	return degree_hours * 15

def degrees(W):
	"""
	Convert W to Degrees
	
	Original macro name: Degrees
	"""
	return W * 57.29577951

def atan2(X, Y):
	"""
	Custom ATAN2 function
	
	Original macro name: Atan2
	"""
	B = 3.1415926535
	if abs(X) < 1e-20:
		if Y < 0:
			A = -B / 2
		else:
			A = B / 2
	else:
		A = math.atan(Y/X)

	if X < 0:
		A = B + A
	
	if A < 0:
		A = A + 2 * B

	return A

def eq_az(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	"""
	Convert Equatorial Coordinates to Azimuth (in decimal degrees)
	
	Original macro name: EQAz
	"""
	A = hms_dh(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	B = A * 15
	C = math.radians(B)
	D = dms_dd(declination_degrees,declination_minutes,declination_seconds)
	E = math.radians(D)
	F = math.radians(geographical_latitude)
	G = math.sin(E) * math.sin(F) + math.cos(E) * math.cos(F) * math.cos(C)
	H = -math.cos(E) * math.cos(F) * math.sin(C)
	I = math.sin(E) - (math.sin(F) * G)
	J = degrees(math.atan2(H,I))
	
	return J - 360 * math.floor(J / 360)

def eq_alt(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	"""
	Convert Equatorial Coordinates to Altitude (in decimal degrees)
	
	Original macro name: EQAlt
	"""
	A = hms_dh(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	B = A * 15
	C = math.radians(B)
	D = dms_dd(declination_degrees,declination_minutes,declination_seconds)
	E = math.radians(D)
	F = math.radians(geographical_latitude)
	G = math.sin(E) * math.sin(F) + math.cos(E) * math.cos(F) * math.cos(C)

	return degrees(math.asin(G))

def hor_dec(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	"""
	Convert Horizon Coordinates to Declination (in decimal degrees)
	
	Original macro name: HORDec
	"""
	A = dms_dd(azimuth_degrees,azimuth_minutes,azimuth_seconds)
	B = dms_dd(altitude_degrees,altitude_minutes,altitude_seconds)
	C = math.radians(A)
	D = math.radians(B)
	E = math.radians(geographical_latitude)
	F = math.sin(D) * math.sin(E) + math.cos(D) * math.cos(E) * math.cos(C)
	
	return degrees(math.asin(F))

def hor_ha(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	"""
	Convert Horizon Coordinates to Hour Angle (in decimal degrees)
	
	Original macro name: HORHa
	"""
	A = dms_dd(azimuth_degrees,azimuth_minutes,azimuth_seconds)
	B = dms_dd(altitude_degrees,altitude_minutes,altitude_seconds)
	C = math.radians(A)
	D = math.radians(B)
	E = math.radians(geographical_latitude)
	F = math.sin(D) * math.sin(E) + math.cos(D) * math.cos(E) * math.cos(C)
	G = -math.cos(D) * math.cos(E) * math.sin(C)
	H = math.sin(D) - math.sin(E) * F
	I = dd_dh(degrees(math.atan2(G,H)))
	
	return I - 24 * math.floor(I / 24)

def nutat_obl(greenwich_day,greenwich_month,greenwich_year):
	"""
	Nutation of Obliquity
	
	Original macro name: NutatObl
	"""
	DJ = cd_jd(greenwich_day,greenwich_month,greenwich_year) - 2415020
	T = DJ / 36525
	T2 = T * T

	A = 100.0021358 * T
	B = 360 * (A - math.floor(A))

	L1 = 279.6967 + 0.000303 * T2 + B
	l2 = 2 * math.radians(L1)

	A = 1336.855231 * T
	B = 360 * (A - math.floor(A))

	D1 = 270.4342 - 0.001133 * T2 + B
	D2 = 2 * math.radians(D1)

	A = 99.99736056 * T
	B = 360 * (A - math.floor(A))

	M1 = 358.4758 - 0.00015 * T2 + B
	M1 = math.radians(M1)

	A = 1325.552359 * T
	B = 360 * (A - math.floor(A))

	M2 = 296.1046 + 0.009192 * T2 + B
	M2 = math.radians(M2)

	A = 5.372616667 * T
	B = 360 * (A - math.floor(A))

	N1 = 259.1833 + 0.002078 * T2 - B
	N1 = math.radians(N1)

	N2 = 2 * N1

	DDO = (9.21 + 0.00091 * T) * math.cos(N1)
	DDO = DDO + (0.5522 - 0.00029 * T) * math.cos(l2) - 0.0904 * math.cos(N2)
	DDO = DDO + 0.0884 * math.cos(D2) + 0.0216 * math.cos(l2 + M1)
	DDO = DDO + 0.0183 * math.cos(D2 - N1) + 0.0113 * math.cos(D2 + M2)
	DDO = DDO - 0.0093 * math.cos(l2 - M1) - 0.0066 * math.cos(l2 - N1)

	return DDO / 3600

def obliq(greenwich_day,greenwich_month,greenwich_year):
	"""
	Obliquity of the Ecliptic for a Greenwich Date
	
	Original macro name: Obliq
	"""
	A = cd_jd(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2415020
	C = (B / 36525) - 1
	D = C * (46.815 + C * (0.0006 - (C * 0.00181)))
	E = D / 3600
	
	return 23.43929167 - E + nutat_obl(greenwich_day,greenwich_month,greenwich_year)

def sun_long(LCH,LCM,LCS,DS,ZC,LD,LM,LY):
	"""
	Calculate Sun's ecliptic longitude
	
	Original macro name: SunLong
	"""
	AA = lct_gday(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	BB = lct_gmonth(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	CC = lct_gyear(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	UT = lct_ut(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	DJ = cd_jd(AA, BB, CC) - 2415020
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T
	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))
	
	L = 279.69668 + 0.0003025 * T2 + B
	A = 99.99736042 * T
	B = 360 * (A - math.floor(A))
	
	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	EC = 0.01675104 - 0.0000418 * T - 0.000000126 * T2

	AM = math.radians(M1)
	AT = true_anomaly(AM, EC)
	AE = eccentric_anomaly(AM, EC)

	A = 62.55209472 * T
	B = 360 * (A - math.floor(A))

	A1 = math.radians(153.23 + B)
	A = 125.1041894 * T
	B = 360 * (A - math.floor(A))

	B1 = math.radians(216.57 + B)
	A = 91.56766028 * T
	B = 360 * (A - math.floor(A))

	C1 = math.radians(312.69 + B)
	A = 1236.853095 * T
	B = 360 * (A - math.floor(A))

	D1 = math.radians(350.74 - 0.00144 * T2 + B)
	E1 = math.radians(231.19 + 20.2 * T)
	A = 183.1353208 * T
	B = 360 * (A - math.floor(A))
	H1 = math.radians(353.4 + B)

	D2 = 0.00134 * math.cos(A1) + 0.00154 * math.cos(B1) + 0.002 * math.cos(C1)
	D2 = D2 + 0.00179 * math.sin(D1) + 0.00178 * math.sin(E1)
	D3 = 0.00000543 * math.sin(A1) + 0.00001575 * math.sin(B1)
	D3 = D3 + 0.00001627 * math.sin(C1) + 0.00003076 * math.cos(D1)
	D3 = D3 + 0.00000927 * math.sin(H1)

	SR = AT + math.radians(L - M1 + D2)
	TP = 6.283185308

	SR = SR - TP * math.floor(SR / TP)

	return degrees(SR)

def sun_dist(LCH,LCM,LCS,DS,ZC,LD,LM,LY):
	"""
	Calculate Sun's distance from the Earth in astronomical units
	
	Original macro name: SunDist
	"""
	AA = lct_gday(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	BB = lct_gmonth(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	CC = lct_gyear(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	UT = lct_ut(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	DJ = cd_jd(AA,BB,CC) - 2415020
	
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T

	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))
	L = 279.69668 + 0.0003025 * T2 + B
	A = 99.99736042 * T
	B = 360 * (A - math.floor(A))
	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	EC = 0.01675104 - 0.0000418 * T - 0.000000126 * T2

	AM = math.radians(M1)
	AT = true_anomaly(AM,EC)
	AE = eccentric_anomaly(AM, EC)

	A = 62.55209472 * T
	B = 360 * (A - math.floor(A))
	A1 = math.radians(153.23 + B)
	A = 125.1041894 * T
	B = 360 * (A - math.floor(A))
	B1 = math.radians(216.57 + B)
	A = 91.56766028 * T
	B = 360 * (A - math.floor(A))
	C1 = math.radians(312.69 + B)
	A = 1236.853095 * T
	B = 360 * (A - math.floor(A))
	D1 = math.radians(350.74 - 0.00144 * T2 + B)
	E1 = math.radians(231.19 + 20.2 * T)
	A = 183.1353208 * T
	B = 360 * (A - math.floor(A))
	H1 = math.radians(353.4 + B)

	D2 = 0.00134 * math.cos(A1) + 0.00154 * math.cos(B1) + 0.002 * math.cos(C1)
	D2 = D2 + 0.00179 * math.sin(D1) + 0.00178 * math.sin(E1)
	D3 = 0.00000543 * math.sin(A1) + 0.00001575 * math.sin(B1)
	D3 = D3 + 0.00001627 * math.sin(C1) + 0.00003076 * math.cos(D1)
	D3 = D3 + 0.00000927 * math.sin(H1)

	return 1.0000002 * (1 - EC * math.cos(AE)) + D3

def sun_dia(LCH,LCM,LCS,DS,ZC,LD,LM,LY):
	"""
	Calculate Sun's angular diameter in decimal degrees
	
	Original macro name: SunDia
	"""
	A = sun_dist(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	
	return 0.533128 / A

def true_anomaly(AM,EC):
	"""
	Solve Kepler's equation, and return value of the true anomaly in radians
	
	Original macro name: TrueAnomaly
	"""
	TP = 6.283185308
	M = AM - TP * math.floor(AM / TP)
	AE = M

	while 1 == 1:
		D = AE - (EC * math.sin(AE)) - M
		if abs(D) < 0.000001:
			break
		D = D / (1 - (EC * math.cos(AE)))
		AE = AE - D

	A = math.sqrt((1 + EC) / (1 - EC)) * math.tan(AE / 2)
	AT = 2 * math.atan(A)

	return AT

def eccentric_anomaly(AM,EC):
	"""
	Solve Kepler's equation, and return value of the eccentric anomaly in radians
	
	Original macro name: EccentricAnomaly
	"""
	TP = 6.283185308
	M = AM - TP * math.floor(AM / TP)
	AE = M

	while 1 == 1:
		D = AE - (EC * math.sin(AE)) - M

		if abs(D) < 0.000001:
			break

		D = D / (1 - (EC * math.cos(AE)))
		AE = AE - D

	return AE

def refract(Y2,SW,PR,TR):
	"""
	Calculate effects of refraction
	
	Original macro name: Refract
	"""
	Y = math.radians(Y2)
	
	D = -1 if SW[0].lower() == "t" else 1

	if D == -1:
		Y3 = Y
		Y1 = Y
		R1 = 0

		while 1 == 1:
			Y = Y1 + R1
			Q = Y
			
			RF = refract_l3035(PR,TR,Y,D)

			if Y < -0.087:
				return 0
			
			R2 = RF

			if (R2 == 0) or (abs(R2 - R1) < 0.000001):
				Q = Y3
				return degrees(Q + RF)

			R1 = R2

	RF = refract_l3035(PR,TR,Y,D)

	if Y < -0.087:
		return 0

	Q = Y

	return degrees(Q + RF)

def refract_l3035(PR,TR,Y,D):
	""" Helper function for refract """
	if Y < 0.2617994:
		if Y < -0.087:
			return 0

		YD = degrees(Y)
		A = ((0.00002 * YD + 0.0196) * YD + 0.1594) * PR
		B = (273 + TR) * ((0.0845 * YD + 0.505) * YD + 1)

		return math.radians(-(A / B) * D)

	return -D * 0.00007888888 * PR / ((273 + TR) * math.tan(Y))

def parallax_ha(HH,HM,HS,DD,DM,DS,SW,GP,HT,HP):
	"""
	Calculate corrected hour angle in decimal hours
	
	Original macro name: ParallaxHA
	"""
	A = math.radians(GP)
	C1 = math.cos(A)
	S1 = math.sin(A)

	U = math.atan(0.996647 * S1 / C1)
	
	C2 = math.cos(U)
	S2 = math.sin(U)
	B = HT / 6378160

	RS = (0.996647 * S2) + (B * S1)
	
	RC = C2 + (B * C1)
	TP = 6.283185308

	RP = 1 / math.sin(math.radians(HP))

	X = math.radians(dh_dd(hms_dh(HH, HM, HS)))
	X1 = X

	Y = math.radians(dms_dd(DD, DM, DS))
	Y1 = Y

	D = 1 if SW[0].lower() == "t" else -1

	if D == 1:
		P,Q = parallax_ha_l2870(X,Y,RC,RP,RS,TP)
		return dd_dh(degrees(P))

	P1 = 0
	Q1 = 0
	while 1==1:
		P,Q = parallax_ha_l2870(X,Y,RC,RP,RS,TP)
		
		P2 = P - X
		Q2 = Q - Y

		AA = abs(P2 - P1)
		BB = abs(Q2 - Q1)

		if (AA < 0.000001) and (BB < 0.000001):
			P = X1 - P2
			Q = Y1 - Q2
			X = X1
			Y = Y1
			return dd_dh(degrees(P))
		
		X = X1 - P2
		Y = Y1 - Q2
		P1 = P2
		Q1 = Q2

def parallax_ha_l2870(X,Y,RC,RP,RS,TP):
	""" Helper function for parallax_ha """
	CX = math.cos(X)
	SY = math.sin(Y)
	CY = math.cos(Y)

	AA = (RC * math.sin(X)) / ((RP * CY) - (RC * CX))
	
	DX = math.atan(AA)
	P = X + DX
	CP = math.cos(P)

	P = P - TP * math.floor(P / TP)
	Q = math.atan(CP * (RP * SY - RS) / (RP * CY * CX - RC))

	return P,Q

def parallax_dec(HH,HM,HS,DD,DM,DS,SW,GP,HT,HP):
	"""
	Calculate corrected declination in decimal degrees
	
	Original macro name: ParallaxDec
	"""
	A = math.radians(GP)
	C1 = math.cos(A)
	S1 = math.sin(A)

	U = math.atan(0.996647 * S1 / C1)
	
	C2 = math.cos(U)
	S2 = math.sin(U)
	B = HT / 6378160
	RS = (0.996647 * S2) + (B * S1)
	
	RC = C2 + (B * C1)
	TP = 6.283185308

	RP = 1 / math.sin(math.radians(HP))

	X = math.radians(dh_dd(hms_dh(HH, HM, HS)))
	X1 = X

	Y = math.radians(dms_dd(DD, DM, DS))
	Y1 = Y

	D = 1 if SW[0].lower() == "t" else -1

	if D == 1:
		P,Q = parallax_dec_l2870(X,Y,RC,RP,RS,TP)
		return degrees(Q)

	P1 = 0
	Q1 = 0

	while 1 == 1:
		P,Q = parallax_dec_l2870(X,Y,RC,RP,RS,TP)
		
		P2 = P - X
		Q2 = Q - Y

		AA = abs(P2 - P1)
		BB = abs(Q2 - Q1)

		if (AA < 0.000001) and (BB < 0.000001):
			P = X1 - P2
			Q = Y1 - Q2
			X = X1
			Y = Y1
			return degrees(Q)
		
		X = X1 - P2
		Y = Y1 - Q2
		P1 = P2
		Q1 = Q2

def parallax_dec_l2870(X,Y,RC,RP,RS,TP):
	""" Helper function for parallax_dec """
	CX = math.cos(X)
	SY = math.sin(Y)
	CY = math.cos(Y)

	AA = (RC * math.sin(X)) / ((RP * CY) - (RC * CX))
	
	DX = math.atan(AA)
	P = X + DX
	CP = math.cos(P)

	P = P - TP * math.floor(P / TP)
	Q = math.atan(CP * (RP * SY - RS) / (RP * CY * CX - RC))
	
	return P,Q

def unwind(W):
	"""
	Convert angle in radians to equivalent angle in degrees.
	
	Original macro name: Unwind
	"""
	return W - 6.283185308 * math.floor(W / 6.283185308)

def unwind_deg(W):
	"""
	Convert angle in degrees to equivalent angle in the range 0 to 360 degrees.

	Original macro name: UnwindDeg
	"""
	return W - 360 * math.floor(W / 360)

def unwind_rad(W):
	"""
	Convert angle in radians to equivalent angle in degrees.

	Original macro name: UnwindRad
	"""
	return W - 6.283185308 * math.floor(W / 6.283185308)

def moon_long(LH,LM,LS,DS,ZC,DY,MN,YR):
	"""
	Calculate geocentric ecliptic longitude for the Moon
	
	Original macro name: MoonLong
	"""
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	L = 6.28875 * math.sin(MD) + 1.274018 * math.sin(2 * ME1 - MD)
	L = L + 0.658309 * math.sin(2 * ME1) + 0.213616 * math.sin(2 * MD)
	L = L - E * 0.185596 * math.sin(MS) - 0.114336 * math.sin(2 * MF)
	L = L + 0.058793 * math.sin(2 * (ME1 - MD))
	L = L + 0.057212 * E * math.sin(2 * ME1 - MS - MD) + 0.05332 * math.sin(2 * ME1 + MD)
	L = L + 0.045874 * E * math.sin(2 * ME1 - MS) + 0.041024 * E * math.sin(MD - MS)
	L = L - 0.034718 * math.sin(ME1) - E * 0.030465 * math.sin(MS + MD)
	L = L + 0.015326 * math.sin(2 * (ME1 - MF)) - 0.012528 * math.sin(2 * MF + MD)
	L = L - 0.01098 * math.sin(2 * MF - MD) + 0.010674 * math.sin(4 * ME1 - MD)
	L = L + 0.010034 * math.sin(3 * MD) + 0.008548 * math.sin(4 * ME1 - 2 * MD)
	L = L - E * 0.00791 * math.sin(MS - MD + 2 * ME1) - E * 0.006783 * math.sin(2 * ME1 + MS)
	L = L + 0.005162 * math.sin(MD - ME1) + E * 0.005 * math.sin(MS + ME1)
	L = L + 0.003862 * math.sin(4 * ME1) + E * 0.004049 * math.sin(MD - MS + 2 * ME1)
	L = L + 0.003996 * math.sin(2 * (MD + ME1)) + 0.003665 * math.sin(2 * ME1 - 3 * MD)
	L = L + E * 0.002695 * math.sin(2 * MD - MS) + 0.002602 * math.sin(MD - 2 * (MF + ME1))
	L = L + E * 0.002396 * math.sin(2 * (ME1 - MD) - MS) - 0.002349 * math.sin(MD + ME1)
	L = L + E2 * 0.002249 * math.sin(2 * (ME1 - MS)) - E * 0.002125 * math.sin(2 * MD + MS)
	L = L - E2 * 0.002079 * math.sin(2 * MS) + E2 * 0.002059 * math.sin(2 * (ME1 - MS) - MD)
	L = L - 0.001773 * math.sin(MD + 2 * (ME1 - MF)) - 0.001595 * math.sin(2 * (MF + ME1))
	L = L + E * 0.00122 * math.sin(4 * ME1 - MS - MD) - 0.00111 * math.sin(2 * (MD + MF))
	L = L + 0.000892 * math.sin(MD - 3 * ME1) - E * 0.000811 * math.sin(MS + MD + 2 * ME1)
	L = L + E * 0.000761 * math.sin(4 * ME1 - MS - 2 * MD)
	L = L + E2 * 0.000704 * math.sin(MD - 2 * (MS + ME1))
	L = L + E * 0.000693 * math.sin(MS - 2 * (MD - ME1))
	L = L + E * 0.000598 * math.sin(2 * (ME1 - MF) - MS)
	L = L + 0.00055 * math.sin(MD + 4 * ME1) + 0.000538 * math.sin(4 * MD)
	L = L + E * 0.000521 * math.sin(4 * ME1 - MS) + 0.000486 * math.sin(2 * MD - ME1)
	L = L + E2 * 0.000717 * math.sin(MD - 2 * MS)
	MM = unwind(ML + math.radians(L))

	return degrees(MM)

def moon_lat(LH,LM,LS,DS,ZC,DY,MN,YR):
	"""
	Calculate geocentric ecliptic latitude for the Moon
	
	Original macro name: MoonLat
	"""
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	G = 5.128189 * math.sin(MF) + 0.280606 * math.sin(MD + MF)
	G = G + 0.277693 * math.sin(MD - MF) + 0.173238 * math.sin(2 * ME1 - MF)
	G = G + 0.055413 * math.sin(2 * ME1 + MF - MD) + 0.046272 * math.sin(2 * ME1 - MF - MD)
	G = G + 0.032573 * math.sin(2 * ME1 + MF) + 0.017198 * math.sin(2 * MD + MF)
	G = G + 0.009267 * math.sin(2 * ME1 + MD - MF) + 0.008823 * math.sin(2 * MD - MF)
	G = G + E * 0.008247 * math.sin(2 * ME1 - MS - MF) + 0.004323 * math.sin(2 * (ME1 - MD) - MF)
	G = G + 0.0042 * math.sin(2 * ME1 + MF + MD) + E * 0.003372 * math.sin(MF - MS - 2 * ME1)
	G = G + E * 0.002472 * math.sin(2 * ME1 + MF - MS - MD)
	G = G + E * 0.002222 * math.sin(2 * ME1 + MF - MS)
	G = G + E * 0.002072 * math.sin(2 * ME1 - MF - MS - MD)
	G = G + E * 0.001877 * math.sin(MF - MS + MD) + 0.001828 * math.sin(4 * ME1 - MF - MD)
	G = G - E * 0.001803 * math.sin(MF + MS) - 0.00175 * math.sin(3 * MF)
	G = G + E * 0.00157 * math.sin(MD - MS - MF) - 0.001487 * math.sin(MF + ME1)
	G = G - E * 0.001481 * math.sin(MF + MS + MD) + E * 0.001417 * math.sin(MF - MS - MD)
	G = G + E * 0.00135 * math.sin(MF - MS) + 0.00133 * math.sin(MF - ME1)
	G = G + 0.001106 * math.sin(MF + 3 * MD) + 0.00102 * math.sin(4 * ME1 - MF)
	G = G + 0.000833 * math.sin(MF + 4 * ME1 - MD) + 0.000781 * math.sin(MD - 3 * MF)
	G = G + 0.00067 * math.sin(MF + 4 * ME1 - 2 * MD) + 0.000606 * math.sin(2 * ME1 - 3 * MF)
	G = G + 0.000597 * math.sin(2 * (ME1 + MD) - MF)
	G = G + E * 0.000492 * math.sin(2 * ME1 + MD - MS - MF) + 0.00045 * math.sin(2 * (MD - ME1) - MF)
	G = G + 0.000439 * math.sin(3 * MD - MF) + 0.000423 * math.sin(MF + 2 * (ME1 + MD))
	G = G + 0.000422 * math.sin(2 * ME1 - MF - 3 * MD) - E * 0.000367 * math.sin(MS + MF + 2 * ME1 - MD)
	G = G - E * 0.000353 * math.sin(MS + MF + 2 * ME1) + 0.000331 * math.sin(MF + 4 * ME1)
	G = G + E * 0.000317 * math.sin(2 * ME1 + MF - MS + MD)
	G = G + E2 * 0.000306 * math.sin(2 * (ME1 - MS) - MF) - 0.000283 * math.sin(MD + 3 * MF)
	W1 = 0.0004664 * math.cos(NA)
	W2 = 0.0000754 * math.cos(C)
	BM = math.radians(G) * (1 - W1 - W2)

	return degrees(BM)

def moon_hp(LH,LM,LS,DS,ZC,DY,MN,YR):
	"""
	Calculate horizontal parallax for the Moon
	
	Original macro name: MoonHP
	"""
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	PM = 0.950724 + 0.051818 * math.cos(MD) + 0.009531 * math.cos(2 * ME1 - MD)
	PM = PM + 0.007843 * math.cos(2 * ME1) + 0.002824 * math.cos(2 * MD)
	PM = PM + 0.000857 * math.cos(2 * ME1 + MD) + E * 0.000533 * math.cos(2 * ME1 - MS)
	PM = PM + E * 0.000401 * math.cos(2 * ME1 - MD - MS)
	PM = PM + E * 0.00032 * math.cos(MD - MS) - 0.000271 * math.cos(ME1)
	PM = PM - E * 0.000264 * math.cos(MS + MD) - 0.000198 * math.cos(2 * MF - MD)
	PM = PM + 0.000173 * math.cos(3 * MD) + 0.000167 * math.cos(4 * ME1 - MD)
	PM = PM - E * 0.000111 * math.cos(MS) + 0.000103 * math.cos(4 * ME1 - 2 * MD)
	PM = PM - 0.000084 * math.cos(2 * MD - 2 * ME1) - E * 0.000083 * math.cos(2 * ME1 + MS)
	PM = PM + 0.000079 * math.cos(2 * ME1 + 2 * MD) + 0.000072 * math.cos(4 * ME1)
	PM = PM + E * 0.000064 * math.cos(2 * ME1 - MS + MD) - E * 0.000063 * math.cos(2 * ME1 + MS - MD)
	PM = PM + E * 0.000041 * math.cos(MS + ME1) + E * 0.000035 * math.cos(2 * MD - MS)
	PM = PM - 0.000033 * math.cos(3 * MD - 2 * ME1) - 0.00003 * math.cos(MD + ME1)
	PM = PM - 0.000029 * math.cos(2 * (MF - ME1)) - E * 0.000029 * math.cos(2 * MD + MS)
	PM = PM + E2 * 0.000026 * math.cos(2 * (ME1 - MS)) - 0.000023 * math.cos(2 * (MF - ME1) + MD)
	PM = PM + E * 0.000019 * math.cos(4 * ME1 - MS - MD)

	return PM

def moon_dist(LH, LM, LS, DS, ZC, DY, MN, YR):
	"""
	Calculate distance from the Earth to the Moon (km)

	Original macro name: MoonDist
	"""
	HP = math.radians(moon_hp(LH, LM, LS, DS, ZC, DY, MN, YR))
	R = 6378.14 / math.sin(HP)

	return R

def moon_size(LH, LM, LS, DS, ZC, DY, MN, YR):
	"""
	Calculate the Moon's angular diameter (degrees)

	Original macro name: MoonSize
	"""
	HP = math.radians(moon_hp(LH, LM, LS, DS, ZC, DY, MN, YR))
	R = 6378.14 / math.sin(HP)
	TH = 384401 * 0.5181 / R

	return TH

def sun_e_long(GD,GM,GY):
	"""
	Mean ecliptic longitude of the Sun at the epoch
	
	Original macro name: SunElong
	"""
	T = (cd_jd(GD,GM,GY) - 2415020) / 36525
	T2 = T * T
	X = 279.6966778 + 36000.76892 * T + 0.0003025 * T2
	
	return X - 360 * math.floor(X / 360)

def sun_peri(GD,GM,GY):
	"""
	Longitude of the Sun at perigee
	
	Original macro name: SunPeri
	"""
	T = (cd_jd(GD,GM,GY) - 2415020) / 36525
	T2 = T * T
	X = 281.2208444 + 1.719175 * T + 0.000452778 * T2
	
	return X - 360 * math.floor(X / 360)

def sun_ecc(GD,GM,GY):
	"""
	Eccentricity of the Sun-Earth orbit
	
	Original macro name: SunEcc
	"""
	T = (cd_jd(GD,GM,GY) - 2415020) / 36525
	T2 = T * T
	
	return 0.01675104 - 0.0000418 * T - 0.000000126 * T2

def ec_dec(ELD,ELM,ELS,BD,BM,BS,GD,GM,GY):
	"""
	Ecliptic - Declination (degrees)
	
	Original macro name: ECDec
	"""
	A = math.radians(dms_dd(ELD, ELM, ELS))
	B = math.radians(dms_dd(BD, BM, BS))
	C = math.radians(obliq(GD, GM, GY))
	D = math.sin(B) * math.cos(C) + math.cos(B) * math.sin(C) * math.sin(A)
	
	return degrees(math.asin(D))

def ec_ra(ELD,ELM,ELS,BD,BM,BS,GD,GM,GY):
	"""
	Ecliptic - Right Ascension (degrees)
	
	Original macro name: ECRA
	"""
	A = math.radians(dms_dd(ELD, ELM, ELS))
	B = math.radians(dms_dd(BD, BM, BS))
	C = math.radians(obliq(GD, GM, GY))
	D = math.sin(A) * math.cos(C) - math.tan(B) * math.sin(C)
	E = math.cos(A)
	F = degrees(math.atan2(D,E))
	
	return F - 360 * math.floor(F / 360)

def sun_true_anomaly(LCH, LCM, LCS, DS, ZC, LD, LM, LY):
	"""
	Calculate Sun's true anomaly, i.e., how much its orbit deviates from a true circle to an ellipse.
	
	Original macro name: SunTrueAnomaly
	"""
	AA = lct_gday(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	BB = lct_gmonth(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	CC = lct_gyear(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	UT = lct_ut(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	DJ = cd_jd(AA, BB, CC) - 2415020
	
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T
	
	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))

	L = 279.69668 + 0.0003025 * T2 + B
	
	A = 99.99736042 * T
	B = 360 * (A - math.floor(A))

	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	EC = 0.01675104 - 0.0000418 * T - 0.000000126 * T2

	AM = math.radians(M1)

	return degrees(true_anomaly(AM, EC))

def sun_mean_anomaly(LCH, LCM, LCS, DS, ZC, LD, LM, LY):
	"""
	Calculate the Sun's mean anomaly.

	Original macro name: SunMeanAnomaly
	"""
	AA = lct_gday(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	BB = lct_gmonth(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	CC = lct_gyear(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	UT = lct_ut(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	DJ = cd_jd(AA, BB, CC) - 2415020
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T
	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))
	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	AM = unwind(math.radians(M1))

	return AM

def sunrise_lct(LD, LM, LY, DS, ZC, GL, GP):
	"""
	Calculate local civil time of sunrise.

	Original macro name: SunriseLCT
	"""
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = sunrise_lct_l3710(GD,GM,GY,SR,DI,GP)

	if S != "OK":
		XX = -99
	else:
		X = lst_gst(LA, 0, 0, GL)
		UT = gst_ut(X, 0, 0, GD, GM, GY)

		if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
			XX = -99
		else:
			SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
			A,X,Y,LA,S = sunrise_lct_l3710(GD,GM,GY,SR,DI,GP)

			if S != "OK":
				XX = -99
			else:
				X = lst_gst(LA, 0, 0, GL)
				UT = gst_ut(X, 0, 0, GD, GM, GY)
				XX = ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)

	return XX

def sunrise_lct_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for sunrise_lct(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

def sunrise_az(LD, LM, LY, DS, ZC, GL, GP):
	"""
	Calculate azimuth of sunrise.

	Original macro name: SunriseAz
	"""
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = sunrise_az_l3710(GD, GM, GY, SR, DI, GP)
        
	if S != "OK":
		return -99

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return -99

	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	A,X,Y,LA,S = sunrise_az_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99

	return rise_set_azimuth_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
        
def sunrise_az_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for sunrise_az(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

def sunset_az(LD, LM, LY, DS, ZC, GL, GP):
	"""
	Calculate azimuth of sunset.

	Original macro name: SunsetAz
	"""
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = sunset_az_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99
		
	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)
	
	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return -99
		
	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = sunset_az_l3710(GD, GM, GY, SR, DI, GP)
	
	if S != "OK":
		return -99
	
	return rise_set_azimuth_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
        
def sunset_az_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for sunset_az(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

def sunset_lct(LD, LM, LY, DS, ZC, GL, GP):
	"""
	Calculate local civil time of sunset.

	Original macro name: SunsetLCT
	"""
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = sunset_lct_l3710(GD,GM,GY,SR,DI,GP)

	if S != "OK":
		XX = -99
	else:
		X = lst_gst(LA, 0, 0, GL)
		UT = gst_ut(X, 0, 0, GD, GM, GY)

		if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
			XX = -99
		else:
			SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
			A,X,Y,LA,S = sunset_lct_l3710(GD,GM,GY,SR,DI,GP)

			if S != "OK":
				XX = -99
			else:
				X = lst_gst(LA, 0, 0, GL)
				UT = gst_ut(X, 0, 0, GD, GM, GY)
				XX = ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)
	
	return XX

def sunset_lct_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for sunset_lct(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	
	return A,X,Y,LA,S

def e_sun_rs(LD, LM, LY, DS, ZC, GL, GP):
	"""
	Sunrise/Sunset calculation status.

	Original macro name: eSunRS
	"""
	S = ""
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = e_sun_rs_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return S
	else:
		X = lst_gst(LA, 0, 0, GL)
		UT = gst_ut(X, 0, 0, GD, GM, GY)
		SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
		A,X,Y,LA,S = e_sun_rs_l3710(GD, GM, GY, SR, DI, GP)
		if S != "OK":
			return S
		else:
			X = lst_gst(LA, 0, 0, GL)
			UT = gst_ut(X, 0, 0, GD, GM, GY)

			if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
				S = S + " GST to UT conversion warning"
				return S
			
			return S

def e_sun_rs_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for e_sun_rs(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

def angle(XX1, XM1, XS1, DD1, DM1, DS1, XX2, XM2, XS2, DD2, DM2, DS2, S):
	"""
	Calculate the angle between two celestial objects
	
	Original macro name: Angle
	"""
	A = dh_dd(hms_dh(XX1, XM1, XS1)) if (S in ["H","h"]) else dms_dd(XX1, XM1, XD1)
	B = math.radians(A)
	C = dms_dd(DD1, DM1, DS1)
	D = math.radians(C)
	E = dh_dd(hms_dh(XX2, XM2, XS2)) if (S in ["H","h"]) else dms_dd(XX2, XM2, XD2)
	F = math.radians(E)
	G = dms_dd(DD2, DM2, DS2)
	H = math.radians(G)
	I = math.acos(math.sin(D) * math.sin(H) + math.cos(D) * math.cos(H) * math.cos(B - F))

	return degrees(I)

def rise_set_local_sidereal_time_rise(RAH, RAM, RAS, DD, DM, DS, VD, G):
	"""
	Local sidereal time of rise, in hours.

	Original macro name: RSLSTR
	"""
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = -(math.sin(D) + math.sin(E) * math.sin(C)) / (math.cos(E) * math.cos(C))
	H = math.acos(F) if (abs(F) < 1) else 0
	I = dd_dh(degrees(B - H))

	return I - 24 * math.floor(I / 24)

def e_rs(RAH, RAM, RAS, DD, DM, DS, VD, G):
	"""
	Rise/Set status

	Possible values: "OK", "** never rises", "** circumpolar"

	Original macro name: eRS
	"""
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = -(math.sin(D) + math.sin(E) * math.sin(C)) / (math.cos(E) * math.cos(C))

	returnValue = "OK"
	if (F >= 1):
		returnValue = "** never rises"
	if (F <= -1):
		returnValue = "** circumpolar"

	return returnValue

def rise_set_local_sidereal_time_set(RAH, RAM, RAS, DD, DM, DS, VD, G):
	"""
	Local sidereal time of setting, in hours.

	Original macro name: RSLSTS
	"""
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = -(math.sin(D) + math.sin(E) * math.sin(C)) / (math.cos(E) * math.cos(C))
	H = math.acos(F) if (abs(F) < 1) else 0
	I = dd_dh(degrees(B + H))

	return I - 24 * math.floor(I / 24)

def rise_set_azimuth_rise(RAH, RAM, RAS, DD, DM, DS, VD, G):
	"""
	Azimuth of rising, in degrees.
	
	Original macro name: RSAZR
	"""
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = (math.sin(C) + math.sin(D) * math.sin(E)) / (math.cos(D) * math.cos(E))
	H = math.acos(F) if e_rs(RAH, RAM, RAS, DD, DM, DS, VD, G) == "OK" else 0
	I = degrees(H)

	return I - 360 * math.floor(I / 360)

def rise_set_azimuth_set(RAH, RAM, RAS, DD, DM, DS, VD, G):
	"""
	Azimuth of setting, in degrees.

	Original macro name: RSAZS
	"""
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = (math.sin(C) + math.sin(D) * math.sin(E)) / (math.cos(D) * math.cos(E))
	H = math.acos(F) if e_rs(RAH, RAM, RAS, DD, DM, DS, VD, G) == "OK" else 0
	I = 360 - degrees(H)

	return I - 360 * math.floor(I / 360)

def nutat_long(GD, GM, GY):
	"""
	Nutation amount to be added in ecliptic longitude, in degrees.

	Original macro name: NutatLong
	"""
	DJ = cd_jd(GD, GM, GY) - 2415020
	T = DJ / 36525
	T2 = T * T

	A = 100.0021358 * T
	B = 360 * (A - math.floor(A))

	L1 = 279.6967 + 0.000303 * T2 + B
	l2 = 2 * math.radians(L1)

	A = 1336.855231 * T
	B = 360 * (A - math.floor(A))

	D1 = 270.4342 - 0.001133 * T2 + B
	D2 = 2 * math.radians(D1)

	A = 99.99736056 * T
	B = 360 * (A - math.floor(A))

	M1 = 358.4758 - 0.00015 * T2 + B
	M1 = math.radians(M1)

	A = 1325.552359 * T
	B = 360 * (A - math.floor(A))

	M2 = 296.1046 + 0.009192 * T2 + B
	M2 = math.radians(M2)

	A = 5.372616667 * T
	B = 360 * (A - math.floor(A))

	N1 = 259.1833 + 0.002078 * T2 - B
	N1 = math.radians(N1)

	N2 = 2 * N1

	DP = (-17.2327 - 0.01737 * T) * math.sin(N1)
	DP = DP + (-1.2729 - 0.00013 * T) * math.sin(l2) + 0.2088 * math.sin(N2)
	DP = DP - 0.2037 * math.sin(D2) + (0.1261 - 0.00031 * T) * math.sin(M1)
	DP = DP + 0.0675 * math.sin(M2) - (0.0497 - 0.00012 * T) * math.sin(l2 + M1)
	DP = DP - 0.0342 * math.sin(D2 - N1) - 0.0261 * math.sin(D2 + M2)
	DP = DP + 0.0214 * math.sin(l2 - M1) - 0.0149 * math.sin(l2 - D2 + M2)
	DP = DP + 0.0124 * math.sin(l2 - N1) + 0.0114 * math.sin(D2 - M2)

	return DP / 3600

def twilight_am_lct(LD, LM, LY, DS, ZC, GL, GP, TT):
	"""
	Calculate morning twilight start, in local time.

	Twilight type (TT) can be one of "C" (civil), "N" (nautical), or "A" (astronomical)

	Original macro name: TwilightAMLCT
	"""
	DI = 18
	if TT in ["C","c"]:
		DI = 6
	if TT in ["N","n"]:
		DI = 12

	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = twilight_am_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return -99

	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = twilight_am_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	XX = ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)

	return XX

def twilight_am_lct_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for twilight_am_lct(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

def twilight_pm_lct(LD, LM, LY, DS, ZC, GL, GP, TT):
	"""
	Calculate evening twilight end, in local time.

	Twilight type can be one of "C" (civil), "N" (nautical), or "A" (astronomical)

	Original macro name: TwilightPMLCT
	"""
	DI = 18
	if TT in ["C","c"]:
		DI = 6
	if TT in ["N","n"]:
		DI = 12

	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = twilight_pm_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return 0

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return 0

	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = twilight_pm_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return 0

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	return ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)
        
def twilight_pm_lct_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for twilight_pm_lct(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

def e_twilight(LD, LM, LY, DS, ZC, GL, GP, TT):
	"""
	Twilight calculation status.

	Twilight type can be one of "C" (civil), "N" (nautical), or "A" (astronomical)

	Original macro name: eTwilight

	Returns:
		One of: "OK", "** lasts all night", or "** Sun too far below horizon"
	"""
	S = ""

	DI = 18
	if TT in ["C","c"]:
		DI = 6
	if TT in ["N","n"]:
		DI = 12

	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = e_twilight_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return S

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)
	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = e_twilight_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return S

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		S = S + " GST to UT conversion warning"
		return S

	return S
        
def e_twilight_l3710(GD, GM, GY, SR, DI, GP):
	""" Helper function for e_twilight(). """
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	if S.startswith("** c"):
		S = "** lasts all night"
	else:
		if S.startswith("** n"):
			S = "** Sun too far below horizon"
	
	return A,X,Y,LA,S

def planet_coordinates(LH, LM, LS, DS, ZC, DY, MN, YR, S):
	"""
	Calculate several planetary properties.

	Original macro names: PlanetLong, PlanetLat, PlanetDist, PlanetHLong1, PlanetHLong2, PlanetHLat, PlanetRVect

	Arguments:
		LH -- Local civil time, hour part.
		LM -- Local civil time, minutes part.
		LS -- Local civil time, seconds part.
		DS -- Daylight Savings offset.
		ZC -- Time zone correction, in hours.
		DY -- Local date, day part.
		MN -- Local date, month part.
		YR -- Local date, year part.
		S -- Planet name.

	Returns:
		planet_longitude -- Ecliptic longitude, in degrees.
		planet_latitude -- Ecliptic latitude, in degrees.
		planet_distance_au -- Earth-planet distance, in AU.
		planet_h_long1 -- Heliocentric orbital longitude, in degrees.
		planet_h_long2 -- NOT USED
		planet_h_lat -- NOT USED
		planet_r_vect -- Sun-planet distance (length of radius vector), in AU.
	"""
	a11 = 178.179078
	a12 = 415.2057519
	a13 = 0.0003011
	a14 = 0
	a21 = 75.899697
	a22 = 1.5554889
	a23 = 0.0002947
	a24 = 0
	a31 = 0.20561421
	a32 = 0.00002046
	a33 = -0.00000003
	a34 = 0
	a41 = 7.002881
	a42 = 0.0018608
	a43 = -0.0000183
	a44 = 0
	a51 = 47.145944
	a52 = 1.1852083
	a53 = 0.0001739
	a54 = 0
	a61 = 0.3870986
	a62 = 6.74
	a63 = -0.42

	b11 = 342.767053
	b12 = 162.5533664
	b13 = 0.0003097
	b14 = 0
	b21 = 130.163833
	b22 = 1.4080361
	b23 = -0.0009764
	b24 = 0
	b31 = 0.00682069
	b32 = -0.00004774
	b33 = 0.000000091
	b34 = 0
	b41 = 3.393631
	b42 = 0.0010058
	b43 = -0.000001
	b44 = 0
	b51 = 75.779647
	b52 = 0.89985
	b53 = 0.00041
	b54 = 0
	b61 = 0.7233316
	b62 = 16.92
	b63 = -4.4

	c11 = 293.737334
	c12 = 53.17137642
	c13 = 0.0003107
	c14 = 0
	c21 = 334.218203
	c22 = 1.8407584
	c23 = 0.0001299
	c24 = -0.00000119
	c31 = 0.0933129
	c32 = 0.000092064
	c33 = -0.000000077
	c34 = 0
	c41 = 1.850333
	c42 = -0.000675
	c43 = 0.0000126
	c44 = 0
	c51 = 48.786442
	c52 = 0.7709917
	c53 = -0.0000014
	c54 = -0.00000533
	c61 = 1.5236883
	c62 = 9.36
	c63 = -1.52

	d11 = 238.049257
	d12 = 8.434172183
	d13 = 0.0003347
	d14 = -0.00000165
	d21 = 12.720972
	d22 = 1.6099617
	d23 = 0.00105627
	d24 = -0.00000343
	d31 = 0.04833475
	d32 = 0.00016418
	d33 = -0.0000004676
	d34 = -0.0000000017
	d41 = 1.308736
	d42 = -0.0056961
	d43 = 0.0000039
	d44 = 0
	d51 = 99.443414
	d52 = 1.01053
	d53 = 0.00035222
	d54 = -0.00000851
	d61 = 5.202561
	d62 = 196.74
	d63 = -9.4

	e11 = 266.564377
	e12 = 3.398638567
	e13 = 0.0003245
	e14 = -0.0000058
	e21 = 91.098214
	e22 = 1.9584158
	e23 = 0.00082636
	e24 = 0.00000461
	e31 = 0.05589232
	e32 = -0.0003455
	e33 = -0.000000728
	e34 = 0.00000000074
	e41 = 2.492519
	e42 = -0.0039189
	e43 = -0.00001549
	e44 = 0.00000004
	e51 = 112.790414
	e52 = 0.8731951
	e53 = -0.00015218
	e54 = -0.00000531
	e61 = 9.554747
	e62 = 165.6
	e63 = -8.88

	f11 = 244.19747
	f12 = 1.194065406
	f13 = 0.000316
	f14 = -0.0000006
	f21 = 171.548692
	f22 = 1.4844328
	f23 = 0.0002372
	f24 = -0.00000061
	f31 = 0.0463444
	f32 = -0.00002658
	f33 = 0.000000077
	f34 = 0
	f41 = 0.772464
	f42 = 0.0006253
	f43 = 0.0000395
	f44 = 0
	f51 = 73.477111
	f52 = 0.4986678
	f53 = 0.0013117
	f54 = 0
	f61 = 19.21814
	f62 = 65.8
	f63 = -7.19

	g11 = 84.457994
	g12 = 0.6107942056
	g13 = 0.0003205
	g14 = -0.0000006
	g21 = 46.727364
	g22 = 1.4245744
	g23 = 0.00039082
	g24 = -0.000000605
	g31 = 0.00899704
	g32 = 0.00000633
	g33 = -0.000000002
	g34 = 0
	g41 = 1.779242
	g42 = -0.0095436
	g43 = -0.0000091
	g44 = 0
	g51 = 130.681389
	g52 = 1.098935
	g53 = 0.00024987
	g54 = -0.000004718
	g61 = 30.10957
	g62 = 62.2
	g63 = -6.87

	PL = np.empty([8,10])
	AP = np.empty(8)

	IP = 0
	B = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	A = cd_jd(GD, GM, GY)
	T = ((A - 2415020) / 36525) + (B / 876600)

	u_s = S.lower()

	if u_s == "mercury":
		IP = 1
	if u_s == "venus":
		IP = 2
	if u_s == "mars":
		IP = 3
	if u_s == "jupiter":
		IP = 4
	if u_s == "saturn":
		IP = 5
	if u_s == "uranus":
		IP = 6
	if u_s == "neptune":
		IP = 7
	if IP == 0:
		return degrees(unwind(0)), degrees(unwind(0)), degrees(unwind(0)), degrees(unwind(0)), degrees(unwind(0)), degrees(unwind(0)), degrees(unwind(0))

	I = int(1)
	A0 = a11
	A1 = a12
	A2 = a13
	A3 = a14
	B0 = a21
	B1 = a22
	B2 = a23
	B3 = a24
	C0 = a31
	C1 = a32
	C2 = a33
	C3 = a34
	D0 = a41
	D1 = a42
	D2 = a43
	D3 = a44
	E0 = a51
	E1 = a52
	E2 = a53
	E3 = a54
	F = a61
	G = a62
	H = a63
        
	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	I = 2
	A0 = b11
	A1 = b12
	A2 = b13
	A3 = b14
	B0 = b21
	B1 = b22
	B2 = b23
	B3 = b24
	C0 = b31
	C1 = b32
	C2 = b33
	C3 = b34
	D0 = b41
	D1 = b42
	D2 = b43
	D3 = b44
	E0 = b51
	E1 = b52
	E2 = b53
	E3 = b54
	F = b61
	G = b62
	H = b63
        
	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	I = 3
	A0 = c11
	A1 = c12
	A2 = c13
	A3 = c14
	B0 = c21
	B1 = c22
	B2 = c23
	B3 = c24
	C0 = c31
	C1 = c32
	C2 = c33
	C3 = c34
	D0 = c41
	D1 = c42
	D2 = c43
	D3 = c44
	E0 = c51
	E1 = c52
	E2 = c53
	E3 = c54
	F = c61
	G = c62
	H = c63

	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	I = 4
	A0 = d11
	A1 = d12
	A2 = d13
	A3 = d14
	B0 = d21
	B1 = d22
	B2 = d23
	B3 = d24
	C0 = d31
	C1 = d32
	C2 = d33
	C3 = d34
	D0 = d41
	D1 = d42
	D2 = d43
	D3 = d44
	E0 = d51
	E1 = d52
	E2 = d53
	E3 = d54
	F = d61
	G = d62
	H = d63

	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	I = 5
	A0 = e11
	A1 = e12
	A2 = e13
	A3 = e14
	B0 = e21
	B1 = e22
	B2 = e23
	B3 = e24
	C0 = e31
	C1 = e32
	C2 = e33
	C3 = e34
	D0 = e41
	D1 = e42
	D2 = e43
	D3 = e44
	E0 = e51
	E1 = e52
	E2 = e53
	E3 = e54
	F = e61
	G = e62
	H = e63

	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	I = 6
	A0 = f11
	A1 = f12
	A2 = f13
	A3 = f14
	B0 = f21
	B1 = f22
	B2 = f23
	B3 = f24
	C0 = f31
	C1 = f32
	C2 = f33
	C3 = f34
	D0 = f41
	D1 = f42
	D2 = f43
	D3 = f44
	E0 = f51
	E1 = f52
	E2 = f53
	E3 = f54
	F = f61
	G = f62
	H = f63

	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	I = 7
	A0 = g11
	A1 = g12
	A2 = g13
	A3 = g14
	B0 = g21
	B1 = g22
	B2 = g23
	B3 = g24
	C0 = g31
	C1 = g32
	C2 = g33
	C3 = g34
	D0 = g41
	D1 = g42
	D2 = g43
	D3 = g44
	E0 = g51
	E1 = g52
	E2 = g53
	E3 = g54
	F = g61
	G = g62
	H = g63

	AA = A1 * T
	B = 360 * (AA - math.floor(AA))
	C = A0 + B + (A3 * T + A2) * T * T
	PL[I, 1] = C - 360 * math.floor(C / 360)
	PL[I, 2] = (A1 * 0.009856263) + (A2 + A3) / 36525
	PL[I, 3] = ((B3 * T + B2) * T + B1) * T + B0
	PL[I, 4] = ((C3 * T + C2) * T + C1) * T + C0
	PL[I, 5] = ((D3 * T + D2) * T + D1) * T + D0
	PL[I, 6] = ((E3 * T + E2) * T + E1) * T + E0
	PL[I, 7] = F
	PL[I, 8] = G
	PL[I, 9] = H

	LI = 0
	TP = 2 * math.pi
	MS = sun_mean_anomaly(LH, LM, LS, DS, ZC, DY, MN, YR)
	SR = math.radians(sun_long(LH, LM, LS, DS, ZC, DY, MN, YR))
	RE = sun_dist(LH, LM, LS, DS, ZC, DY, MN, YR)
	LG = SR + math.pi

	for K in range(1,3):
		for J in range(1,8):
			AP[J] = math.radians(PL[J, 1] - PL[J, 3] - LI * PL[J, 2])
			
		QA = 0
		QB = 0
		QC = 0
		QD = 0
		QE = 0
		QF = 0
		QG = 0

		if IP == 1:
			QA,QB = planet_long_l4685(AP)
		if IP == 2:
			QA,QB,QC,QE = planet_long_l4735(AP,MS,T)
		if IP == 3:
			A,SA,CA,QC,QE,QA,QB = planet_long_l4810(AP,MS)
		if IP in (4,5,6,7):
			QA,QB,QC,QD,QE,QF,QG = planet_long_l4945(T,IP,PL)
		
		EC = PL[IP, 4] + QD
		AM = AP[IP] + QE
		AT = true_anomaly(AM, EC)
		PVV = (PL[IP, 7] + QF) * (1 - EC * EC) / (1 + EC * math.cos(AT))
		LP = degrees(AT) + PL[IP, 3] + degrees(QC - QE)
		LP = math.radians(LP)
		OM = math.radians(PL[IP, 6])
		LO = LP - OM
		SO = math.sin(LO)
		CO = math.cos(LO)
		INN = math.radians(PL[IP, 5])
		PVV = PVV + QB
		SP = SO * math.sin(INN)
		Y = SO * math.cos(INN)
		PS = math.asin(SP) + QG
		SP = math.sin(PS)
		PD = math.atan2(Y, CO) + OM + math.radians(QA)
		PD = unwind(PD)
		CI = math.cos(PS)
		RD = PVV * CI
		LL = PD - LG
		RH = RE * RE + PVV * PVV - 2 * RE * PVV * CI * math.cos(LL)
		RH = math.sqrt(RH)
		LI = RH * 0.005775518
		
		if K == 1:
			L0 = PD
			V0 = RH
			S0 = PS
			P0 = PVV
			VO = RH
			LP1 = LP

	L1 = math.sin(LL)
	l2 = math.cos(LL)

	if IP < 3:
		EP = math.atan(-1 * RD * L1 / (RE - RD * l2)) + LG + math.pi
	else:
		EP = math.atan(RE * L1 / (RD - RE * l2)) + PD

	EP = unwind(EP)
	BP = math.atan(RD * SP * math.sin(EP - PD) / (CI * RE * L1))

	planet_longitude = degrees(unwind(EP))
	planet_latitude = degrees(unwind(BP))
	planet_distance_au = VO
	planet_h_long1 = degrees(LP1)
	planet_h_long2 = degrees(L0)
	planet_h_lat = degrees(S0)
	planet_r_vect = P0

	return planet_longitude, planet_latitude, planet_distance_au, planet_h_long1, planet_h_long2, planet_h_lat, planet_r_vect

def planet_long_l4685(AP):
	""" Helper function for planet_long_lat() """
	QA = 0.00204 * math.cos(5 * AP[2] - 2 * AP[1] + 0.21328)
	QA = QA + 0.00103 * math.cos(2 * AP[2] - AP[1] - 2.8046)
	QA = QA + 0.00091 * math.cos(2 * AP[4] - AP[1] - 0.64582)
	QA = QA + 0.00078 * math.cos(5 * AP[2] - 3 * AP[1] + 0.17692)

	QB = 0.000007525 * math.cos(2 * AP[4] - AP[1] + 0.925251)
	QB = QB + 0.000006802 * math.cos(5 * AP[2] - 3 * AP[1] - 4.53642)
	QB = QB + 0.000005457 * math.cos(2 * AP[2] - 2 * AP[1] - 1.24246)
	QB = QB + 0.000003569 * math.cos(5 * AP[2] - AP[1] - 1.35699)

	return QA,QA

def planet_long_l4735(AP,MS,T):
	""" Helper function for planet_long_lat() """
	QC = 0.00077 * math.sin(4.1406 + T * 2.6227)
	QC = math.radians(QC)
	QE = QC

	QA = 0.00313 * math.cos(2 * MS - 2 * AP[2] - 2.587)
	QA = QA + 0.00198 * math.cos(3 * MS - 3 * AP[2] + 0.044768)
	QA = QA + 0.00136 * math.cos(MS - AP[2] - 2.0788)
	QA = QA + 0.00096 * math.cos(3 * MS - 2 * AP[2] - 2.3721)
	QA = QA + 0.00082 * math.cos(AP[4] - AP[2] - 3.6318)

	QB = 0.000022501 * math.cos(2 * MS - 2 * AP[2] - 1.01592)
	QB = QB + 0.000019045 * math.cos(3 * MS - 3 * AP[2] + 1.61577)
	QB = QB + 0.000006887 * math.cos(AP[4] - AP[2] - 2.06106)
	QB = QB + 0.000005172 * math.cos(MS - AP[2] - 0.508065)
	QB = QB + 0.00000362 * math.cos(5 * MS - 4 * AP[2] - 1.81877)
	QB = QB + 0.000003283 * math.cos(4 * MS - 4 * AP[2] + 1.10851)
	QB = QB + 0.000003074 * math.cos(2 * AP[4] - 2 * AP[2] - 0.962846)

	return QA,QB,QC,QE

def planet_long_l4810(AP,MS):
	""" Helper function for planet_long_lat() """
	A = 3 * AP[4] - 8 * AP[3] + 4 * MS
	SA = math.sin(A)
	CA = math.cos(A)
	QC = -(0.01133 * SA + 0.00933 * CA)
	QC = math.radians(QC)
	QE = QC

	QA = 0.00705 * math.cos(AP[4] - AP[3] - 0.85448)
	QA = QA + 0.00607 * math.cos(2 * AP[4] - AP[3] - 3.2873)
	QA = QA + 0.00445 * math.cos(2 * AP[4] - 2 * AP[3] - 3.3492)
	QA = QA + 0.00388 * math.cos(MS - 2 * AP[3] + 0.35771)
	QA = QA + 0.00238 * math.cos(MS - AP[3] + 0.61256)
	QA = QA + 0.00204 * math.cos(2 * MS - 3 * AP[3] + 2.7688)
	QA = QA + 0.00177 * math.cos(3 * AP[3] - AP[2] - 1.0053)
	QA = QA + 0.00136 * math.cos(2 * MS - 4 * AP[3] + 2.6894)
	QA = QA + 0.00104 * math.cos(AP[4] + 0.30749)

	QB = 0.000053227 * math.cos(AP[4] - AP[3] + 0.717864)
	QB = QB + 0.000050989 * math.cos(2 * AP[4] - 2 * AP[3] - 1.77997)
	QB = QB + 0.000038278 * math.cos(2 * AP[4] - AP[3] - 1.71617)
	QB = QB + 0.000015996 * math.cos(MS - AP[3] - 0.969618)
	QB = QB + 0.000014764 * math.cos(2 * MS - 3 * AP[3] + 1.19768)
	QB = QB + 0.000008966 * math.cos(AP[4] - 2 * AP[3] + 0.761225)
	QB = QB + 0.000007914 * math.cos(3 * AP[4] - 2 * AP[3] - 2.43887)
	QB = QB + 0.000007004 * math.cos(2 * AP[4] - 3 * AP[3] - 1.79573)
	QB = QB + 0.00000662 * math.cos(MS - 2 * AP[3] + 1.97575)
	QB = QB + 0.00000493 * math.cos(3 * AP[4] - 3 * AP[3] - 1.33069)
	QB = QB + 0.000004693 * math.cos(3 * MS - 5 * AP[3] + 3.32665)
	QB = QB + 0.000004571 * math.cos(2 * MS - 4 * AP[3] + 4.27086)
	QB = QB + 0.000004409 * math.cos(3 * AP[4] - AP[3] - 2.02158)

	return A,SA,CA,QC,QE,QA,QB

def planet_long_l4945(T,IP,PL):
	""" Helper function for planet_long_lat() """
	QA = 0
	QB = 0
	QC = 0
	QD = 0
	QE = 0
	QF = 0
	QG = 0

	J1 = T / 5 + 0.1
	J2 = unwind(4.14473 + 52.9691 * T)
	J3 = unwind(4.641118 + 21.32991 * T)
	J4 = unwind(4.250177 + 7.478172 * T)
	J5 = 5 * J3 - 2 * J2
	J6 = 2 * J2 - 6 * J3 + 3 * J4

	if IP in (1,2,3,8):
		return QA,QB,QC,QD,QE,QF,QG
	if IP in (4,5):
		J7 = J3 - J2
		U1 = math.sin(J3)
		U2 = math.cos(J3)
		U3 = math.sin(2 * J3)
		U4 = math.cos(2 * J3)
		U5 = math.sin(J5)
		U6 = math.cos(J5)
		U7 = math.sin(2 * J5)
		U8 = math.sin(J6)
		U9 = math.sin(J7)
		UA = math.cos(J7)
		UB = math.sin(2 * J7)
		UC = math.cos(2 * J7)
		UD = math.sin(3 * J7)
		UE = math.cos(3 * J7)
		UF = math.sin(4 * J7)
		UG = math.cos(4 * J7)
		VH = math.cos(5 * J7)

		if IP == 5:
			UI = math.sin(3 * J3)
			UJ = math.cos(3 * J3)
			UK = math.sin(4 * J3)
			UL = math.cos(4 * J3)
			VI = math.cos(2 * J5)
			UN = math.sin(5 * J7)
			J8 = J4 - J3
			UO = math.sin(2 * J8)
			UP = math.cos(2 * J8)
			UQ = math.sin(3 * J8)
			UR = math.cos(3 * J8)

			QC = 0.007581 * U7 - 0.007986 * U8 - 0.148811 * U9
			QC = QC - (0.814181 - (0.01815 - 0.016714 * J1) * J1) * U5
			QC = QC - (0.010497 - (0.160906 - 0.0041 * J1) * J1) * U6
			QC = QC - 0.015208 * UD - 0.006339 * UF - 0.006244 * U1
			QC = QC - 0.0165 * UB * U1 - 0.040786 * UB
			QC = QC + (0.008931 + 0.002728 * J1) * U9 * U1 - 0.005775 * UD * U1
			QC = QC + (0.081344 + 0.003206 * J1) * UA * U1 + 0.015019 * UC * U1
			QC = QC + (0.085581 + 0.002494 * J1) * U9 * U2 + 0.014394 * UC * U2
			QC = QC + (0.025328 - 0.003117 * J1) * UA * U2 + 0.006319 * UE * U2
			QC = QC + 0.006369 * U9 * U3 + 0.009156 * UB * U3 + 0.007525 * UQ * U3
			QC = QC - 0.005236 * UA * U4 - 0.007736 * UC * U4 - 0.007528 * UR * U4
			QC = math.radians(QC)

			QD = (-7927 + (2548 + 91 * J1) * J1) * U5
			QD = QD + (13381 + (1226 - 253 * J1) * J1) * U6 + (248 - 121 * J1) * U7
			QD = QD - (305 + 91 * J1) * VI + 412 * UB + 12415 * U1
			QD = QD + (390 - 617 * J1) * U9 * U1 + (165 - 204 * J1) * UB * U1
			QD = QD + 26599 * UA * U1 - 4687 * UC * U1 - 1870 * UE * U1 - 821 * UG * U1
			QD = QD - 377 * VH * U1 + 497 * UP * U1 + (163 - 611 * J1) * U2
			QD = QD - 12696 * U9 * U2 - 4200 * UB * U2 - 1503 * UD * U2 - 619 * UF * U2
			QD = QD - 268 * UN * U2 - (282 + 1306 * J1) * UA * U2
			QD = QD + (-86 + 230 * J1) * UC * U2 + 461 * UO * U2 - 350 * U3
			QD = QD + (2211 - 286 * J1) * U9 * U3 - 2208 * UB * U3 - 568 * UD * U3
			QD = QD - 346 * UF * U3 - (2780 + 222 * J1) * UA * U3
			QD = QD + (2022 + 263 * J1) * UC * U3 + 248 * UE * U3 + 242 * UQ * U3
			QD = QD + 467 * UR * U3 - 490 * U4 - (2842 + 279 * J1) * U9 * U4
			QD = QD + (128 + 226 * J1) * UB * U4 + 224 * UD * U4
			QD = QD + (-1594 + 282 * J1) * UA * U4 + (2162 - 207 * J1) * UC * U4
			QD = QD + 561 * UE * U4 + 343 * UG * U4 + 469 * UQ * U4 - 242 * UR * U4
			QD = QD - 205 * U9 * UI + 262 * UD * UI + 208 * UA * UJ - 271 * UE * UJ
			QD = QD - 382 * UE * UK - 376 * UD * UL
			QD = QD * 0.0000001

			VK = (0.077108 + (0.007186 - 0.001533 * J1) * J1) * U5
			VK = VK - 0.007075 * U9
			VK = VK + (0.045803 - (0.014766 + 0.000536 * J1) * J1) * U6
			VK = VK - 0.072586 * U2 - 0.075825 * U9 * U1 - 0.024839 * UB * U1
			VK = VK - 0.008631 * UD * U1 - 0.150383 * UA * U2
			VK = VK + 0.026897 * UC * U2 + 0.010053 * UE * U2
			VK = VK - (0.013597 + 0.001719 * J1) * U9 * U3 + 0.011981 * UB * U4
			VK = VK - (0.007742 - 0.001517 * J1) * UA * U3
			VK = VK + (0.013586 - 0.001375 * J1) * UC * U3
			VK = VK - (0.013667 - 0.001239 * J1) * U9 * U4
			VK = VK + (0.014861 + 0.001136 * J1) * UA * U4
			VK = VK - (0.013064 + 0.001628 * J1) * UC * U4
			QE = QC - (math.radians(VK) / PL[IP, 4])

			QF = 572 * U5 - 1590 * UB * U2 + 2933 * U6 - 647 * UD * U2
			QF = QF + 33629 * UA - 344 * UF * U2 - 3081 * UC + 2885 * UA * U2
			QF = QF - 1423 * UE + (2172 + 102 * J1) * UC * U2 - 671 * UG
			QF = QF + 296 * UE * U2 - 320 * VH - 267 * UB * U3 + 1098 * U1
			QF = QF - 778 * UA * U3 - 2812 * U9 * U1 + 495 * UC * U3 + 688 * UB * U1
			QF = QF + 250 * UE * U3 - 393 * UD * U1 - 856 * U9 * U4 - 228 * UF * U1
			QF = QF + 441 * UB * U4 + 2138 * UA * U1 + 296 * UC * U4 - 999 * UC * U1
			QF = QF + 211 * UE * U4 - 642 * UE * U1 - 427 * U9 * UI - 325 * UG * U1
			QF = QF + 398 * UD * UI - 890 * U2 + 344 * UA * UJ + 2206 * U9 * U2
			QF = QF - 427 * UE * UJ
			QF = QF * 0.000001

			QG = 0.000747 * UA * U1 + 0.001069 * UA * U2 + 0.002108 * UB * U3
			QG = QG + 0.001261 * UC * U3 + 0.001236 * UB * U4 - 0.002075 * UC * U4
			QG = math.radians(QG)

			return QA,QB,QC,QD,QE,QF,QG

		QC = (0.331364 - (0.010281 + 0.004692 * J1) * J1) * U5
		QC = QC + (0.003228 - (0.064436 - 0.002075 * J1) * J1) * U6
		QC = QC - (0.003083 + (0.000275 - 0.000489 * J1) * J1) * U7
		QC = QC + 0.002472 * U8 + 0.013619 * U9 + 0.018472 * UB
		QC = QC + 0.006717 * UD + 0.002775 * UF + 0.006417 * UB * U1
		QC = QC + (0.007275 - 0.001253 * J1) * U9 * U1 + 0.002439 * UD * U1
		QC = QC - (0.035681 + 0.001208 * J1) * U9 * U2 - 0.003767 * UC * U1
		QC = QC - (0.033839 + 0.001125 * J1) * UA * U1 - 0.004261 * UB * U2
		QC = QC + (0.001161 * J1 - 0.006333) * UA * U2 + 0.002178 * U2
		QC = QC - 0.006675 * UC * U2 - 0.002664 * UE * U2 - 0.002572 * U9 * U3
		QC = QC - 0.003567 * UB * U3 + 0.002094 * UA * U4 + 0.003342 * UC * U4
		QC = math.radians(QC)

		QD = (3606 + (130 - 43 * J1) * J1) * U5 + (1289 - 580 * J1) * U6
		QD = QD - 6764 * U9 * U1 - 1110 * UB * U1 - 224 * UD * U1 - 204 * U1
		QD = QD + (1284 + 116 * J1) * UA * U1 + 188 * UC * U1
		QD = QD + (1460 + 130 * J1) * U9 * U2 + 224 * UB * U2 - 817 * U2
		QD = QD + 6074 * U2 * UA + 992 * UC * U2 + 508 * UE * U2 + 230 * UG * U2
		QD = QD + 108 * VH * U2 - (956 + 73 * J1) * U9 * U3 + 448 * UB * U3
		QD = QD + 137 * UD * U3 + (108 * J1 - 997) * UA * U3 + 480 * UC * U3
		QD = QD + 148 * UE * U3 + (99 * J1 - 956) * U9 * U4 + 490 * UB * U4
		QD = QD + 158 * UD * U4 + 179 * U4 + (1024 + 75 * J1) * UA * U4
		QD = QD - 437 * UC * U4 - 132 * UE * U4
		QD = QD * 0.0000001

		VK = (0.007192 - 0.003147 * J1) * U5 - 0.004344 * U1
		VK = VK + (J1 * (0.000197 * J1 - 0.000675) - 0.020428) * U6
		VK = VK + 0.034036 * UA * U1 + (0.007269 + 0.000672 * J1) * U9 * U1
		VK = VK + 0.005614 * UC * U1 + 0.002964 * UE * U1 + 0.037761 * U9 * U2
		VK = VK + 0.006158 * UB * U2 - 0.006603 * UA * U2 - 0.005356 * U9 * U3
		VK = VK + 0.002722 * UB * U3 + 0.004483 * UA * U3
		VK = VK - 0.002642 * UC * U3 + 0.004403 * U9 * U4
		VK = VK - 0.002536 * UB * U4 + 0.005547 * UA * U4 - 0.002689 * UC * U4
		QE = QC - (math.radians(VK) / PL[IP, 4])

		QF = 205 * UA - 263 * U6 + 693 * UC + 312 * UE + 147 * UG + 299 * U9 * U1
		QF = QF + 181 * UC * U1 + 204 * UB * U2 + 111 * UD * U2 - 337 * UA * U2
		QF = QF - 111 * UC * U2
		QF = QF * 0.000001

		return QA,QB,QC,QD,QE,QF,QG

	if IP in (6,7):
		J8 = unwind(1.46205 + 3.81337 * T)
		J9 = 2 * J8 - J4
		VJ = math.sin(J9)
		UU = math.cos(J9)
		UV = math.sin(2 * J9)
		UW = math.cos(2 * J9)

		if IP == 7:
			JA = J8 - J2
			JB = J8 - J3
			JC = J8 - J4
			QC = (0.001089 * J1 - 0.589833) * VJ
			QC = QC + (0.004658 * J1 - 0.056094) * UU - 0.024286 * UV
			QC = math.radians(QC)

			VK = 0.024039 * VJ - 0.025303 * UU + 0.006206 * UV
			VK = VK - 0.005992 * UW
			QE = QC - (math.radians(VK) / PL[IP, 4])

			QD = 4389 * VJ + 1129 * UV + 4262 * UU + 1089 * UW
			QD = QD * 0.0000001

			QF = 8189 * UU - 817 * VJ + 781 * UW
			QF = QF * 0.000001

			VD = math.sin(2 * JC)
			VE = math.cos(2 * JC)
			VF = math.sin(J8)
			VG = math.cos(J8)
			QA = -0.009556 * math.sin(JA) - 0.005178 * math.sin(JB)
			QA = QA + 0.002572 * VD - 0.002972 * VE * VF - 0.002833 * VD * VG

			QG = 0.000336 * VE * VF + 0.000364 * VD * VG
			QG = math.radians(QG)

			QB = -40596 + 4992 * math.cos(JA) + 2744 * math.cos(JB)
			QB = QB + 2044 * math.cos(JC) + 1051 * VE
			QB = QB * 0.000001

			return QA,QB,QC,QD,QE,QF,QG

		JA = J4 - J2
		JB = J4 - J3
		JC = J8 - J4
		QC = (0.864319 - 0.001583 * J1) * VJ
		QC = QC + (0.082222 - 0.006833 * J1) * UU + 0.036017 * UV
		QC = QC - 0.003019 * UW + 0.008122 * math.sin(J6)
		QC = math.radians(QC)

		VK = 0.120303 * VJ + 0.006197 * UV
		VK = VK + (0.019472 - 0.000947 * J1) * UU
		QE = QC - (math.radians(VK) / PL[IP, 4])

		QD = (163 * J1 - 3349) * VJ + 20981 * UU + 1311 * UW
		QD = QD * 0.0000001

		QF = -0.003825 * UU

		QA = (-0.038581 + (0.002031 - 0.00191 * J1) * J1) * math.cos(J4 + JB)
		QA = QA + (0.010122 - 0.000988 * J1) * math.sin(J4 + JB)
		A = (0.034964 - (0.001038 - 0.000868 * J1) * J1) * math.cos(2 * J4 + JB)
		QA = A + QA + 0.005594 * math.sin(J4 + 3 * JC) - 0.014808 * math.sin(JA)
		QA = QA - 0.005794 * math.sin(JB) + 0.002347 * math.cos(JB)
		QA = QA + 0.009872 * math.sin(JC) + 0.008803 * math.sin(2 * JC)
		QA = QA - 0.004308 * math.sin(3 * JC)

		UX = math.sin(JB)
		UY = math.cos(JB)
		UZ = math.sin(J4)
		VA = math.cos(J4)
		VB = math.sin(2 * J4)
		VC = math.cos(2 * J4)
		QG = (0.000458 * UX - 0.000642 * UY - 0.000517 * math.cos(4 * JC)) * UZ
		QG = QG - (0.000347 * UX + 0.000853 * UY + 0.000517 * math.sin(4 * JB)) * VA
		QG = QG + 0.000403 * (math.cos(2 * JC) * VB + math.sin(2 * JC) * VC)
		QG = math.radians(QG)

		QB = -25948 + 4985 * math.cos(JA) - 1230 * VA + 3354 * UY
		QB = QB + 904 * math.cos(2 * JC) + 894 * (math.cos(JC) - math.cos(3 * JC))
		QB = QB + (5795 * VA - 1165 * UZ + 1388 * VC) * UX
		QB = QB + (1351 * VA + 5702 * UZ + 1388 * VB) * UY
		QB = QB * 0.000001
		
		return QA,QB,QC,QD,QE,QF,QG

def solve_cubic(W):
	"""
	For W, in radians, return S, also in radians.

	Original macro name: SolveCubic
	"""
	S = W / 3

	while 1 == 1:
		S2 = S * S
		D = (S2 + 3) * S - W

		if abs(D) < 0.000001:
			return S

		S = ((2 * S * S2) + W) / (3 * (S2 + 1))

def p_comet_long_lat_dist(LH, LM, LS, DS, ZC, DY, MN, YR, TD, TM, TY, Q, I, P, N):
	"""
	Calculate longitude, latitude, and distance of parabolic-orbit comet.

	Original macro names: PcometLong, PcometLat, PcometDist

	Arguments:
		LH -- Local civil time, hour part.
		LM -- Local civil time, minutes part.
		LS -- Local civil time, seconds part.
		DS -- Daylight Savings offset.
		ZC -- Time zone correction, in hours.
		DY -- Local date, day part.
		MN -- Local date, month part.
		YR -- Local date, year part.
		TD -- Perihelion epoch (day)
		TM -- Perihelion epoch (month)
		TY -- Perihelion epoch (year)
		Q -- q (AU)
		I -- Inclination (degrees)
		P -- Perihelion (degrees)
		N -- Node (degrees)

	Returns:
		comet_long_deg -- Comet longitude (degrees)
		comet_lat_deg -- Comet lat (degrees)
		comet_dist_au -- Comet distance from Earth (AU)
	"""
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	TPE = (UT / 365.242191) + cd_jd(GD, GM, GY) - cd_jd(TD, TM, TY)
	LG = math.radians(sun_long(LH, LM, LS, DS, ZC, DY, MN, YR) + 180)
	RE = sun_dist(LH, LM, LS, DS, ZC, DY, MN, YR)

	LI = 0
	for K in range(1,3):
		S = solve_cubic(0.0364911624 * TPE / (Q * math.sqrt(Q)))
		NU = 2 * math.atan(S)
		R = Q * (1 + S * S)
		L = NU + math.radians(P)
		S1 = math.sin(L)
		C1 = math.cos(L)
		I1 = math.radians(I)
		S2 = S1 * math.sin(I1)
		PS = math.asin(S2)
		Y = S1 * math.cos(I1)
		LC = math.atan2(Y, C1) + math.radians(N)
		C2 = math.cos(PS)
		RD = R * C2
		LL = LC - LG
		C3 = math.cos(LL)
		S3 = math.sin(LL)
		RH = math.sqrt((RE * RE) + (R * R) - (2 * RE * RD * C3 * math.cos(PS)))
		if K == 1:
			RH2 = math.sqrt((RE * RE) + (R * R) - (2 * RE * R * math.cos(PS) * math.cos(L + math.radians(N) - LG)))

		LI = RH * 0.005775518

	if RD < RE:
		EP = math.atan((-RD * S3) / (RE - (RD * C3))) + LG + 3.141592654
	else:
		EP = math.atan((RE * S3) / (RD - (RE * C3))) + LC

	EP = unwind(EP)
	TB = (RD * S2 * math.sin(EP - LC)) / (C2 * RE * S3)
	BP = math.atan(TB)

	comet_long_deg = degrees(EP)
	comet_lat_deg = degrees(BP)
	comet_dist_au = RH2

	return comet_long_deg, comet_lat_deg, comet_dist_au

def moon_long_lat_hp(LH, LM, LS, DS, ZC, DY, MN, YR):
	"""
	Calculate longitude, latitude, and horizontal parallax of the Moon.

	Original macro names: MoonLong, MoonLat, MoonHP

	Arguments:
		LH -- Local civil time, hour part.
		LM -- Local civil time, minutes part.
		LS -- Local civil time, seconds part.
		DS -- Daylight Savings offset.
		ZC -- Time zone correction, in hours.
		DY -- Local date, day part.
		MN -- Local date, month part.
		YR -- Local date, year part.

	Returns:
		moon_long_deg -- Moon longitude (degrees)
		moon_lat_deg -- Moon latitude (degrees)
		moon_hor_para -- Moon horizontal parallax (degrees)
	"""
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	# Longitude-specific
	L = 6.28875 * math.sin(MD) + 1.274018 * math.sin(2 * ME1 - MD)
	L = L + 0.658309 * math.sin(2 * ME1) + 0.213616 * math.sin(2 * MD)
	L = L - E * 0.185596 * math.sin(MS) - 0.114336 * math.sin(2 * MF)
	L = L + 0.058793 * math.sin(2 * (ME1 - MD))
	L = L + 0.057212 * E * math.sin(2 * ME1 - MS - MD) + 0.05332 * math.sin(2 * ME1 + MD)
	L = L + 0.045874 * E * math.sin(2 * ME1 - MS) + 0.041024 * E * math.sin(MD - MS)
	L = L - 0.034718 * math.sin(ME1) - E * 0.030465 * math.sin(MS + MD)
	L = L + 0.015326 * math.sin(2 * (ME1 - MF)) - 0.012528 * math.sin(2 * MF + MD)
	L = L - 0.01098 * math.sin(2 * MF - MD) + 0.010674 * math.sin(4 * ME1 - MD)
	L = L + 0.010034 * math.sin(3 * MD) + 0.008548 * math.sin(4 * ME1 - 2 * MD)
	L = L - E * 0.00791 * math.sin(MS - MD + 2 * ME1) - E * 0.006783 * math.sin(2 * ME1 + MS)
	L = L + 0.005162 * math.sin(MD - ME1) + E * 0.005 * math.sin(MS + ME1)
	L = L + 0.003862 * math.sin(4 * ME1) + E * 0.004049 * math.sin(MD - MS + 2 * ME1)
	L = L + 0.003996 * math.sin(2 * (MD + ME1)) + 0.003665 * math.sin(2 * ME1 - 3 * MD)
	L = L + E * 0.002695 * math.sin(2 * MD - MS) + 0.002602 * math.sin(MD - 2 * (MF + ME1))
	L = L + E * 0.002396 * math.sin(2 * (ME1 - MD) - MS) - 0.002349 * math.sin(MD + ME1)
	L = L + E2 * 0.002249 * math.sin(2 * (ME1 - MS)) - E * 0.002125 * math.sin(2 * MD + MS)
	L = L - E2 * 0.002079 * math.sin(2 * MS) + E2 * 0.002059 * math.sin(2 * (ME1 - MS) - MD)
	L = L - 0.001773 * math.sin(MD + 2 * (ME1 - MF)) - 0.001595 * math.sin(2 * (MF + ME1))
	L = L + E * 0.00122 * math.sin(4 * ME1 - MS - MD) - 0.00111 * math.sin(2 * (MD + MF))
	L = L + 0.000892 * math.sin(MD - 3 * ME1) - E * 0.000811 * math.sin(MS + MD + 2 * ME1)
	L = L + E * 0.000761 * math.sin(4 * ME1 - MS - 2 * MD)
	L = L + E2 * 0.000704 * math.sin(MD - 2 * (MS + ME1))
	L = L + E * 0.000693 * math.sin(MS - 2 * (MD - ME1))
	L = L + E * 0.000598 * math.sin(2 * (ME1 - MF) - MS)
	L = L + 0.00055 * math.sin(MD + 4 * ME1) + 0.000538 * math.sin(4 * MD)
	L = L + E * 0.000521 * math.sin(4 * ME1 - MS) + 0.000486 * math.sin(2 * MD - ME1)
	L = L + E2 * 0.000717 * math.sin(MD - 2 * MS)
	MM = unwind(ML + math.radians(L))

	# Latitude-specific
	G = 5.128189 * math.sin(MF) + 0.280606 * math.sin(MD + MF)
	G = G + 0.277693 * math.sin(MD - MF) + 0.173238 * math.sin(2 * ME1 - MF)
	G = G + 0.055413 * math.sin(2 * ME1 + MF - MD) + 0.046272 * math.sin(2 * ME1 - MF - MD)
	G = G + 0.032573 * math.sin(2 * ME1 + MF) + 0.017198 * math.sin(2 * MD + MF)
	G = G + 0.009267 * math.sin(2 * ME1 + MD - MF) + 0.008823 * math.sin(2 * MD - MF)
	G = G + E * 0.008247 * math.sin(2 * ME1 - MS - MF) + 0.004323 * math.sin(2 * (ME1 - MD) - MF)
	G = G + 0.0042 * math.sin(2 * ME1 + MF + MD) + E * 0.003372 * math.sin(MF - MS - 2 * ME1)
	G = G + E * 0.002472 * math.sin(2 * ME1 + MF - MS - MD)
	G = G + E * 0.002222 * math.sin(2 * ME1 + MF - MS)
	G = G + E * 0.002072 * math.sin(2 * ME1 - MF - MS - MD)
	G = G + E * 0.001877 * math.sin(MF - MS + MD) + 0.001828 * math.sin(4 * ME1 - MF - MD)
	G = G - E * 0.001803 * math.sin(MF + MS) - 0.00175 * math.sin(3 * MF)
	G = G + E * 0.00157 * math.sin(MD - MS - MF) - 0.001487 * math.sin(MF + ME1)
	G = G - E * 0.001481 * math.sin(MF + MS + MD) + E * 0.001417 * math.sin(MF - MS - MD)
	G = G + E * 0.00135 * math.sin(MF - MS) + 0.00133 * math.sin(MF - ME1)
	G = G + 0.001106 * math.sin(MF + 3 * MD) + 0.00102 * math.sin(4 * ME1 - MF)
	G = G + 0.000833 * math.sin(MF + 4 * ME1 - MD) + 0.000781 * math.sin(MD - 3 * MF)
	G = G + 0.00067 * math.sin(MF + 4 * ME1 - 2 * MD) + 0.000606 * math.sin(2 * ME1 - 3 * MF)
	G = G + 0.000597 * math.sin(2 * (ME1 + MD) - MF)
	G = G + E * 0.000492 * math.sin(2 * ME1 + MD - MS - MF) + 0.00045 * math.sin(2 * (MD - ME1) - MF)
	G = G + 0.000439 * math.sin(3 * MD - MF) + 0.000423 * math.sin(MF + 2 * (ME1 + MD))
	G = G + 0.000422 * math.sin(2 * ME1 - MF - 3 * MD) - E * 0.000367 * math.sin(MS + MF + 2 * ME1 - MD)
	G = G - E * 0.000353 * math.sin(MS + MF + 2 * ME1) + 0.000331 * math.sin(MF + 4 * ME1)
	G = G + E * 0.000317 * math.sin(2 * ME1 + MF - MS + MD)
	G = G + E2 * 0.000306 * math.sin(2 * (ME1 - MS) - MF) - 0.000283 * math.sin(MD + 3 * MF)
	W1 = 0.0004664 * math.cos(NA)
	W2 = 0.0000754 * math.cos(C)
	BM = math.radians(G) * (1 - W1 - W2)

	# Horizontal parallax-specific
	PM = 0.950724 + 0.051818 * math.cos(MD) + 0.009531 * math.cos(2 * ME1 - MD)
	PM = PM + 0.007843 * math.cos(2 * ME1) + 0.002824 * math.cos(2 * MD)
	PM = PM + 0.000857 * math.cos(2 * ME1 + MD) + E * 0.000533 * math.cos(2 * ME1 - MS)
	PM = PM + E * 0.000401 * math.cos(2 * ME1 - MD - MS)
	PM = PM + E * 0.00032 * math.cos(MD - MS) - 0.000271 * math.cos(ME1)
	PM = PM - E * 0.000264 * math.cos(MS + MD) - 0.000198 * math.cos(2 * MF - MD)
	PM = PM + 0.000173 * math.cos(3 * MD) + 0.000167 * math.cos(4 * ME1 - MD)
	PM = PM - E * 0.000111 * math.cos(MS) + 0.000103 * math.cos(4 * ME1 - 2 * MD)
	PM = PM - 0.000084 * math.cos(2 * MD - 2 * ME1) - E * 0.000083 * math.cos(2 * ME1 + MS)
	PM = PM + 0.000079 * math.cos(2 * ME1 + 2 * MD) + 0.000072 * math.cos(4 * ME1)
	PM = PM + E * 0.000064 * math.cos(2 * ME1 - MS + MD) - E * 0.000063 * math.cos(2 * ME1 + MS - MD)
	PM = PM + E * 0.000041 * math.cos(MS + ME1) + E * 0.000035 * math.cos(2 * MD - MS)
	PM = PM - 0.000033 * math.cos(3 * MD - 2 * ME1) - 0.00003 * math.cos(MD + ME1)
	PM = PM - 0.000029 * math.cos(2 * (MF - ME1)) - E * 0.000029 * math.cos(2 * MD + MS)
	PM = PM + E2 * 0.000026 * math.cos(2 * (ME1 - MS)) - 0.000023 * math.cos(2 * (MF - ME1) + MD)
	PM = PM + E * 0.000019 * math.cos(4 * ME1 - MS - MD)

	moon_long_deg = degrees(MM)
	moon_lat_deg = degrees(BM)
	moon_hor_para = PM

	return moon_long_deg, moon_lat_deg, moon_hor_para

def moon_phase(LH, LM, LS, DS, ZC, DY, MN, YR):
	"""
	Calculate current phase of Moon.

	Original macro name: MoonPhase
	"""
	moon_long_deg, moon_lat_deg, moon_hor_para = moon_long_lat_hp(LH, LM, LS, DS, ZC, DY, MN, YR)

	CD = math.cos(math.radians(moon_long_deg - sun_long(LH, LM, LS, DS, ZC, DY, MN, YR))) * math.cos(math.radians(moon_lat_deg))
	D = math.acos(CD)
	SD = math.sin(D)
	I = 0.1468 * SD * (1 - 0.0549 * math.sin(moon_mean_anomaly(LH, LM, LS, DS, ZC, DY, MN, YR)))
	I = I / (1 - 0.0167 * math.sin(sun_mean_anomaly(LH, LM, LS, DS, ZC, DY, MN, YR)))
	I = 3.141592654 - D - math.radians(I)
	K = (1 + math.cos(I)) / 2

	return round(K,2)

def moon_mean_anomaly(LH, LM, LS, DS, ZC, DY, MN, YR):
	"""
	Calculate the Moon's mean anomaly.

	Original macro name: MoonMeanAnomaly
	"""
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2

	return math.radians(MD)

def new_moon(DS, ZC, DY, MN, YR):
	"""
	Calculate Julian date of New Moon.

	Original macro name: NewMoon

	Arguments:
		DS -- Daylight Savings offset.
		ZC -- Time zone correction, in hours.
		DY -- Local date, day part.
		MN -- Local date, month part.
		YR -- Local date, year part.
	"""
	D0 = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	M0 = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	Y0 = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)

	if Y0 < 0:
		Y0 = Y0 + 1

	J0 = cd_jd(0, 1, Y0) - 2415020
	DJ = cd_jd(D0, M0, Y0) - 2415020
	K = lint(((Y0 - 1900 + ((DJ - J0) / 365)) * 12.3685) + 0.5)
	TN = K / 1236.85
	TF = (K + 0.5) / 1236.85
	T = TN
	A,B,F = new_moon_full_moon_l6855(K,T)
	NI = A
	NF = B
	NB = F
	T = TF
	K = K + 0.5
	A,B,F = new_moon_full_moon_l6855(K,T)
	FI = A
	FF = B
	FB = F
	
	return NI + 2415020 + NF

def full_moon(DS, ZC, DY, MN, YR):
	"""
	Calculate Julian date of Full Moon.

	Original macro name: FullMoon

	Arguments:
		DS -- Daylight Savings offset.
		ZC -- Time zone correction, in hours.
		DY -- Local date, day part.
		MN -- Local date, month part.
		YR -- Local date, year part.
	"""
	D0 = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	M0 = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	Y0 = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)

	if Y0 < 0:
		Y0 = Y0 + 1

	J0 = cd_jd(0, 1, Y0) - 2415020
	DJ = cd_jd(D0, M0, Y0) - 2415020
	K = lint(((Y0 - 1900 + ((DJ - J0) / 365)) * 12.3685) + 0.5)
	TN = K / 1236.85
	TF = (K + 0.5) / 1236.85
	T = TN
	A,B,F = new_moon_full_moon_l6855(K,T)
	NI = A
	NF = B
	NB = F
	T = TF
	K = K + 0.5
	A,B,F = new_moon_full_moon_l6855(K,T)
	FI = A
	FF = B
	FB = F

	return FI + 2415020 + FF	

def new_moon_full_moon_l6855(K,T):
	""" Helper function for new_moon() and full_moon() """
	T2 = T * T
	E = 29.53 * K
	C = 166.56 + (132.87 - 0.009173 * T) * T
	C = math.radians(C)
	B = 0.00058868 * K + (0.0001178 - 0.000000155 * T) * T2
	B = B + 0.00033 * math.sin(C) + 0.75933
	A = K / 12.36886
	A1 = 359.2242 + 360 * fract(A) - (0.0000333 + 0.00000347 * T) * T2
	A2 = 306.0253 + 360 * fract(K / 0.9330851)
	A2 = A2 + (0.0107306 + 0.00001236 * T) * T2
	A = K / 0.9214926
	F = 21.2964 + 360 * fract(A) - (0.0016528 + 0.00000239 * T) * T2
	A1 = unwind_deg(A1)
	A2 = unwind_deg(A2)
	F = unwind_deg(F)
	A1 = math.radians(A1)
	A2 = math.radians(A2)
	F = math.radians(F)

	DD = (0.1734 - 0.000393 * T) * math.sin(A1) + 0.0021 * math.sin(2 * A1)
	DD = DD - 0.4068 * math.sin(A2) + 0.0161 * math.sin(2 * A2) - 0.0004 * math.sin(3 * A2)
	DD = DD + 0.0104 * math.sin(2 * F) - 0.0051 * math.sin(A1 + A2)
	DD = DD - 0.0074 * math.sin(A1 - A2) + 0.0004 * math.sin(2 * F + A1)
	DD = DD - 0.0004 * math.sin(2 * F - A1) - 0.0006 * math.sin(2 * F + A2) + 0.001 * math.sin(2 * F - A2)
	DD = DD + 0.0005 * math.sin(A1 + 2 * A2)
	E1 = math.floor(E)
	B = B + DD + (E - E1)
	B1 = math.floor(B)
	A = E1 + B1
	B = B - B1

	return A,B,F

def moon_rise_lct(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Local time of moonrise.

	Original macro name: MoonRiseLCT

	Returns:
		hours
	"""
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_rise_lct_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	if LCT == -99:
		return LCT
	LA = LU

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = moon_rise_lct_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT)
		MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_rise_lct_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		if LCT == -99:
			return LCT
		LA = LU

	X = lst_gst(LA, 0, 0, GLong)
	UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)

	return LCT

def moon_rise_lct_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT):
	""" Helper function for moon_rise_lct """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR

def moon_rise_lct_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for moon_rise_lct """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_rise(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	if e_rs(P, 0, 0, Q, 0, 0, degrees(DI), GLat) != "OK":
		LCT = -99

	return MM,BM,PM,DP,TH,DI,P,Q,LU,LCT

def e_moon_rise(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Moonrise calculation status.

	Original macro name: eMoonRise
	"""
	S4 = "OK"
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	
	MM,BM,PM,DP,TH,DI,P,Q,LU,S1 = e_moon_rise_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	LA = LU

	if S1 != "OK":
		S4 = S1
		return S4

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)
		S3 = e_gst_ut(X, 0, 0, GDY, GMN, GYR)

		if S3 != "OK":
			S4 = "GST conversion: " + S3

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = e_moon_rise_l6680(S3,G1,UT,DS,ZC,GDY,GMN,GYR,DY1,MN1,YR1)
		MM,BM,PM,DP,TH,DI,P,Q,LU,S1 = e_moon_rise_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		LA = LU

		if S1 != "OK":
			S4 = S1
			return S4

	X = lst_gst(LA, 0, 0, GLong)
	UT = gst_ut(X, 0, 0, GDY, GMN, GYR)
	S3 = e_gst_ut(X, 0, 0, GDY, GMN, GYR)

	if S3 != "OK":
		S4 = "GST conversion: " + S3

	return S4
    
def e_moon_rise_l6680(S3,G1,UT,DS,ZC,GDY,GMN,GYR,DY1,MN1,YR1):
	""" Helper function for e_moon_rise() """
	if S3 != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR
        
def e_moon_rise_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for e_moon_rise() """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_rise(P, 0, 0, Q, 0, 0, degrees(DI), GLat)
	S1 = e_rs(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	return MM,BM,PM,DP,TH,DI,P,Q,LU,S1

def moon_rise_lc_dmy(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Local date of moonrise.
	
	Original macro names: MoonRiseLcDay, MoonRiseLcMonth, MoonRiseLcYear

	Returns:
		Local date (day)
		Local date (month)
		Local date (year)
	"""
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_rise_lc_dmy_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	if LCT == -99:
		return LCT,LCT,LCT
	LA = LU

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = moon_rise_lc_dmy_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT)
		MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_rise_lc_dmy_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		if LCT == -99:
			return LCT,LCT,LCT
		LA = LU

	X = lst_gst(LA, 0, 0, GLong)
	UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)

	return DY1,MN1,YR1

def moon_rise_lc_dmy_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT):
	""" Helper function for moon_rise_lc_dmy """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR

def moon_rise_lc_dmy_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for moon_rise_lc_dmy """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_rise(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	return MM,BM,PM,DP,TH,DI,P,Q,LU,LCT

def moon_rise_az(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Local azimuth of moonrise.

	Original macro name: MoonRiseAz

	Returns:
		degrees
	"""
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	MM,BM,PM,DP,TH,DI,P,Q,LU,LCT,AU = moon_rise_az_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	if LCT == -99:
		return LCT
	LA = LU

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = moon_rise_az_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT)
		MM,BM,PM,DP,TH,DI,P,Q,LU,LCT,AU = moon_rise_az_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		if LCT == -99:
			return LCT
		LA = LU
		AA = AU

	AU = AA

	return AU

def moon_rise_az_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT):
	""" Helper function for moon_rise_az """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR

def moon_rise_az_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for moon_rise_az """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_rise(P, 0, 0, Q, 0, 0, degrees(DI), GLat)
	AU = rise_set_azimuth_rise(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	return MM,BM,PM,DP,TH,DI,P,Q,LU,LCT,AU

def moon_set_lct(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Local time of moonset.

	Original macro name: MoonSetLCT

	Returns:
		hours
	"""
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_set_lct_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	if LCT == -99:
		return LCT
	LA = LU

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = moon_set_lct_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT)
		MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_set_lct_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		if LCT == -99:
			return LCT
		LA = LU

	X = lst_gst(LA, 0, 0, GLong)
	UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)

	return LCT

def moon_set_lct_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT):
	""" Helper function for moon_set_lct """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR

def moon_set_lct_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for moon_set_lct """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_set(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	if e_rs(P, 0, 0, Q, 0, 0, degrees(DI), GLat) != "OK":
		LCT = -99

	return MM,BM,PM,DP,TH,DI,P,Q,LU,LCT

def e_moon_set(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Moonset calculation status.

	Original macro name: eMoonSet
	"""
	S4 = "OK"
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	
	MM,BM,PM,DP,TH,DI,P,Q,LU,S1 = e_moon_set_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	LA = LU

	if S1 != "OK":
		S4 = S1
		return S4

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)
		S3 = e_gst_ut(X, 0, 0, GDY, GMN, GYR)

		if S3 != "OK":
			S4 = "GST conversion: " + S3

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = e_moon_set_l6680(X,S3,G1,UT,DS,ZC,GDY,GMN,GYR,DY1,MN1,YR1)
		MM,BM,PM,DP,TH,DI,P,Q,LU,S1 = e_moon_set_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		LA = LU

		if S1 != "OK":
			S4 = S1
			return S4

	X = lst_gst(LA, 0, 0, GLong)
	UT = gst_ut(X, 0, 0, GDY, GMN, GYR)
	S3 = e_gst_ut(X, 0, 0, GDY, GMN, GYR)

	if S3 != "OK":
		S4 = "GST conversion: " + S3

	return S4
    
def e_moon_set_l6680(X,S3,G1,UT,DS,ZC,GDY,GMN,GYR,DY1,MN1,YR1):
	""" Helper function for e_moon_set() """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR
        
def e_moon_set_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for e_moon_set() """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_set(P, 0, 0, Q, 0, 0, degrees(DI), GLat)
	S1 = e_rs(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	return MM,BM,PM,DP,TH,DI,P,Q,LU,S1

def moon_set_lc_dmy(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Local date of moonset.
	
	Original macro names: MoonSetLcDay, MoonSetLcMonth, MoonSetLcYear

	Returns:
		Local date (day)
		Local date (month)
		Local date (year)
	"""
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_set_lc_dmy_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	if LCT == -99:
		return LCT,LCT,LCT
	LA = LU

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = moon_set_lc_dmy_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT)
		MM,BM,PM,DP,TH,DI,P,Q,LU,LCT = moon_set_lc_dmy_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		if LCT == -99:
			return LCT,LCT,LCT
		LA = LU

	X = lst_gst(LA, 0, 0, GLong)
	UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)

	return DY1,MN1,YR1

def moon_set_lc_dmy_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT):
	""" Helper function for moon_set_lc_dmy """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR

def moon_set_lc_dmy_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for moon_set_lc_dmy """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_set(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	return MM,BM,PM,DP,TH,DI,P,Q,LU,LCT

def moon_set_az(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Local azimuth of moonset.

	Original macro name: MoonSetAz

	Returns:
		degrees
	"""
	GDY = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	GMN = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	GYR = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)
	LCT = 12
	DY1 = DY
	MN1 = MN
	YR1 = YR
	MM,BM,PM,DP,TH,DI,P,Q,LU,LCT,AU = moon_set_az_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
	if LCT == -99:
		return LCT
	LA = LU

	for K in range(1,9):
		X = lst_gst(LA, 0, 0, GLong)
		UT = gst_ut(X, 0, 0, GDY, GMN, GYR)

		G1 = UT if K == 1 else GU

		GU = UT
		UT = GU
		UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR = moon_set_az_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT)
		MM,BM,PM,DP,TH,DI,P,Q,LU,LCT,AU = moon_set_az_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat)
		if LCT == -99:
			return LCT
		LA = LU
		AA = AU

	AU = AA

	return AU

def moon_set_az_l6680(X, DS, ZC, GDY, GMN, GYR, G1, UT):
	""" Helper function for moon_set_az """
	if e_gst_ut(X, 0, 0, GDY, GMN, GYR) != "OK":
		if abs(G1 - UT) > 0.5:
			UT = UT + 23.93447

	UT = ut_day_adjust(UT, G1)
	LCT = ut_lct(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	DY1 = ut_lc_day(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	MN1 = ut_lc_month(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	YR1 = ut_lc_year(UT, 0, 0, DS, ZC, GDY, GMN, GYR)
	GDY = lct_gday(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GMN = lct_gmonth(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	GYR = lct_gyear(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	UT = UT - 24 * math.floor(UT / 24)

	return UT,LCT,DY1,MN1,YR1,GDY,GMN,GYR

def moon_set_az_l6700(LCT,DS,ZC,DY1,MN1,YR1,GDY,GMN,GYR,GLat):
	""" Helper function for moon_set_az """
	MM = moon_long(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	BM = moon_lat(LCT, 0, 0, DS, ZC, DY1, MN1, YR1)
	PM = math.radians(moon_hp(LCT, 0, 0, DS, ZC, DY1, MN1, YR1))
	DP = nutat_long(GDY, GMN, GYR)
	TH = 0.27249 * math.sin(PM)
	DI = TH + 0.0098902 - PM
	P = dd_dh(ec_ra(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR))
	Q = ec_dec(MM + DP, 0, 0, BM, 0, 0, GDY, GMN, GYR)
	LU = rise_set_local_sidereal_time_set(P, 0, 0, Q, 0, 0, degrees(DI), GLat)
	AU = rise_set_azimuth_set(P, 0, 0, Q, 0, 0, degrees(DI), GLat)

	return MM,BM,PM,DP,TH,DI,P,Q,LU,LCT,AU

def lunar_eclipse_occurrence(DS, ZC, DY, MN, YR):
	"""
	Determine if a lunar eclipse is likely to occur.

	Original macro name: LEOccurrence
	"""
	D0 = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	M0 = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	Y0 = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)

	if Y0 < 0:
		Y0 = Y0 + 1

	J0 = cd_jd(0, 1, Y0)
	DJ = cd_jd(D0, M0, Y0)
	K = ((Y0 - 1900 + ((DJ - J0) * 1 / 365)) * 12.3685)
	K = lint(K + 0.5)
	TN = K / 1236.85
	TF = (K + 0.5) / 1236.85
	T = TN
	F,DD,E1,B,B1,A,B = lunar_eclipse_occurrence_l6855(T,K)
	NI = A
	NF = B
	NB = F
	T = TF
	K = K + 0.5
	F,DD,E1,B,B1,A,B = lunar_eclipse_occurrence_l6855(T,K)
	FI = A
	FF = B
	FB = F

	DF = abs(FB - 3.141592654 * lint(FB / 3.141592654))

	if DF > 0.37:
		DF = 3.141592654 - DF

	S = "Lunar eclipse certain"
	if DF >= 0.242600766:
		S = "Lunar eclipse possible"
		if DF > 0.37:
			S = "No lunar eclipse"

	return S

def lunar_eclipse_occurrence_l6855(T,K):
	""" Helper function for lunar_eclipse_occurrence """
	T2 = T * T
	E = 29.53 * K
	C = 166.56 + (132.87 - 0.009173 * T) * T
	C = math.radians(C)
	B = 0.00058868 * K + (0.0001178 - 0.000000155 * T) * T2
	B = B + 0.00033 * math.sin(C) + 0.75933
	A = K / 12.36886
	A1 = 359.2242 + 360 * f_part(A) - (0.0000333 + 0.00000347 * T) * T2
	A2 = 306.0253 + 360 * f_part(K / 0.9330851)
	A2 = A2 + (0.0107306 + 0.00001236 * T) * T2
	A = K / 0.9214926
	F = 21.2964 + 360 * f_part(A) - (0.0016528 + 0.00000239 * T) * T2
	A1 = unwind_deg(A1)
	A2 = unwind_deg(A2)
	F = unwind_deg(F)
	A1 = math.radians(A1)
	A2 = math.radians(A2)
	F = math.radians(F)

	DD = (0.1734 - 0.000393 * T) * math.sin(A1) + 0.0021 * math.sin(2 * A1)
	DD = DD - 0.4068 * math.sin(A2) + 0.0161 * math.sin(2 * A2) - 0.0004 * math.sin(3 * A2)
	DD = DD + 0.0104 * math.sin(2 * F) - 0.0051 * math.sin(A1 + A2)
	DD = DD - 0.0074 * math.sin(A1 - A2) + 0.0004 * math.sin(2 * F + A1)
	DD = DD - 0.0004 * math.sin(2 * F - A1) - 0.0006 * math.sin(2 * F + A2) + 0.001 * math.sin(2 * F - A2)
	DD = DD + 0.0005 * math.sin(A1 + 2 * A2)
	E1 = math.floor(E)
	B = B + DD + (E - E1)
	B1 = math.floor(B)
	A = E1 + B1
	B = B - B1

	return F,DD,E1,B,B1,A,B

def mag_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate magnitude of lunar eclipse.

	Original macro name: MagLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		MG = -99#
		return MG

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		MG = -99
		return MG

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	R = RM + RU
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RP - PJ) / (2 * RM)

	if DD < 0:
		return MG

	ZD = math.sqrt(DD)
	Z8 = Z1 - ZD
	Z9 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z8 < 0:
		Z8 = Z8 + 24

	R = RU - RM
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RU - PJ) / (2 * RM)

	return MG

def ut_end_total_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate end time of total phase of lunar eclipse (UT)

	Original macro name: UTEndTotalLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	R = RM + RU
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RP - PJ) / (2 * RM)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z8 = Z1 - ZD
	Z9 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z8 < 0:
		Z8 = Z8 + 24

	R = RU - RM
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RU - PJ) / (2 * RM)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	ZB = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	return ZB

def ut_end_umbra_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate end time of umbra phase of lunar eclipse (UT)

	Original macro name: UTEndUmbraLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	R = RM + RU
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RP - PJ) / (2 * RM)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z8 = Z1 - ZD
	Z9 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	return Z9

def ut_first_contact_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate time of first shadow contact for lunar eclipse (UT)

	Original macro name: UTFirstContactLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD

	if Z6 < 0:
		Z6 = Z6 + 24

	return Z6

def ut_last_contact_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate time of last shadow contact for lunar eclipse (UT)

	Original macro name: UTLastContactLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	return Z7

def ut_max_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate time of maximum shadow for lunar eclipse (UT)

	Original macro name: UTMaxLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	return Z1

def ut_start_total_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate start time of total phase of lunar eclipse (UT)

	Original macro name: UTStartTotalLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	R = RM + RU
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RP - PJ) / (2 * RM)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z8 = Z1 - ZD
	Z9 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z8 < 0:
		Z8 = Z8 + 24

	R = RU - RM
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RU - PJ) / (2 * RM)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	ZCC = Z1 - ZD
	ZB = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if ZCC < 0:
		ZCC = ZC + 24

	return ZCC

def ut_start_umbra_lunar_eclipse(DY, MN, YR, DS, ZC):
	"""
	Calculate start time of umbra phase of lunar eclipse (UT)

	Original macro name: UTStartUmbraLunarEclipse
	"""
	TP = 2 * math.pi

	if (lunar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No lunar eclipse"):
		return -99

	DJ = full_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTFM = XI * 24
	UT = UTFM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTFM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTFM
	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	SR = SR + math.pi - lint((SR + math.pi) / TP) * TP
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RP
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	R = RM + RU
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)
	MG = (RM + RP - PJ) / (2 * RM)

	if DD < 0:
		return -99

	ZD = math.sqrt(DD)
	Z8 = Z1 - ZD
	Z9 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z8 < 0:
		Z8 = Z8 + 24

	return Z8

def solar_eclipse_occurrence(DS, ZC, DY, MN, YR):
	"""
	Determine if a solar eclipse is likely to occur.

	Original macro name: SEOccurrence
	"""
	D0 = lct_gday(12, 0, 0, DS, ZC, DY, MN, YR)
	M0 = lct_gmonth(12, 0, 0, DS, ZC, DY, MN, YR)
	Y0 = lct_gyear(12, 0, 0, DS, ZC, DY, MN, YR)

	if Y0 < 0:
		Y0 = Y0 + 1

	J0 = cd_jd(0, 1, Y0)
	DJ = cd_jd(D0, M0, Y0)
	K = ((Y0 - 1900 + ((DJ - J0) * 1 / 365)) * 12.3685)
	K = lint(K + 0.5)
	TN = K / 1236.85
	TF = (K + 0.5) / 1236.85
	T = TN
	F,DD,E1,B,B1,A,B = solar_eclipse_occurrence_l6855(T,K)
	NI = A
	NF = B
	NB = F
	T = TF
	K = K + 0.5
	F,DD,E1,B,B1,A,B = solar_eclipse_occurrence_l6855(T,K)
	FI = A
	FF = B
	FB = F

	DF = abs(NB - 3.141592654 * lint(NB / 3.141592654))

	if DF > 0.37:
		DF = 3.141592654 - DF

	S = "Solar eclipse certain"
	if DF >= 0.242600766:
		S = "Solar eclipse possible"
		if DF > 0.37:
			S = "No solar eclipse"

	return S

def solar_eclipse_occurrence_l6855(T,K):
	""" Helper function for solar_eclipse_occurrence """
	T2 = T * T
	E = 29.53 * K
	C = 166.56 + (132.87 - 0.009173 * T) * T
	C = math.radians(C)
	B = 0.00058868 * K + (0.0001178 - 0.000000155 * T) * T2
	B = B + 0.00033 * math.sin(C) + 0.75933
	A = K / 12.36886
	A1 = 359.2242 + 360 * f_part(A) - (0.0000333 + 0.00000347 * T) * T2
	A2 = 306.0253 + 360 * f_part(K / 0.9330851)
	A2 = A2 + (0.0107306 + 0.00001236 * T) * T2
	A = K / 0.9214926
	F = 21.2964 + 360 * f_part(A) - (0.0016528 + 0.00000239 * T) * T2
	A1 = unwind_deg(A1)
	A2 = unwind_deg(A2)
	F = unwind_deg(F)
	A1 = math.radians(A1)
	A2 = math.radians(A2)
	F = math.radians(F)

	DD = (0.1734 - 0.000393 * T) * math.sin(A1) + 0.0021 * math.sin(2 * A1)
	DD = DD - 0.4068 * math.sin(A2) + 0.0161 * math.sin(2 * A2) - 0.0004 * math.sin(3 * A2)
	DD = DD + 0.0104 * math.sin(2 * F) - 0.0051 * math.sin(A1 + A2)
	DD = DD - 0.0074 * math.sin(A1 - A2) + 0.0004 * math.sin(2 * F + A1)
	DD = DD - 0.0004 * math.sin(2 * F - A1) - 0.0006 * math.sin(2 * F + A2) + 0.001 * math.sin(2 * F - A2)
	DD = DD + 0.0005 * math.sin(A1 + 2 * A2)
	E1 = math.floor(E)
	B = B + DD + (E - E1)
	B1 = math.floor(B)
	A = E1 + B1
	B = B - B1

	return F,DD,E1,B,B1,A,B

def mag_solar_eclipse(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Calculate magnitude of solar eclipse.

	Original macro name: MagSolarEclipse
	"""
	TP = 2 * math.pi

	if solar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No solar eclipse":
		return -99

	DJ = new_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTNM = XI * 24
	UT = UTNM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTNM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTNM
	X = MY
	Y = BY
	TM = XH - 1
	HP = HY
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = mag_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MY = P
	BY = Q
	X = MZ
	Y = BZ
	TM = XH + 1
	HP = HZ
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = mag_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MZ = P
	BZ = Q

	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	X = SR
	Y = 0
	TM = UT
	HP = 0.00004263452 / RR
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = mag_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	SR = P
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RN
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99
		
	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	MG = (RM + RN - PJ) / (2 * RN)

	return MG

def mag_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP):
	""" Helper function for mag_solar_eclipse """
	PAA = ec_ra(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	QAA = ec_dec(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	XAA = ra_ha(dd_dh(PAA), 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	PBB = parallax_ha(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	QBB = parallax_dec(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	XBB = ha_ra(PBB, 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	P = math.radians(eq_e_long(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))
	Q = math.radians(eq_e_lat(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))

	return PAA,QAA,XAA,PBB,QBB,XBB,P,Q

def ut_first_contact_solar_eclipse(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Calculate time of first contact for solar eclipse (UT)

	Original macro name: UTFirstContactSolarEclipse
	"""
	TP = 2 * math.pi

	if solar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No solar eclipse":
		return -99

	DJ = new_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTNM = XI * 24
	UT = UTNM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTNM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTNM
	X = MY
	Y = BY
	TM = XH - 1
	HP = HY
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_first_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MY = P
	BY = Q
	X = MZ
	Y = BZ
	TM = XH + 1
	HP = HZ
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_first_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MZ = P
	BZ = Q

	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	X = SR
	Y = 0
	TM = UT
	HP = 0.00004263452 / RR
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_first_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	SR = P
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RN
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99
		
	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	MG = (RM + RN - PJ) / (2 * RN)

	return Z6

def ut_first_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP):
	""" Helper function for ut_first_contact_solar_eclipse """
	PAA = ec_ra(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	QAA = ec_dec(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	XAA = ra_ha(dd_dh(PAA), 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	PBB = parallax_ha(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	QBB = parallax_dec(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	XBB = ha_ra(PBB, 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	P = math.radians(eq_e_long(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))
	Q = math.radians(eq_e_lat(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))

	return PAA,QAA,XAA,PBB,QBB,XBB,P,Q

def ut_last_contact_solar_eclipse(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Calculate time of last contact for solar eclipse (UT)

	Original macro name: UTLastContactSolarEclipse
	"""
	TP = 2 * math.pi

	if solar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No solar eclipse":
		return -99

	DJ = new_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTNM = XI * 24
	UT = UTNM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTNM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTNM
	X = MY
	Y = BY
	TM = XH - 1
	HP = HY
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_last_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MY = P
	BY = Q
	X = MZ
	Y = BZ
	TM = XH + 1
	HP = HZ
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_last_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MZ = P
	BZ = Q

	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	X = SR
	Y = 0
	TM = UT
	HP = 0.00004263452 / RR
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_last_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	SR = P
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RN
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99
		
	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	MG = (RM + RN - PJ) / (2 * RN)

	return Z7

def ut_last_contact_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP):
	""" Helper function for ut_last_contact_solar_eclipse """
	PAA = ec_ra(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	QAA = ec_dec(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	XAA = ra_ha(dd_dh(PAA), 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	PBB = parallax_ha(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	QBB = parallax_dec(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	XBB = ha_ra(PBB, 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	P = math.radians(eq_e_long(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))
	Q = math.radians(eq_e_lat(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))

	return PAA,QAA,XAA,PBB,QBB,XBB,P,Q

def ut_max_solar_eclipse(DY, MN, YR, DS, ZC, GLong, GLat):
	"""
	Calculate time of maximum shadow for solar eclipse (UT)

	Original macro name: UTMaxSolarEclipse
	"""
	TP = 2 * math.pi

	if solar_eclipse_occurrence(DS, ZC, DY, MN, YR) == "No solar eclipse":
		return -99

	DJ = new_moon(DS, ZC, DY, MN, YR)
	DP = 0
	GDay = jdc_day(DJ)
	GMonth = jdc_month(DJ)
	GYear = jdc_year(DJ)
	IGDay = math.floor(GDay)
	XI = GDay - IGDay
	UTNM = XI * 24
	UT = UTNM - 1
	LY = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	MY = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BY = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HY = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	UT = UTNM + 1
	SB = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)) - LY
	MZ = math.radians(moon_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	BZ = math.radians(moon_lat(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	HZ = math.radians(moon_hp(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))

	if SB < 0:
		SB = SB + TP

	XH = UTNM
	X = MY
	Y = BY
	TM = XH - 1
	HP = HY
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_max_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MY = P
	BY = Q
	X = MZ
	Y = BZ
	TM = XH + 1
	HP = HZ
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_max_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	MZ = P
	BZ = Q

	X0 = XH + 1 - (2 * BZ / (BZ - BY))
	DM = MZ - MY

	if DM < 0:
		DM = DM + TP

	LJ = (DM - SB) / 2
	Q = 0
	MR = MY + (DM * (X0 - XH + 1) / 2)
	UT = X0 - 0.13851852
	RR = sun_dist(UT, 0, 0, 0, 0, IGDay, GMonth, GYear)
	SR = math.radians(sun_long(UT, 0, 0, 0, 0, IGDay, GMonth, GYear))
	SR = SR + math.radians(nutat_long(IGDay, GMonth, GYear) - 0.00569)
	X = SR
	Y = 0
	TM = UT
	HP = 0.00004263452 / RR
	PAA,QAA,XAA,PBB,QBB,XBB,P,Q = ut_max_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP)
	SR = P
	BY = BY - Q
	BZ = BZ - Q
	P3 = 0.00004263
	ZH = (SR - MR) / LJ
	TC = X0 + ZH
	SH = (((BZ - BY) * (TC - XH - 1) / 2) + BZ) / LJ
	S2 = SH * SH
	Z2 = ZH * ZH
	PS = P3 / (RR * LJ)
	Z1 = (ZH * Z2 / (Z2 + S2)) + X0
	H0 = (HY + HZ) / (2 * LJ)
	RM = 0.272446 * H0
	RN = 0.00465242 / (LJ * RR)
	HD = H0 * 0.99834
	RU = (HD - RN + PS) * 1.02
	RP = (HD + RN + PS) * 1.02
	PJ = abs(SH * ZH / math.sqrt(S2 + Z2))
	R = RM + RN
	DD = Z1 - X0
	DD = DD * DD - ((Z2 - (R * R)) * DD / ZH)

	if DD < 0:
		return -99
		
	ZD = math.sqrt(DD)
	Z6 = Z1 - ZD
	Z7 = Z1 + ZD - lint((Z1 + ZD) / 24) * 24

	if Z6 < 0:
		Z6 = Z6 + 24

	MG = (RM + RN - PJ) / (2 * RN)

	return Z1

def ut_max_solar_eclipse_l7390(X,Y,IGDay,GMonth,GYear,TM,GLong,GLat,HP):
	""" Helper function for ut_max_solar_eclipse """
	PAA = ec_ra(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	QAA = ec_dec(degrees(X), 0, 0, degrees(Y), 0, 0, IGDay, GMonth, GYear)
	XAA = ra_ha(dd_dh(PAA), 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	PBB = parallax_ha(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	QBB = parallax_dec(XAA, 0, 0, QAA, 0, 0, "True", GLat, 0, degrees(HP))
	XBB = ha_ra(PBB, 0, 0, TM, 0, 0, 0, 0, IGDay, GMonth, GYear, GLong)
	P = math.radians(eq_e_long(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))
	Q = math.radians(eq_e_lat(XBB, 0, 0, QBB, 0, 0, IGDay, GMonth, GYear))

	return PAA,QAA,XAA,PBB,QBB,XBB,P,Q

def fract(W):
	"""
	Original macro name: FRACT
	"""
	return W - lint(W)

def lint(W):
	"""
	Original macro name: LINT
	"""
	return iint(W) + iint(((1 * sgn(W)) - 1) / 2)

def iint(W):
	"""
	Original macro name: IINT
	"""
	return sgn(W) * math.floor(abs(W))

def sgn(number_to_check):
	"""
	Calculate sign of number.

	Arguments:
		number_to_check -- Number to calculate the sign of.

	Returns:
		sign_value -- Sign value: -1, 0, or 1
	"""
	sign_value = 0

	if number_to_check < 0:
		sign_value = -1

	if number_to_check > 0:
		sign_value = 1

	return sign_value

def ut_day_adjust(UT, G1):
	"""
	Original macro name: UTDayAdjust
	"""
	return_value = UT

	if (UT - G1) < -6:
		return_value = UT + 24

	if (UT - G1) > 6:
		return_value = UT - 24

	return return_value

def f_part(W):
	"""
	Original macro name: Fpart
	"""

	return W - lint(W)

def eq_e_lat(RAH, RAM, RAS, DD, DM, DS, GD, GM, GY):
	"""
	Original macro name: EQElat
	"""
	A = math.radians(dh_dd(hms_dh(RAH, RAM, RAS)))
	B = math.radians(dms_dd(DD, DM, DS))
	C = math.radians(obliq(GD, GM, GY))
	D = math.sin(B) * math.cos(C) - math.cos(B) * math.sin(C) * math.sin(A)

	return degrees(math.asin(D))

def eq_e_long(RAH, RAM, RAS, DD, DM, DS, GD, GM, GY):
	"""
	Original macro name: EQElong
	"""
	A = math.radians(dh_dd(hms_dh(RAH, RAM, RAS)))
	B = math.radians(dms_dd(DD, DM, DS))
	C = math.radians(obliq(GD, GM, GY))
	D = math.sin(A) * math.cos(C) + math.tan(B) * math.sin(C)
	E = math.cos(A)
	F = degrees(math.atan2(D, E))

	return F - 360 * math.floor(F / 360)

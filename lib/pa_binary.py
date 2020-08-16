import math
from . import pa_macro as PM
from . import pa_binary_data as PBD

def binary_star_orbit(greenwich_date_day, greenwich_date_month, greenwich_date_year, binary_name):
	"""
	Calculate orbital data for binary star.

	Arguments:
		greenwich_date_day -- Greenwich date (day)
		greenwich_date_month -- Greenwich date (month)
		greenwich_date_year -- Greenwich date (year)
		binary_name -- Abbreviated name of binary

	Returns:
		position_angle_deg -- Position angle (degrees)	
		separation_arcsec -- Separation of binary members (arcseconds)
	"""

	y_years = (greenwich_date_year+(PM.cd_jd(greenwich_date_day,greenwich_date_month,greenwich_date_year)-PM.cd_jd(0,1,greenwich_date_year))/365.242191)-PBD.get_binary_data(binary_name)['EpochPeri']
	m_deg = 360*y_years / PBD.get_binary_data(binary_name)['Period']
	m_rad = math.radians(m_deg-360*math.floor(m_deg/360))
	eccentricity = PBD.get_binary_data(binary_name)['Ecc']
	true_anomaly_rad = PM.true_anomaly(m_rad,eccentricity)
	r_arcsec = (1-eccentricity*math.cos(PM.eccentric_anomaly(m_rad,eccentricity)))*PBD.get_binary_data(binary_name)['Axis']
	ta_peri_rad = true_anomaly_rad+math.radians(PBD.get_binary_data(binary_name)['LongPeri'])
	y = math.sin(ta_peri_rad)*math.cos(math.radians(PBD.get_binary_data(binary_name)['Incl']))
	x = math.cos(ta_peri_rad)
	a_deg = PM.degrees(math.atan2(y,x))
	theta_deg1 = a_deg + PBD.get_binary_data(binary_name)['PANode']
	theta_deg2 = theta_deg1-360*math.floor(theta_deg1/360)
	rho_arcsec = r_arcsec*math.cos(ta_peri_rad)/math.cos(math.radians(theta_deg2-PBD.get_binary_data(binary_name)['PANode']))

	position_angle_deg = round(theta_deg2,1)
	separation_arcsec = round(rho_arcsec,2)

	return position_angle_deg, separation_arcsec
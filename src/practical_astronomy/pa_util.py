def is_leap_year(year):
	""" Returns True or False indicating if the specified year is a leap year. """
	if (year % 4) == 0:
		if (year % 100) == 0:
			return True if (year % 400) == 0 else False
		else:
			return True
	else:
		return False

def mi_to_km(miles):
	""" Convert miles to kilometers. """
	return miles * 1.609344

def km_to_mi(kilometers):
	""" Convert kilometers to miles. """
	return kilometers * 0.6213712

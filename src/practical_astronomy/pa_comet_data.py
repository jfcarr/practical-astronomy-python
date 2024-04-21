
CometDataElliptical = {
	"Encke": {
		"Epoch": 1974.32,
		"Peri": 160.1,
		"Node": 334.2,
		"Period": 3.3,
		"Axis": 2.21,
		"Ecc": 0.85,
		"Incl": 12
	},
	"Temple 2": {
		"Epoch": 1972.87,
		"Peri": 310.2,
		"Node": 119.3,
		"Period": 5.26,
		"Axis": 3.02,
		"Ecc": 0.55,
		"Incl": 12.5
	},
	"Haneda-Campos": {
		"Epoch": 1978.77,
		"Peri": 12.02,
		"Node": 131.7,
		"Period": 5.37,
		"Axis": 3.07,
		"Ecc": 0.64,
		"Incl": 5.81
	},
	"Schwassmann-Wachmann 2": {
		"Epoch": 1974.7,
		"Peri": 123.3,
		"Node": 126,
		"Period": 6.51,
		"Axis": 3.49,
		"Ecc": 0.39,
		"Incl": 3.7
	},
	"Borrelly": {
		"Epoch": 1974.36,
		"Peri": 67.8,
		"Node": 75.1,
		"Period": 6.76,
		"Axis": 3.58,
		"Ecc": 0.63,
		"Incl": 30.2
	},
	"Whipple": {
		"Epoch": 1970.77,
		"Peri": 18.2,
		"Node": 188.4,
		"Period": 7.47,
		"Axis": 3.82,
		"Ecc": 0.35,
		"Incl": 10.2
	},
	"Oterma": {
		"Epoch": 1958.44,
		"Peri": 150,
		"Node": 155.1,
		"Period": 7.88,
		"Axis": 3.96,
		"Ecc": 0.14,
		"Incl": 4
	},
	"Schaumasse": {
		"Epoch": 1960.29,
		"Peri": 138.1,
		"Node": 86.2,
		"Period": 8.18,
		"Axis": 4.05,
		"Ecc": 0.71,
		"Incl": 12
	},
	"Comas Sola": {
		"Epoch": 1969.83,
		"Peri": 102.9,
		"Node": 62.8,
		"Period": 8.55,
		"Axis": 4.18,
		"Ecc": 0.58,
		"Incl": 13.4
	},
	"Schwassmann-Wachmann 1": {
		"Epoch": 1974.12,
		"Peri": 334.1,
		"Node": 319.6,
		"Period": 15.03,
		"Axis": 6.09,
		"Ecc": 0.11,
		"Incl": 9.7
	},
	"Neujmin 1": {
		"Epoch": 1966.94,
		"Peri": 334,
		"Node": 347.2,
		"Period": 17.93,
		"Axis": 6.86,
		"Ecc": 0.78,
		"Incl": 15
	},
	"Crommelin": {
		"Epoch": 1956.82,
		"Peri": 86.4,
		"Node": 250.4,
		"Period": 27.89,
		"Axis": 9.17,
		"Ecc": 0.92,
		"Incl": 28.9
	},
	"Olbers": {
		"Epoch": 1956.46,
		"Peri": 150,
		"Node": 85.4,
		"Period": 69.47,
		"Axis": 16.84,
		"Ecc": 0.93,
		"Incl": 44.6
	},
	"Pons-Brooks": {
		"Epoch": 1954.39,
		"Peri": 94.2,
		"Node": 255.2,
		"Period": 70.98,
		"Axis": 17.2,
		"Ecc": 0.96,
		"Incl": 74.2
	},
	"Halley": {
		"Epoch": 1986.112,
		"Peri": 170.011,
		"Node": 58.154,
		"Period": 76.0081,
		"Axis": 17.9435,
		"Ecc": 0.9673,
		"Incl": 162.2384
	}
}

CometDataParabolic = {
	"Kohler": {
		"EpochPeriDay": 10.5659,
		"EpochPeriMonth": 11,
		"EpochPeriYear": 1977,
		"ArgPeri": 163.4799,
		"Node": 181.8175,
		"PeriDist": 0.990662,
		"Incl": 48.7196
	}
}

def get_comet_data_elliptical(comet_name):
	"""
	Get data for elliptical comet.
	
	Example, retrieving orbital period of Halley:
		get_comet_data_elliptical("Halley")['Period']

	Arguments:
		comet_name -- Name of comet, e.g., "Halley"

	Returns:
		A dictionary object with the following elements:

		Epoch -- Epoch of the perihelion.
		Peri -- Longitude of the perihelion.
		Node -- Longitude of the ascending node.
		Period -- Period of the orbit.
		Axis -- Semi-major axis of the orbit.
		Ecc -- Eccentricity of the orbit.
		Incl -- Orbital inclination.
	"""
	return CometDataElliptical.get(comet_name)

def get_comet_data_parabolic(comet_name):
	"""
	Get data for parabolic comet.

	Example, retrieving longitude of the ascending node of Kohler:
		get_comet_data_parabolic("Kohler")['Node']

	Arguments:
		comet_name -- Name of comet, e.g., "Kohler"

	Returns:
		A dictionary object with the following elements:

		EpochPeriDay -- Epoch of the perihelion (day)
		EpochPeriMonth -- Epoch of the perihelion (month)
		EpochPeriYear -- Epoch of the perihelion (year)
		ArgPeri -- Longitude of the perihelion (degrees)
		Node -- Longitude of the ascending node (degrees)
		PeriDist -- Distance at perihelion (AU)	
		Incl -- Orbital inclination (degrees)
	"""
	return CometDataParabolic.get(comet_name)
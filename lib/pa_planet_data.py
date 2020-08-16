
PlanetData = {
	"Mercury": {
		"Tp": 0.24085,
		"Long": 75.5671,
		"Peri": 77.612,
		"Ecc": 0.205627,
		"Axis": 0.387098,
		"Incl": 7.0051,
		"Node": 48.449,
		"Theta0": 6.74,
		"V0": -0.42
	},
	"Venus": {
		"Tp": 0.615207,
		"Long": 272.30044,
		"Peri": 131.54,
		"Ecc": 0.006812,
		"Axis": 0.723329,
		"Incl": 3.3947,
		"Node": 76.769,
		"Theta0": 16.92,
		"V0": -4.4
	},
	"Earth": {
		"Tp": 0.999996,
		"Long": 99.556772,
		"Peri": 103.2055,
		"Ecc": 0.016671,
		"Axis": 0.999985,
		"Incl": None,
		"Node": None,
		"Theta0": None,
		"V0": None
	},
	"Mars": {
		"Tp": 1.880765,
		"Long": 109.09646,
		"Peri": 336.217,
		"Ecc": 0.093348,
		"Axis": 1.523689,
		"Incl": 1.8497,
		"Node": 49.632,
		"Theta0": 9.36,
		"V0": -1.52
	},
	"Jupiter": {
		"Tp": 11.857911,
		"Long": 337.917132,
		"Peri": 14.6633,
		"Ecc": 0.048907,
		"Axis": 5.20278,
		"Incl": 1.3035,
		"Node": 100.595,
		"Theta0": 196.74,
		"V0": -9.4
	},
	"Saturn": {
		"Tp": 29.310579,
		"Long": 172.398316,
		"Peri": 89.567,
		"Ecc": 0.053853,
		"Axis": 9.51134,
		"Incl": 2.4873,
		"Node": 113.752,
		"Theta0": 165.6,
		"V0": -8.88
	},
	"Uranus": {
		"Tp": 84.039492,
		"Long": 356.135400,
		"Peri": 172.884833,
		"Ecc": 0.046321,
		"Axis": 19.21814,
		"Incl": 0.773059,
		"Node": 73.926961,
		"Theta0": 65.8,
		"V0": -7.19
	},
	"Neptune": {
		"Tp": 165.845392,
		"Long": 326.895127,
		"Peri": 23.07,
		"Ecc": 0.010483,
		"Axis": 30.1985,
		"Incl": 1.7673,
		"Node": 131.879,
		"Theta0": 62.2,
		"V0": -6.87
	}
}

def get_planet_data(planet_name):
	"""
	Get planet data.

	Arguments:
		planet_name -- Name of planet, e.g., "Jupiter"

	Returns a dictionary object with the following elements:
		Tp -- Period of orbit.
		Long -- Longitude at the epoch.
		Peri -- Longitude of the perihelion.
		Ecc -- Eccentricity of the orbit.
		Axis -- Semi-major axis of the orbit.
		Incl -- Orbital inclination.
		Node -- Longitude of the ascending node.
		Theta0 -- ?
		V0 -- ?
	"""
	return PlanetData.get(planet_name)

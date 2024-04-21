BinaryData = {
	"eta-Cor": {
		"Period": 41.623,
		"EpochPeri": 1934.008,
		"LongPeri": 219.907,
		"Ecc": 0.2763,
		"Axis": 0.907,
		"Incl": 59.025,
		"PANode": 23.717
	},
	"gamma-Vir": {
		"Period": 171.37,
		"EpochPeri": 1836.433,
		"LongPeri": 252.88,
		"Ecc": 0.8808,
		"Axis": 3.746,
		"Incl": 146.05,
		"PANode": 31.78
	},
	"eta-Cas": {
		"Period": 480,
		"EpochPeri": 1889.6,
		"LongPeri": 268.59,
		"Ecc": 0.497,
		"Axis": 11.9939,
		"Incl": 34.76,
		"PANode": 278.42
	},
	"zeta-Ori": {
		"Period": 1508.6,
		"EpochPeri": 2070.6,
		"LongPeri": 47.3,
		"Ecc": 0.07,
		"Axis": 2.728,
		"Incl": 72,
		"PANode": 155.5
	},
	"alpha-CMa": {
		"Period": 50.09,
		"EpochPeri": 1894.13,
		"LongPeri": 147.27,
		"Ecc": 0.5923,
		"Axis": 7.5,
		"Incl": 136.53,
		"PANode": 44.57
	},
	"delta-Gem": {
		"Period": 1200,
		"EpochPeri": 1437,
		"LongPeri": 57.19,
		"Ecc": 0.11,
		"Axis": 6.9753,
		"Incl": 63.28,
		"PANode": 18.38
	},
	"alpha-Gem": {
		"Period": 420.07,
		"EpochPeri": 1965.3,
		"LongPeri": 261.43,
		"Ecc": 0.33,
		"Axis": 6.295,
		"Incl": 115.94,
		"PANode": 40.47
	},
	"aplah-CMi": {
		"Period": 40.65,
		"EpochPeri": 1927.6,
		"LongPeri": 269.8,
		"Ecc": 0.4,
		"Axis": 4.548,
		"Incl": 35.7,
		"PANode": 284.3
	},
	"alpha-Cen": {
		"Period": 79.92,
		"EpochPeri": 1955.56,
		"LongPeri": 231.56,
		"Ecc": 0.516,
		"Axis": 17.583,
		"Incl": 79.24,
		"PANode": 204.868
	},
	"alpha Sco": {
		"Period": 900,
		"EpochPeri": 1889,
		"LongPeri": 0,
		"Ecc": 0,
		"Axis": 3.21,
		"Incl": 86.3,
		"PANode": 273
	}
}

def get_binary_data(binary_name):
	'''
	Get data for binary star.
	
	Example, retrieving orbital inclination of eta-Cor:
		get_binary_data("eta-Cor")['Incl']

	Arguments:
		binary_name -- Name of binary, e.g., "eta-Cor"

	Returns:
		A dictionary object with the following elements:

		Period -- Period of the orbit.
		EpochPeri -- Epoch of the perihelion.
		LongPeri -- Longitude of the perihelion.
		Ecc -- Eccentricity of the orbit.
		Axis -- Semi-major axis of the orbit.
		Incl -- Orbital inclination.
		PANode -- Position angle of the ascending node.
	'''
	return BinaryData.get(binary_name)

to_microns = {"nanometers": 0.001,
		"microns": 1,
		"milimeters": 1000,
		"centimeters": 10000,
		"meters": 1000000,
		"kilometers": 1000000000,
		"inches": 25400,
		"feet": 304800,
		"yards": 914400,
		"miles": 1609344000,
		"nautical miles": 1852000000
		}
microns_to = {"nanometers": 1000,
		"microns": 1,
		"milimeters": 0.001,
		"centimeters": 0.0001,
		"meters": 0.000001,
		"kilometers": 0.000000001,
		"inches": 0.000039,
		"feet": 0.000003,
		"yards": 0.000001,
		"miles": 0.000000000621371,
		"nautical miles": 0.000000000539957
		}

def lenconvert(length_from, length_to, amount):
	try:
		if length_from == "microns" and length_to == "microns" :
			return 1

		elif length_from != "microns" and length_to == "microns" :
			amount *= to_microns[length_from]

		elif length_from == "microns" and length_to != "microns" :
			amount *= microns_to[length_to]

		elif length_from != "microns" and length_to != "microns" :
			amount *= to_microns[length_from]
			amount *= microns_to[length_to]

		return amount
	except:
		return "Error"


# print(lenconvert('milimeters', 'meters', 1000))
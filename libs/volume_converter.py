to_milimeter = {"milimeters": 1,
		"cubic centimeters": 1,
		"liters": 1000,
		"cubic meters": 1000000,
		"teaspoons(us)": 4.928922,
		"tablespoons(us)": 14.78676,
		"fluid ounces(us)": 29.57353,
		"cups(us)": 236.5882,
		"pints(us)": 473.1765,
		"quarts": 946.3529,
		"gallons": 3785.412,
		"cubic inches": 16.38706,
		"cubic feet": 28316.85,
		"cubic yard": 764554.9,
		"teaspoons(uk)": 5.919388,
		"tablespoons(uk)": 17.75816,
		"fluid ounces(uk)": 28.41306,
		"pints(uk)": 568.2613,
		"quarts(uk)": 1136.523,
		"gallons(uk)": 4546.09
		}

milimeter_to = {"milimeters": 1,
		"cubic centimeters": 1,
		"liters": 0.001,
		"cubic meters": 0.000001,
		"teaspoons(us)": 0.202884,
		"tablespoons(us)": 0.067628,
		"fluid ounces(us)": 0.033814,
		"cups(us)": 0.004227,
		"pints(us)": 0.002113,
		"quarts": 0.001057,
		"gallons": 0.000264,
		"cubic inches": 0.061024,
		"cubic feet": 0.000035,
		"cubic yard": 0.000001,
		"teaspoons(uk)": 0.168936,
		"tablespoons(uk)": 0.056312,
		"fluid ounces(uk)": 0.035195,
		"pints(uk)": 0.00176,
		"quarts(uk)": 0.00088,
		"gallons(uk)": 0.00022
		}

def volconvert(volume_from, volume_to, amount):
	try:
		if volume_from == "milimeters" and volume_to == "milimeters" :
			return 1

		elif volume_from != "milimeters" and volume_to == "milimeters" :
			amount *= to_milimeter[volume_from]

		elif volume_from == "milimeters" and volume_to != "milimeters" :
			amount *= milimeter_to[volume_to]

		elif volume_from != "milimeters" and volume_to != "milimeters" :
			amount *= to_milimeter[volume_from]
			amount *= milimeter_to[volume_to]

		return amount
	except:
		return "Error"



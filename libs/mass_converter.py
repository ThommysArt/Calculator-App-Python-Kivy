miligrams_to = {
    "carats": 0.005,
    "miligrams": 1,
    "centigrams": 0.1,
    "decigrams": 0.01,
    "grams": 0.001,
    "dekagrams": 0.0001,
    "hectograms": 0.00001,
    "kilograms": 0.000001,
    "metric tonnes": 0.000000001,
    "ounces": 0.000035273965,
    "pounds": 0.000002204622,
    "stone": 0.000000157473044,
    "short tons(us)": 0.000000001102311,
    "long tons(uk)": 0.000000000984207
}

to_miligrams = {
    "carats": 200,
    "miligrams": 1,
    "centigrams": 10,
    "decigrams": 100,
    "grams": 1000,
    "dekagrams": 10000,
    "hectograms": 100000,
    "kilograms": 1000000,
    "metric tonnes": 1000000000,
    "ounces": 28349.52,
    "pounds": 453592.4,
    "stone": 6350293,
    "short tons(us)": 907184740,
    "long tons(uk)": 1016046909
}


def mass_convert(mass1, mass2, amount):
	try:
		if mass1 == "miligrams" and mass2 == "miligrams":
			return 1
		elif mass1 == "miligrams" and mass2 != "miligrams":
			amount *= miligrams_to[mass2]
		elif mass1 != "miligrams" and mass2 == "miligrams":
			amount *= to_miligrams[mass1]
		elif mass1 != "miligrams" and mass2 != "miligrams":
			amount *= to_miligrams[mass1]
			amount *= miligrams_to[mass2]
		return amount
	except:
		return "Error"
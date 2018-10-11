def remove_duplicates(input_list):
	new = list()
	for i in input_list:
		if i not in new:
			new.append(i)

	return new

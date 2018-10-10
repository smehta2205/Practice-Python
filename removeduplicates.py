def removeDuplicates(arr):
	# Convert list to a set data structure where duplicates are not allowed.
	# Sort the set according to original indices so that you don't lose order.
	return sorted(set(arr), key=lambda x: arr.index(x))
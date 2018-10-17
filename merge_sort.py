def merge (left, right):
	result = list()

	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]

	while len(left) > 0:
		result.append(left[0])
		left = left[1:]

	while len(right) > 0:
		result.append(right[0])
		right = right[1:]

	return result

def merge_sort (items):
	length = len(items)

	if length <= 1:
		return items
	left = list()
	right = list()

	for i, x in enumerate(items):
		if i < length/2:
			left.append(x)
		else:
			right.append(x)

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

if __name__ == '__main__':
	data = [1, 9, 3, 2, 6, 5, 7, 3]
	print(merge_sort(data))

def bubble_sort(nums):
	temp = 0
	changed = True
	while changed == True:
		changed = False
		for i in xrange(len(nums) - 1):
			if nums[i+1] < nums[i]:
				temp = nums[i+1]
				nums[i+1] = nums[i]
				nums[i] = temp
				changed = True
	return nums


print bubble_sort([4,3,78,2,0,2])
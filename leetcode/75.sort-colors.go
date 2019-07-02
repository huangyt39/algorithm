/*
 * @lc app=leetcode id=75 lang=golang
 *
 * [75] Sort Colors
 */
func sortColors(nums []int) {
	count := [3]int{0, 0, 0}
	index := 0
	for _, num := range nums {
		count[num] += 1
	}
	for color, time := range count {
		for time > 0 {
			nums[index] = color
			time -= 1
			index += 1
		}
	}
	return
}


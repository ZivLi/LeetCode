/*
 * @lc app=leetcode.cn id=1480 lang=golang
 *
 * [1480] 一维数组的动态和
 */

// @lc code=start
func runningSum(nums []int) []int {
	for i := range nums {
		if i != 0 {
			nums[i] = nums[i] + nums[i-1]
		}
	}
	return nums
}

// @lc code=end


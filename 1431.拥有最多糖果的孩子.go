/*
 * @lc app=leetcode.cn id=1431 lang=golang
 *
 * [1431] 拥有最多糖果的孩子
 */

// @lc code=start
func kidsWithCandies(candies []int, extraCandies int) []bool {
	maxCandy := 0
	for _, candiesCount := range candies {
		if candiesCount > maxCandy {
			maxCandy = candiesCount
		}
	}
	result := make([]bool, len(candies))
	for i, candiesCount := range candies {
		result[i] = (candiesCount + extraCandies) >= maxCandy
	}
	return result
}


// @lc code=end


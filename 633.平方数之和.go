import "math"

/*
 * @lc app=leetcode.cn id=633 lang=golang
 *
 * [633] 平方数之和
 */

// @lc code=start
func judgeSquareSum(c int) bool {
	for i, j := 0, int(math.Sqrt(float64(c))); i <= j; {
		if sum := i*i + j*j; sum < c {
			i++
		} else if sum > c {
			j--
		} else {
			return true
		}
	}
	return false
}

// @lc code=end

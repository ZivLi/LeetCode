func convert(s string, numRows int) string{
  if numRows == 1{
	return s
  }
  runes := []rune(s)
  n := len(runes)
  runesOut := make([]rune, n)
  j := 0
  for row := 0; row < numRows; row ++{
	k := row
	skip := 2 * (numRows - row - 1)
	for j < n && k < n{
	  if skip > 0{
		runesOut[j] = runes[k]
		k = k + skip
		j ++
	  }
	  skip = 2 * (numRows - 1) - skip
	}
  }
  return string(runesOut)
}

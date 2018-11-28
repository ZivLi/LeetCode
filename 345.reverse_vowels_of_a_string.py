class Solution(object):
    def reverseVowels(self, s):
        v = 'aeiouAEIOU'
        i, j = 0, len(s) - 1
        l = [0] * (j + 1)
        while i <= j:
            while i < j and s[i] not in v: 
                l[i] = s[i]; i += 1
            while i < j and s[j] not in v: 
                l[j] = s[j]; j -= 1
            l[i], l[j] = s[j], s[i]
            i += 1; j -= 1
        return ''.join(l)

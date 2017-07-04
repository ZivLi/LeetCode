class Solution(object):
    line1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    line2 = ['a', 's', 'd', 'f', 'g', 'h', 'j','k', 'l']
    line3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = [
            word for word in words if self.check_one_line_words(word)
        ]
        return res

    def check_one_line_words(self, w):
        def not_in_line(w, temp_l):
            for o in w:
                if o not in temp_l:
                    return False
            return True

        w = w.lower()
        return any([
                not_in_line(w, self.line1),
                not_in_line(w, self.line2),
                not_in_line(w, self.line3)
            ])
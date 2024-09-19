class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        # %20
        '''
        arr = lint, code, abc%20abc, 4%, nice

        4%lint4%code9%abc%20abc2%4%4%nice
              l

        '''
        out = []

        for word in strs:
            out.append(str(len(word))+word)
        
        return "".join(out)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, string):
        lptr = 0
        out = []

        while lptr < len(string):
            lookahead = int(string[lptr])
            startindex = lptr+1

            out.append(string[startindex:startindex+lookahead])

            lptr = startindex + lookahead

        return out
    
if __name__ == "__main__":
    s = Solution()

    encoded = s.encode(["lint", "code", "abc%20abc", "4%", "  ", "nice"])
    decoded = s.decode(encoded)

    print(encoded, decoded)
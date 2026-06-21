class Solution:
    # idea: we have a new empty string X, we should get the length of each string and append it to X
    # then add the string to X and so on
    def encode(self, strs: List[str]) -> str:
        X = ""
        X += str(len(strs)) + "?"
        for s in strs:
            X += str(len(s)) + "!"
            X += s
        print(X)
        return X

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        length = 0
        for i in range(len(s)):
            if s[i] == "?":
                length = int(s[:i])
                start = i + 1
                break
        if length != 0:
            i = start
            while i < len(s):
                count = 0
                substart = i
                while True:
                    if s[i] == "!":
                        break
                    else:
                        count += 1
                        i += 1
                sub_len = int(s[substart:substart + count])
                res.append(s[i+1:i + sub_len+1])
                i+=sub_len+1

        return res

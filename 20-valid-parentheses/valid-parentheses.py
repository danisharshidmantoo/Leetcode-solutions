class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {}
        mapp["("] = ")"
        mapp['['] = ']'
        mapp["{"] = '}'

        arr = []
        for c in s:
            if c in mapp:
                arr.append(c)
            else:
                if not arr:
                    return False
                elif c != mapp[arr[-1]]:
                    return False
                else:
                    arr.pop()
        return len(arr) == 0
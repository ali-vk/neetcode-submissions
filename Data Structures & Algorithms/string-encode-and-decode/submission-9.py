class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(st)}#{st}" for st in strs)


    def decode(self, s: str) -> List[str]:
        deco = []
        i = 0
        while i < len(s):
            ind = s.find('#', i)
            len_ = int(s[i:ind])
            start = ind + 1
            end = start + len_
            deco.append(s[start:end])
            i = end
        return deco

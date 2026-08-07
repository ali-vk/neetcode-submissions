class Solution:

    def encode(self, strs: List[str]) -> str:
        str_ = ""
        return "".join(f"{len(st)}#{st}" for st in strs)

    def decode(self, s: str) -> List[str]:
        deco = []
        i = 0
        while i < len(s):
            hash_ind = s.find('#', i)
            len_ = int(s[i:hash_ind])
            start = hash_ind + 1
            end = start + len_
            deco.append(s[start:end])
            i = end
        return deco

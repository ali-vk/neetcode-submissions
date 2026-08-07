class Solution:

    def encode(self, strs: List[str]) -> str:
        str_ = ""
        for st in strs:
            str_ += str(len(st))+'#'+st
        return str_

    def decode(self, s: str) -> List[str]:
        addi = ""
        deco = []
        i = 0
        while i < len(s):
            hash_ind = s.find('#', i)
            if hash_ind == -1:
                break
            len_ = int(s[i:hash_ind])
            start = hash_ind + 1
            end = start + len_
            deco.append(s[start:end])
            addi = ""
            i = end
        return deco

class Solution:

    def encode(self, strs: List[str]) -> str:
        str_ = ""
        for st in strs:
            str_ += str(len(st))+'#'
            for ch in st:
                str_ += chr(ord(ch) - 4)
        return str_

    def decode(self, s: str) -> List[str]:
        # split = re.split(r'\d+#', s)[1:]
        # len_ = re.findall(r'(\d+)#', s)
        # addi = ""
        # deco = []
        # for i, st in enumerate(split):
        #     if len_[i] == 0:
        #         deco.append("")
        #         continue
        #     for ch in st:
        #         addi += chr(ord(ch) + 4)
        #     deco.append(addi)
        #     addi = ""
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
            for ch in s[start:end]:
                addi += chr(ord(ch) + 4)
            deco.append(addi)
            addi = ""
            i = end
        return deco

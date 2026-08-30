class Solution:

    def encode(self, strs: List[str]) -> str:
        
        ret = ""

        for s in strs:
            len_s = len(s)
            ret += f"{len_s}#{s}"
        
        print(ret)
        return ret



    def decode(self, s: str) -> List[str]: 
        
        ret = []
        len_s = ""
        num_len_s = -1
        i = 0

        while i < len(s):

            if s[i] == "#":
                num_len_s = int(len_s)
                len_s = ""
                ret.append(s[i+1:i+1+num_len_s])
                i += num_len_s
            else:
                len_s += s[i]

            i += 1

        return ret
        

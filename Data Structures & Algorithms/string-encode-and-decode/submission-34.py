class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for i in range(len(strs)):
            cnt = len(strs[i]) # 字數長度, 再前面補2個零
            encode_str = encode_str + str(cnt).zfill(3) + "%$#_" + strs[i]

        print(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        
        decode_list = []
        decode_str = ""
        
        for i in range(len(s)):
            if s[i:i+4] == "%$#_":
                for j in range(i+4, i+4+int(s[i-3:i])):
                    decode_str = decode_str + s[j]
                    # print(len(s), i, j, decode_str)
                decode_list.append(decode_str)
                decode_str = ""
        

        return decode_list

        

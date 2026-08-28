class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dist =  {}
        
        for i in range(len(strs)):
            txt = ''.join(sorted(strs[i]))

            # 若排序後的字串「第一次出現」，就幫他在字典開一個空箱子 []

            if txt not in dist:
                dist[txt] = []

            dist[txt].append(strs[i])

        # dist.values() 會直接把字典裡所有的內層 List 抓出來打包
        # 剛好就是我們要的二維陣列結果！
            
        return list(dist.values())


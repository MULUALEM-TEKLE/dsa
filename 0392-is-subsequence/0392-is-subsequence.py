class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == ""  : return True
        if t == "" : return False
        
       
        # t_list = list(t)
        # print(t_list)

        # for i  in range(len(t_list)):
        #     if t_list[i] not in s:
        #         t_list[i] = ""
        
        # last_pos = -1
        # similar_counter = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i] == t[j] :
        #             if last_pos > j : 
        #                 return False
        #             print("found {s[i]} = {t[j]}")
        #             last_pos = j
        #             similar_counter += 1
        #             continue
        #         continue
                   

        # print(similar_counter)
        
        # return similar_counter == len(s)

        last_pos = 0
        similar_count = 0
        for i in range(len(s)):
            print(f"search space is now :{t[last_pos+1 : ]} ")
            if s[i] in t :
                print(f"found {s[i]} at position {t.index(s[i])} ")
                last_pos = t.index(s[i])
                similar_count += 1
                t = t[last_pos+1 : ]
                continue
            else : 
                return False

        print(similar_count)

        return similar_count  == len(s)


        


       
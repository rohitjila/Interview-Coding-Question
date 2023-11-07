class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        stack = []
        lst = ["[" ,"{" , "("]
        for i in range(len(s)):
            if (s[i] in lst):
                stack.append(s[i])
            else:
                if(stack):
                    value = stack.pop()
                    if(s[i] == "]"):
                        if(value != "["):
                            return False
                    if(s[i] == "}"):
                        if(value != "{"):
                            return False 
                    if(s[i] == ")"):
                        if(value != "("):
                            return False 
                else:
                    #this signify if we will encounter closing bracket first before opening bracket
                    if(s[i] == "}" or s[i] == "]" or s[i] == ")"):
                        return False
        if(stack):
            return False
        else:
            return True
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s=list(s)
        # stack=[]
        # lst=["[","{","("]
        # for i in range(len(s)):
        #     if (s[i] in lst):
        #         stack.append(s[i])
        #     else:
        #         if (stack):
        #             st=stack.pop()
        #             if st == "[":
        #                 if (s[i] != "]"):
        #                     return False
        #             if (st == "{"):
        #                 if (s[i] != "}"):
        #                     return False
        #             if (st == "("):
        #                 if (s[i] != ")"):
        #                     return False
        #         else:
        #             if(s[i] == "}" or s[i] == ")" or s[i] == "]"):
        #                 return False
        # if (stack):
        #     return False
        # else:
        #     return True
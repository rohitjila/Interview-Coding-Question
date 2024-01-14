class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = Counter(words[0])
    
        # Iterate over each word starting from the second word
        for word in words[1:]:
            # Update common_counts with the minimum count for each character
            common_counts &= Counter(word)

        # Build the result list based on the minimum count for each character
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)

        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force
        # common_char = []
        # #isme hmlog sabse pehle first word ko rakh lenge 
        # for char in words[0]:
        #     #phir aage jitna bhi words hai uska comparison karenge ki kya ye character saare me hai ki nahi
        #     if all(char in word for word in words[1:]):
        #         #hai to ans me append kar denge
        #         common_char.append(char)
        #         #yaha kya ho raha hai jo character answer aa ja raha hai usko saare words me se hata rahe hai taaki
        #         #phir se wo repeat na ho.
        #         words = [word.replace(char,'',1) for word in words]
        # return common_char
    
    
    #T.C : O(N * M) (N = length of single words , M = length of complete array)
    #S.C : O(1)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
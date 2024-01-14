class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []
    
        # Iterate over each character in the first word
        for char in words[0]:
            # Check if the character is present in all other words
            if all(char in word for word in words[1:]):
                # If yes, add it to the common_chars list
                common_chars.append(char)

                # Remove the first occurrence of the character from all words
                words = [word.replace(char, '', 1) for word in words]

        return common_chars

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
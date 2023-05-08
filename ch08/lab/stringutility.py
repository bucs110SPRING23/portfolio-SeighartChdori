class StringUtility :
    
    def __init__(self, string) :
        self.string = string
   
    def __str__(self) :
        return(self.string)

    def vowels(self) :

        count = 0

        #Adds a single count for every vowel in the word
        for i in self.string :

            if i in "aeiou" :
                count += 1

            if count >= 5 :
                return("many")
        
        
        return str(count)
    
    def bothEnds(self) :
        
        word = "" 
        if len(self.string) <= 2 : # Returns nothing if the length is less than 2
            return ""
        else :
            for i in range(2) :
                word = word + self.string[i] # Adds the first two letters into the new string
            
            for i in reversed(range(1,3)) :
                word = word + self.string[-i] # Adds the last two letters into the new string

        return word
    
    def fixStart(self) :

        if len(self.string) <= 1 :
            return self.string 
        else :
            for i in self.string :

                first_letter = self.string[0] # Stores the first letter
                string = ""

                for i in (range(1,len(self.string))) : # Creates a new string without the first letter
                    string = string + self.string[i]

                new_string = string.replace(self.string[0],"*") # Replaces the new string with *

                return first_letter +new_string # Returns the first letter with the new string
            

    def asciiSum(self) :
        sum = 0

        if len(self.string) <= 1 :
            return 0
        else :
            for i in self.string :

                for i in range(len(self.string)) :
                    sum += ord(self.string[i])
                
                return sum
            
    def cipher(self) :

        new_word = ""

        for i in self.string :
            if i.isupper() :
                new_word = new_word + chr((ord(i) - ord("A") + len(self.string)) % 26 + ord("A"))
            elif i.islower() :
                new_word = new_word + chr((ord(i) - ord("a") + len(self.string)) % 26 + ord("a"))
            else :
                new_word = new_word + chr(ord(i))

        return new_word
    

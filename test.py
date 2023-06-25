def duplicate_encode(word):
    # word = "".join([w for w in word if not w.isupper()])
    word = word.lower()
    duplicate_chars = []
    new_word = ""
    
    for c in word:        
        if word.count(c) > 1:
            duplicate_chars.append(c)
            
    for c in word:
        if c in duplicate_chars:
            new_word += ")"
        else: 
            new_word += "("
            
    return new_word
        


duplicate_encode("recede") #"()()()"
duplicate_encode("Success") #())())","should ignore case")
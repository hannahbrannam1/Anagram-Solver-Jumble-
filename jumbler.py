"""jumbler:  List dictionary words that match an anagram.
2022-09-28 by Hannah Brannam

Credits: 
A. Nother Student, And Another:  Sketched pseudocode together
Our Friend:  Helped debug
"""
# DICT = "shortdict.txt"
DICT = "dict.txt" 

def find(anagram: str):
  """Print words in DICT that match anagram.
  
  >>> find("AgEmo")
  omega
  
  >>> find("nosuchword")

  >>> find("alpha")
  alpha

  >>> find("KAWEA")
  awake
  
  """
  dict_file = open(DICT, "r")
  for line in dict_file:
        word = line.strip()
        if normalize(word) == normalize(anagram):
            print(word)
            
def normalize(word: str) -> list[str]:
     """Returns a list of characters that is canonical for anagrams.
    
    >>> normalize("gamma") == normalize("magam")
    True
    
    >>> normalize("MAGAM") == normalize("gamma")
    True
    
    >>> normalize("KAWEA") == normalize("awake")
    True
    
    >>> normalize("KAWEA") == normalize("gamma")
    False
    """
     letters = word.lower()
     letters = sorted(letters)
     return letters
    
def main(): 
    anagram = input("Anagram to find> ")
    find(anagram)

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    #print("Doctests complete!")
    
    

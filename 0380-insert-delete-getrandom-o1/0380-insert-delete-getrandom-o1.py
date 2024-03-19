from random import choice
class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.add(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        else:
            self.s.remove(val)
            return True
        

    def getRandom(self) -> int:
        random_values = choice(tuple(self.s))
        return random_values
        #to get the randon_value from set we have to import random then call random.choice and convert the 
        #set into tuple because choice only works with tuples in this way we can get the random values.
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
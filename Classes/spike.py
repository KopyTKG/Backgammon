from Core.stack import Stack

class Spike:
    def __init__(self, stones=[]): 
        self.__stones = Stack(stones)
    
    @property
    def stones(self) -> List:
        return self.__stones

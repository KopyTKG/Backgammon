from Core.stack import Stack

class Stone():
    def __init__(self, currentLocation, color: str):
        self._location = currentLocation
        self._color = color
        
        self._locationMemory = Stack()
    
    @property    
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location) -> None:
        self._locationMemory.push(self._location)
        self._location = location
    
    @property
    def locations(self):
        return self._locationMemory
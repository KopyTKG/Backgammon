from typing import Any, List

class Stack:
    def __init__(self, start=[]):
        self.__memory = start

    def push(self, item) -> None:
        self.__memory.append(item)

    def pop(self) -> Any:
        return self.__memory.pop(len(self.__memory)-1)

    def peek(self) -> Any:
        return self.__memory[-1]

    def isEmpty(self) -> bool:
        return not self.__memory

    def __len__(self) -> int:
        return len(self.__memory)
    
    def __str__(self) -> str:
        return str(self.__memory)

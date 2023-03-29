from typing import Any, List

class Stack:
    def __init__(self, start=[]):
        self._memory = start

    def push(self, item) -> None:
        self._memory.append(item)

    def pop(self) -> Any:
        return self._memory.pop(-1)

    def peek(self) -> Any:
        return self._memory[-1]

    def isEmpty(self) -> bool:
        return not self._memory

    def __len__(self) -> int:
        return len(self._memory)
    
    def __str__(self) -> str:
        return str(self._memory)

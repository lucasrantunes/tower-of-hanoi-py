from rich import print
from rich import inspect
from stack import Stack
from disk import Disk

class Controller:


    def __legal_move(self, stacks, current_stack, target_stack) -> bool:
        if stacks[current_stack].get_size() > 0:
            if stacks[target_stack].get_size() > 0:
                if stacks[target_stack].peek_top().get_width() > stacks[current_stack].peek_top().get_width():
                    return True
                else:
                    print("Invalid move: attempt to put a large disk on top of a small one [2].")
                    return False
            else:
                return True
        else:
            print("Invalid move: actual stack is empty [1].")
            return False

    def move_disk(self, stacks, current_stack, target_stack):
        if self.__legal_move(stacks, current_stack, target_stack):
            disk = stacks[current_stack].remove_top()
            stacks[target_stack].push_back(disk)
            print(f"    Stack[0]: {stacks[0].stack_status()}")
            print(f"    Stack[1]: {stacks[1].stack_status()}")
            print(f"    Stack[2]: {stacks[2].stack_status()}")
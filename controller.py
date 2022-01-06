from stack import Stack
from disk import Disk

class Controller:


    def __legal_move(self, stacks, current_stack, target_stack) -> int:
        if stacks[current_stack].size() > 0:
            if stacks[target_stack].size() > 0:
                if stacks[target_stack].peek_top().get_width() > stacks[current_stack].peek_top().get_width():
                    return 1
                else:
                    print("Invalid move: attempt to put a large disk on top of a small one.")
                    return 0
            else:
                return 1
        else:
            print("Invalid move: actual stack is empty.")
            return 0

    def move_disk(self, stacks, current_stack, target_stack):
        if self.__legal_move(stacks, current_stack, target_stack) == 1:
            disk = stacks[current_stack].remove_top()
            stacks[target_stack].push_back(disk)
            return 1
        else:
            return 0

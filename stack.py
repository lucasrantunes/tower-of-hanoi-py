from disk import Disk 
class Stack:
    def __init__(self, size: int = 0):
        self.disks = []

        # insert disks in the stack
        if size > 0 :
            for width in range(size, 0, -1):
                self.disks.append(Disk(width))


    def get_size(self):
        return len(self.disks)


    def peek_top(self):
        return self.disks[self.get_size() - 1]
    

    def remove_top(self):
        disk = self.disks[self.get_size() - 1]
        self.disks.pop()
        return disk

    
    def push_back(self, disk):
        self.disks.append(disk)


    def stack_status(self):
        return self.disks
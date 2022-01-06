from disk import Disk 
class Stack:
    def __init__(self, size: int = 0):
        self.size = size
        self.disks = []

        # insert disks in the stack
        if self.size > 0 :
            for width in range(size, 0, -1):
                self.disks.append(Disk(width))


    def get_size(self):
        return self.size


    def peek_top(self):
        return self.disks[self.size - 1]
    

    def remove_top(self):
        disk = self.disks[self.size - 1]
        self.disks.pop()
        self.size = self.size - 1
        return disk

    
    def push_back(self, disk):
        self.disks.append(disk)
        self.size += 1


    def stack_status(self):
        return self.disks
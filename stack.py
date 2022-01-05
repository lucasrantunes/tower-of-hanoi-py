from disk import Disk


from disk import Disk 
class Stack:
    def __init__(self, num_disks: int = 0):
        self.num_disks = num_disks
        self.disks = []
        for width in range(1,num_disks+1):
            self.disks.append(Disk(width))
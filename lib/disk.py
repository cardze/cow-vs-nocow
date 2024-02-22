from .data import Data

class Disk:
    datas = []
    is_cow = False
    
    def __init__(self, cow:bool) -> None:
        self.is_cow = cow
        print("Disk object created")
    
    def __str__(self) -> str:
        ret = []
        for data in self.datas:
            ret.append(str(data))
        return str(ret)

    def nocow(self, data, index:int):
        self.datas[index] = data
        return index
    
    def cow(self, data, index:int):
        ret = self.write(data)
        self.datas[index].mark_as_deleted()
        # return the new index
        return ret
    
    def find_free_space(self):
        for i in range(len(self.datas)):
            if self.datas[i].deleted:
                return i
        return -1
    
    def write(self, data:Data):
        new_space = self.find_free_space()
        if new_space != -1:
            self.datas[new_space] = data
            return new_space
        else:
            self.datas.append(data)
            return len(self.datas) - 1

    def read(self, index:int):
        return self.datas[index]
    
    def update(self, data, index:int):
        if self.is_cow:
            return self.cow(data, index)
        return self.nocow(data, index)

    def format_disk(self):
        self.datas = []
        print("Disk formatted")
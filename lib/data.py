

class Data:
    deleted = False
    data = None
    def __init__(self, data) -> None:
        self.data = data
        self.deleted = False

    def __str__(self) -> str:
        return str(self.data)
    
    def mark_as_deleted(self):
        self.deleted = True

# TODO 1: Add a metadata attribute to the Data class.
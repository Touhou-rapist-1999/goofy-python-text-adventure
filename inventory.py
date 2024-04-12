class item:
  def __init__(self, name):
    self.name = name

class inv:
    def __init__(self):
        self.items = []
    def giveitem(self, item):
        self.items.append(item.name)
    def removeitem(self, itemname):
        self.items.remove(itemname)
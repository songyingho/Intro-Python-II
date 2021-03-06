# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def drop_item(self, item):
        self.items.remove(item)
class Room():
    def __init__(self):
        self.linked_rooms={}
        self.character=None
        self.item=None
    def set_description(self,room_description):
        self.description=room_description
    def get_description(self):
        return self.description
    def set_name(self,room_name):
        self.name=room_name
    def get_name(self):
        return self.name
    def set_character(self,character):
        self.character=character
    def get_character(self):
        return self.character
    def set_item(self,item):
        self.item=item
    def get_item(self):
        return self.item
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction]=room_to_link
    def get_details(self):
        print(self.name)
        print('---------------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)
        print('            ')
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you can't move there")
            return self
        
class Items():
    def description(self,item_description):
        self.description=item_description
    def name(self,item_name):
        self.name=item_name
    def moving(self,new_room):
        self.room=new_room
        return self.room
    def get_details(self):
        print(self.name,self.description,self.room)

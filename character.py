class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        #self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def set_weakness(self,weakness):
        self.weakness=weakness
        
    def get_weakness(self):
        return self_weakness
    
    def fight(self,weapon):
        if weapon==self.weakness:
            print('You fend '+ self.name + ' with ' + weapon)
            return True
        else:
            print(self.name + ' crushes you' )
            return False 
    
class Enemy(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.weakness=None
        
    def steal(self,stealed_stuff):
        print('hey,you stealed my '+ stealed_stuff)
    
class Friend(Character):
    def __init__(self, char_name,char_description):
        super().__init__(char_name,char_description)
        
    def hugging(self):
        print('You have no choise, I will hug you!')
   

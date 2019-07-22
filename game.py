from room import Room
from room import Items
from character import Enemy,Friend

#making kitchen
kitchen=Room()
kitchen.set_description('A dank and dirty room buzzing with flies.')
kitchen.get_description()
kitchen.set_name('Kitchen')
kitchen.get_name()
#making dinning hall
dinning_hall=Room()
dinning_hall.set_description('A large room with ornate golden decorations on every wall')
dinning_hall.get_description()
dinning_hall.set_name('Dinning hall')
dinning_hall.get_name()
#making ballroom
ballroom=Room()
ballroom.set_description('des. of a ballroom.')
ballroom.get_description()
ballroom.set_name('Ballroom')
ballroom.get_name()
#making a connection 
kitchen.link_room(dinning_hall,'south')
dinning_hall.link_room(kitchen,'north')
dinning_hall.link_room(ballroom,'west')
ballroom.link_room(dinning_hall,'east')
#making items
chair=Items()
chair.name('chair')
chair.description('des. of a chair')
hammer=Items()
hammer.name('hamer')
black_lipstick=Items()
black_lipstick.name('black lipstick')
kitchen.set_item(hammer)
dinning_hall.set_item(black_lipstick)

#making caracters

dave=Enemy('Dave','smelly zombie')
dave.set_conversation('eh....brains...yamy')
dave.set_weakness('hammer')

sam=Friend('Sam', 'I am perfect girl')
sam.set_conversation('How are you, darling?')
sam.set_weakness('black lipstick')



#game body
current_room=kitchen
dinning_hall.set_character(dave)
ballroom.set_character(sam)
backpack=[]
dead=False

while dead==False:
    print('\n')
    current_room.get_details()
    #command that allows to enter other rooms
    command=input('>  ')
    if command in ['south','north','west','east']:
        current_room=current_room.move(command)

    #command that allows to take things in room
    room_item=current_room.get_item()
    if command=='take':
        backpack.append(room_item)
        print('Now you have '+ room_item.name )
        current_room.set_item=None
        
    #command that allows to interact with other caracters
    inhabbitant=current_room.get_character()
    if inhabbitant is not None:
        inhabbitant.describe()
        if command=='talk':
            inhabbitant.talk()
        elif command=='fight':
            print('What you would like to fight with ')
            weapoon=input()
            if weapoon in backpack:
                inhabbitant.fight(weapoon)
                if inhabbitant.fight(weapoon)==True:
                    print('continue game')
                else:
                     print('endgame')
                     dead=True
            else:
                print('Sorry, you do not have correct weapoon')
                dead=True
    elif inhabbitant is None and command=='talk' :
        print('You hane no one to talk with')
    elif inhabbitant is None and command=='fight':
        print('You have no one to fight with')
        
    
        
        
        





        

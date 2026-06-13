class World:
    def __init__(self):
        self.size = 5
        self.agent_position = [2,2]
        self.key_position = [1,1]
        self.door_position = [0,4]
        self.has_key = False
        self.door_open = False

    def show_world(self):
        for row in range(self.size):
            line=""
            for col in range(self.size):
                position = [row, col]

                if position == self.agent_position:
                    line+='A'
                elif position == self.key_position and not self.has_key:
                    line+= 'K'
                elif position == self.door_position and not self.door_open:
                    line += 'D'
                else:
                    line+='.'
            print(line)

    def move_agent(self, directions):
        row = self.agent_position[0]
        col = self.agent_position[1]

        if directions =='up':
            row -=1
        elif directions =='down':
            row +=1
        elif directions == 'left':
            col -=1
        elif directions == 'right':
            col +=1
        
        if 0<=row < self.size and 0<=col <self.size:
            self.agent_position = [row,col]
            self.check_current_position()
        else:
            print('You cannot move outside the world')

    def check_current_position(self):
        if self.agent_position == self.key_position and not self.has_key:
            self.has_key = True
            print('Key pick up')

        if self.agent_position == self.door_position and not self.door_open:
            self.door_open = True
            print("Door opened! Goal complete.")

    def get_observation(self):
        return{
            'agent_position':self.agent_position, 'key_position': self.key_position, 'door_position': self.door_position,
            'has_key': self.has_key, 'door_open': self.door_open
        }



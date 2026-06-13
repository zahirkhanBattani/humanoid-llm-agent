class Agent:


    def  choose_action(self, observation):
        agent_row, agent_col = observation['agent_position']
        key_row, key_col = observation['key_position']
        door_row, door_col = observation['door_position']
        has_key =observation['has_key']

        if not has_key:
            target_row = key_row
            target_col = key_col

        else:
            target_row = door_row
            target_col = door_col

        if agent_row> target_row:
            return 'up'
        elif agent_row <target_row:
            return 'down'
        elif agent_col> target_col:
            return 'left'
        elif agent_col < target_col:
            return 'right'
        else:
            return 'wait'
        
        
        


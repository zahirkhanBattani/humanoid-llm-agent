from world import World
from agent import Agent
from llm_agent import LLMAgent

world = World()
# agent = Agent()
agent = LLMAgent()


world.show_world()
print(world.get_observation())
steps = 0
max_steps = 20

while not world.door_open and steps <max_steps:
    observation = world.get_observation()
    action = agent.choose_action(observation)
    print('Agent choose:', action)
    world.move_agent(action)
    world.show_world()
    steps +=1

if world.door_open:
    print("successful! Goal Achieved")
else:
    print('Stopped: Max steps reached')



# print('Moving up...')
# world.move_agent("up")
# world.show_world()

# print ('Moving left...')
# world.move_agent("left")
# world.show_world()

# print ('MOving up...')
# world.move_agent('up')
# world.show_world()

# print('MOving right...')
# world.move_agent('right')
# world.show_world()

# print('MOving right...')
# world.move_agent('right')
# world.show_world()

# print('MOving right...')
# world.move_agent('right')
# world.show_world()


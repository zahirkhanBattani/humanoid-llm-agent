import os
from dotenv import load_dotenv
from openai import OpenAI
from agent import Agent


class LLMAgent:

    def __init__(self):
        load_dotenv()
        print("LLMAgent is active")
        self.client = OpenAI()
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')

        # Backup rule-based agent
        # If OpenAI fails, our project will still work
        self.rule_agent = Agent()
        self.allowed_actions = ['up', 'down', 'right', 'left']


    def choose_action(self, observation):

        prompt = f"""You are controlling an agent in a 5x5 grid world.

        The only actions you are allowed to return are:
        up, down, left, right

        Important:
        - There is no "open" action.
        - The door opens automatically when the agent reaches the door with the key.
        - If has_key is False, move towards the key.
        - If has_key is True, move towards the door.
        - Return exactly one word only.

        Current observation:
        {observation}

        Valid response examples:
        up
        down
        left
        right

        Return only one action from the allowed actions.
        """

        try:
            response = self.client.responses.create(
                model = self.model,
                instructions='Return exactly one word only: up, down, left, or right. Never return open',
                input= prompt, max_output_tokens=20,
            )
            #action = response.output_text.strip().lower()
            raw_action = response.output_text.strip().lower()
            print('LLM raw responses:', raw_action)
            action = self.extract_action(raw_action)
            print('final action:', action)
            if action:
                return action
            
            print("Invalid LLM action. Using rule agent instead.")
            return self.rule_agent.choose_action(observation)
        except Exception as error:
            print('LLM error:', error)
            print('using rule base LLM instead.')
            return self.rule_agent.choose_action(observation)



        #print(prompt)
    def extract_action(self, text):
        text = text.strip().lower()

        for action in self.allowed_actions:
            if action in text:
                return action
        
        return None
    
        
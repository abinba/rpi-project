import openai

from core.config import OPENAI_API_KEY, OPENAI_MAX_TOKENS, OPENAI_ENGINE


class AI:
    """
    Class that retrieves the information about conditions status of
    whether conditions are good or bad for people located there.
    """
    def __init__(self):
        self.client = openai
        self.client.api_key = OPENAI_API_KEY

    @staticmethod
    def generate_prompt(parameters):
        return f"""
            The temperature is {parameters["temperature"]}, the humidity is {parameters["humidity"]}, 
            and the pressure is {parameters["pressure"]}. Are the conditions bad or good for a person located
            in those conditions? 
        """

    def get_conditions_status(self, prompt):
        response = self.client.Completion.create(
            engine=OPENAI_ENGINE,
            prompt=prompt,
            max_tokens=OPENAI_MAX_TOKENS,
        )

        return response["choices"][0]["text"]

import openai

from core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


class AI:
    """
    Class that retrieves the information about conditions status of
    whether conditions are good or bad for people located there.
    """
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def generate_prompt(self):
        return f"""
            The temperature is {self.temperature}, the humidity is {self.humidity}, 
            and the pressure is {self.pressure}. Are the conditions bad or good for a person located
            in those conditions? 
        """

    @staticmethod
    def get_conditions_status(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500,
        )

        return response["choices"][0]["text"]

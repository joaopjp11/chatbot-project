# digital_twin/digital_twin.py

from .person import Person

class DigitalTwin:
    def __init__(self, person: Person):
        self.person = person

    def build_prompt(self, user_input: str) -> str:
        """
        Cria prompt para o LLM com base no perfil e pergunta do utilizador.
        """
        prompt = (
            f"Tu és {self.person.name}, com o seguinte perfil:\n"
            f"{self.person.profile_summary()}\n\n"
            f"Responde à seguinte pergunta da forma que {self.person.name} responderia:\n"
            f"Pergunta: {user_input}\nResposta:"
        )
        return prompt

    def __repr__(self):
        return f"<DigitalTwin of {self.person.name}>"

# digital_twin/person.py

class Person:
    def __init__(self, name: str, age: int, nationality: str, personality: str, profession: str, style: str = "normal"):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.personality = personality
        self.profession = profession
        self.style = style

    def profile_summary(self) -> str:
        return (
            f"Nome: {self.name}. Idade: {self.age}. Nacionalidade: {self.nationality}. "
            f"Personalidade: {self.personality}. Profissão: {self.profession}. "
            f"Estilo de comunicação: {self.style}."
        )

    def __repr__(self):
        return f"<Person {self.name}>"

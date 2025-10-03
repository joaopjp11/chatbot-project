import os
import json
from digital_twin.person import Person

DATA_DIR = "profiles"

def load_profile(file_path: str) -> Person:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Person.from_dict(data)

def choose_profile() -> Person:
    # lista todos os ficheiros JSON 
    profiles = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    
    print("Perfis disponíveis:\n")
    for i, p in enumerate(profiles, start=1):
        nome_perfil = os.path.splitext(p)[0]
        print(f"{i}. {nome_perfil}")
    
    # pedir escolha ao utilizador
    while True:
        try:
            choice = int(input("\nEscolhe o número do perfil: "))
            if 1 <= choice <= len(profiles):
                selected = profiles[choice - 1]
                nome_perfil = os.path.splitext(selected)[0]
                print(f"\nSelecionaste: {nome_perfil}\n")
                return load_profile(os.path.join(DATA_DIR, selected))
            else:
                print("Número inválido, tenta novamente.")
        except ValueError:
            print("Por favor insere um número válido.")

if __name__ == "__main__":
    pessoa = choose_profile()

    print(f"Chatbot a representar: {pessoa.nome}\n")


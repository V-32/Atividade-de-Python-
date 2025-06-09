import random

def escolher_classe(classes):
    print("Escolha sua classe:")
    for idx, classe in enumerate(classes.keys(), 1):
        print(f"{idx}. {classe}")
    while True:
        try:
            opcao = int(input("Digite o número da classe: "))
            if 1 <= opcao <= len(classes):
                nome_classe = list(classes.keys())[opcao - 1]
                return nome_classe, classes[nome_classe].copy()
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def escolher_inimigo(inimigos):
    nome_inimigo = random.choice(list(inimigos.keys()))
    return nome_inimigo, inimigos[nome_inimigo].copy()

def batalha(jogador, nome_classe, inimigo, nome_inimigo):
    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print(f"\nSeu HP: {jogador['vida']} | HP do {nome_inimigo}: {inimigo['vida']}")
        input("Pressione Enter para atacar...")
        inimigo["vida"] -= jogador["ataque"]
        print(f"Você atacou e causou {jogador['ataque']} de dano!")

        if inimigo["vida"] <= 0:
            print(f"\nVocê derrotou o {nome_inimigo}!")
            return True

        jogador["vida"] -= inimigo["ataque"]
        print(f"O {nome_inimigo} atacou e causou {inimigo['ataque']} de dano!")

    return jogador["vida"] > 0

def main():
    classes = {
        "Guerreiro": {"vida": 100, "ataque": 15},
        "Mago": {"vida": 70, "ataque": 25},
        "Arqueiro": {"vida": 85, "ataque": 20}
    }

    inimigos = {
        "Goblin": {"vida": 50, "ataque": 10},
        "Esqueleto": {"vida": 60, "ataque": 12},
        "Orc": {"vida": 80, "ataque": 18}
    }

    nome_classe, jogador = escolher_classe(classes)
    print(f"\nVocê escolheu {nome_classe}!")

    nome_inimigo, inimigo = escolher_inimigo(inimigos)
    print(f"\nUm {nome_inimigo} apareceu!")

    venceu = batalha(jogador, nome_classe, inimigo, nome_inimigo)

    if venceu:
        print("\nParabéns! Você venceu a batalha!")
    else:
        print("\nVocê foi derrotado... Fim de jogo.")

if __name__ == "__main__":
    main()

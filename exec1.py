def status_do_personagem(vida, força, ataques):
    personagem = {
        "vida": vida,
        "força": força,
        "ataques": ataques}
    return personagem

def ataque(personagem, dano):
    personagem["vida"] -= dano
    if personagem["vida"] < 0:
        personagem["vida"] = 0
    return personagem

def inimigo(vida, força, ataques):
    inimigo = {
        "vida": vida,
        "força": força,
        "ataques": ataques}
    return inimigo


import random

saldo = 50

multiplicadores = {
    "preto": 2,
    "vermelho": 2,
    "branco": 14
}

cores_disponiveis = list(multiplicadores.keys())

print("🎰 Bem-vindo ao Mini Cassino! 🎰")
print(f"Seu saldo inicial: R${saldo:.2f}\n")

while saldo > 0:
    print(f"Seu saldo atual: R${saldo:.2f}")

    aposta = float(input("Quanto deseja apostar? R$"))

    if aposta > saldo:
        print("❌ Você não tem saldo suficiente para essa aposta!")
        continue

    cor_escolhida = input("Escolha a cor (preto/vermelho/branco): ").lower()

    if cor_escolhida not in multiplicadores:
        print("❌ Escolha inválida! Tente novamente.")
        continue

    cor_sorteada = random.choice(cores_disponiveis)
    print(f"🎲 A roleta girou... e caiu na cor: {cor_sorteada.upper()}!")

    if cor_escolhida == cor_sorteada:
        ganho = aposta * multiplicadores[cor_escolhida]
        saldo += ganho
        print(f"🎉 Você ganhou R${ganho:.2f}! Seu novo saldo: R${saldo:.2f}")
    else:
        saldo -= aposta
        print(f"😢 Você perdeu R${aposta:.2f}! Seu novo saldo: R${saldo:.2f}")

    continuar = input("Deseja continuar jogando? (s/n): ").lower()
    if continuar != "s":
        break

print("\n💰 Obrigado por jogar no Mini Cassino! 💰")
print(f"Saldo final: R${saldo:.2f}")

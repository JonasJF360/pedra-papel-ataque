import os
import subprocess
from random import choice

# Variáveis globais de controle do placar do campeonato
partidas_usuario: int = 0
partidas_maquina: int = 0

# HP que reseta a cada partida
ponto_usuario: int = 10
ponto_maquina: int = 10

def limpar() -> None:
    # Correção para o subprocess sem shell=True no Windows com listas
    comando = "clear" if os.name != "nt" else "cls"
    subprocess.run(comando, shell=True)

def verificar(escolha_usuario: int, escolha_maquina: int) -> None:
    global ponto_usuario, ponto_maquina
    
    if escolha_usuario == escolha_maquina:
        if escolha_usuario == 1:
            print("\nEmpate! Ambos escolheram Pedra.")
        elif escolha_usuario == 2:
            print("\nSintonia Total! Ambos escolheram Papel (+1 HP para ambos).")
            ponto_usuario += 1
            ponto_maquina += 1
        else:
            print("\nAniquilação mútua! Ambos escolheram Ataque (-1 HP para ambos).")
            ponto_usuario -= 1
            ponto_maquina -= 1
    else:
        # Usuário: Pedra (1) vs Máquina: Papel (2) -> Usuário vence
        if escolha_usuario == 1 and escolha_maquina == 2:
            print("\nPedra ganha! Você esmagou o papel da máquina (-1 HP para Máquina).")
            ponto_maquina -= 1
        # Usuário: Papel (2) vs Máquina: Pedra (1) -> Máquina vence
        elif escolha_usuario == 2 and escolha_maquina == 1:
            print("\nPedra ganha! A máquina esmagou o seu papel (-1 HP para Você).")
            ponto_usuario -= 1
        # Usuário: Pedra (1) vs Máquina: Ataque (3) -> Máquina vence
        elif escolha_usuario == 1 and escolha_maquina == 3:
            print("\nAtaque ganha! O ataque aéreo da máquina destruiu sua pedra (-2 HP para Você).")
            ponto_usuario -= 2
        # Usuário: Ataque (3) vs Máquina: Pedra (1) -> Usuário vence
        elif escolha_usuario == 3 and escolha_maquina == 1:
            print("\nAtaque ganha! Seu ataque aéreo destruiu a pedra da máquina (-2 HP para Máquina).")
            ponto_maquina -= 2
        # Usuário: Papel (2) vs Máquina: Ataque (3) -> Máquina vence
        elif escolha_usuario == 2 and escolha_maquina == 3:
            print("\nAtaque ganha! O ataque aéreo da máquina pulverizou seu papel (-3 HP para Você).")
            ponto_usuario -= 3
        # Usuário: Ataque (3) vs Máquina: Papel (2) -> Usuário vence
        elif escolha_usuario == 3 and escolha_maquina == 2:
            print("\nAtaque ganha! Seu ataque aéreo pulverizou o papel da máquina (-3 HP para Máquina).")
            ponto_maquina -= 3

    input("\nPressione Enter para continuar...")

def rodar_partida() -> str:
    """Executa uma partida única até que alguém zere o HP. Retorna o vencedor 'usuario' ou 'maquina'."""
    global ponto_usuario, ponto_maquina
    
    # Reseta o HP e os especiais para o início desta partida
    ponto_usuario = 10
    ponto_maquina = 10
    maquina_especial = True
    usuario_especial = True

    while ponto_usuario > 0 and ponto_maquina > 0:    
        limpar()
        print("=" * 40)
        print(f" PLACAR GERAL: Usuário {partidas_usuario} x {partidas_maquina} Máquina")
        print("=" * 40)
        print(f" HP ATUAL: Usuário {ponto_usuario} x {ponto_maquina} Máquina")
        print("-" * 40)
        print("Escolha uma opção:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Ataque")

        try:
            escolha_usuario = int(input("Digite o número da sua escolha: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            input("Pressione Enter...")
            continue

        if escolha_usuario not in [1, 2, 3]:
            print("Escolha inválida. Tente novamente.")
            input("Pressione Enter...")
            continue

        escolha_maquina = choice([1, 2, 3])
        verificar(escolha_usuario, escolha_maquina)

        # Gatilhos de Ataque Especial (Modo Fúria) executados imediatamente após a rodada
        if ponto_maquina <= 5 and ponto_maquina > 0 and maquina_especial:
            limpar()
            print("🚨 MÁQUINA ATIVOU O ATAQUE ESPECIAL! 🚨")
            print("Ela recuperou +2 HP e te causou -1 de dano!")
            ponto_usuario -= 1
            ponto_maquina += 2
            maquina_especial = False
            input("\nPressione Enter para continuar...")

        if ponto_usuario <= 5 and ponto_usuario > 0 and usuario_especial:
            limpar()
            print("🔥 VOCÊ ATIVOU O ATAQUE ESPECIAL! 🔥")
            print("Você recuperou +2 HP e causou -1 de dano na máquina!")
            ponto_maquina -= 1
            ponto_usuario += 2
            usuario_especial = False
            input("\nPressione Enter para continuar...")

    # Define o vencedor desta partida específica
    if ponto_usuario > ponto_maquina:
        return "usuario"
    else:
        return "maquina"

def campeonato() -> None:
    global partidas_usuario, partidas_maquina
    
    limpar()
    print("====== BEM-VINDO AO CAMPEONATO ======")
    print("Regra: Quem vencer 3 partidas primeiro será o Campeão Supremo!")
    input("Pressione Enter para começar a primeira partida...")

    # O jogo roda em loop até que alguém atinja 3 vitórias de partidas
    while partidas_usuario < 3 and partidas_maquina < 3:
        vencedor_da_partida = rodar_partida()
        
        limpar()
        if vencedor_da_partida == "usuario":
            partidas_usuario += 1
            print("🎉 Você venceu esta partida! (+1 Ponto no Placar Geral) 🎉")
        else:
            partidas_maquina += 1
            print("🤖 A máquina venceu esta partida! (+1 Ponto no Placar Geral) 🤖")
            
        print(f"\nPlacar do Campeonato: Usuário {partidas_usuario} x {partidas_maquina} Máquina")
        
        if partidas_usuario < 3 and partidas_maquina < 3:
            input("\nPressione Enter para ir para a próxima partida...")

    # Fim do campeonato
    limpar()
    print("=" * 40)
    print("          FIM DO CAMPEONATO!          ")
    print("=" * 40)
    if partidas_usuario == 3:
        print(f"🏆 PARABÉNS! Você fechou o placar em {partidas_usuario}x{partidas_maquina} e é o Campeão Supremo!")
    else:
        print(f"💀 GAME OVER! A máquina fechou o placar em {partidas_maquina}x{partidas_usuario}. Mais sorte na próxima!")
    print("=" * 40)

if __name__ == "__main__":
    campeonato()

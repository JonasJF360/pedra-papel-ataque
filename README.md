# Jogo - Pedra Papel e Ataque:
Esse é um projeto baseado no jogo "pedra, papel e tesoura".

Esse projeto foi criado a partir de um sugestão do meu amigo **Lucas Ferreira**:
> O objetivo principal é criar um jogo para pratiar meus conhecimentos em programação web.

## Tecnologias utiluzadas:
- JavaScript;
- HTML 5;
- CSS 3;
- SASS.


# ⚔️ Regras Gerais: Pedra, Papel e Ataque Aéreo (Modo Sobrevivência)


### 🏆 Condição de Vitória

• O jogo acaba quando um jogador vencer 3 partidas completas (Melhor de 3 Partidas).

### 💔 Sistema de Partida (HP)

• Cada partida começa com ambos os jogadores com 10 Pontos de Vida (HP).
• Quem perder o confronto da rodada perde 1 HP.
• A partida termina quando o HP de alguém chegar a 0. O sobrevivente ganha 1 ponto no placar geral e os HPs resetam para 10.

### ⚡ Ataque Especial

• Gatilho: Desbloqueado apenas quando o jogador atinge 5 HP ou menos.
• Uso: Pode ser usado uma única vez por partida.
• Efeito: Causa Dano Massivo se vencer o confronto da rodada.

### 📜 Tabela de Confrontos (Rodadas Normais)

| Jogada 1 | Jogada 2 | Resultado |
| --- | --- | --- |
| Ataque | Pedra | **Ataque vence** (Jogador 2 perde 1 HP) |
| Ataque | Papel | **Ataque vence** (Jogador 2 perde 1 HP) |
| Pedra | Papel | **Pedra vence** (Jogador 2 perde 1 HP) |
| Papel | Papel | **Sintonia Total** (Ambos ganham 1 HP) |
| Pedra | Pedra | **Empate** (Ninguém perde ou ganha HP) |
| Ataque | Ataque | **Aniquilação Mútua** (Ambos perdem 1 HP) |


# Jogo - Pedra Papel e Ataque:
Esse é um projeto baseado no jogo "pedra, papel e tesoura".

Esse projeto foi criado a partir de um sugestão do meu amigo **Lucas Ferreira**:
> O objetivo principal é criar um jogo para pratiar meus conhecimentos em programação web.

## Tecnologias utiluzadas:
- JavaScript;
- HTML 5;
- CSS 3;
- SASS.


# ⚔️ Regras Gerais: Pedra, Papel e Ataque Aéreo (Modo Campeonato)


### 🏆 Condição de Vitória

• O campeonato acaba quando um jogador vencer 3 partidas completas (Melhor de 3 Partidas).

### 💔 Sistema de Partida (HP)

• Cada partida começa com ambos os jogadores com 10 Pontos de Vida (HP).
• A partida termina quando o HP de um jogador chegar a 0. O sobrevivente ganha 1 ponto no placar do campeonato e os HPs de ambos resetam para 10.

### ⚡ Ataque Especial (Modo Fúria)

• Gatilho: Ativa automaticamente uma vez por partida assim que o jogador atinge 5 HP ou menos (e ainda esteja vivo).
• Efeito: Recupera +2 HP para si e causa -1 HP de dano direto no oponente.

### 📜 Tabela de Confrontos (Danos Escalonados)


| JOGADOR 1 | JOGADOR 2 | Resultado da Rodada e Impacto no HP |
| --- | --- | --- |
|Ataque | Papel	| Ataque Aéreo pulveriza Papel: Jogador 2 perde 3 HP |
|Ataque | Pedra	| Ataque Aéreo destrói Pedra: Jogador 2 perde 2 HP |
|Pedra	| Papel	| Pedra esmaga Papel: Jogador 2 perde 1 HP |
|Papel	| Papel	| Sintonia Total: Ambos os jogadores recuperam +1 HP |
|Pedra	| Pedra	| Empate: Nada acontece. Nenhum HP é alterado |
|Ataque | Ataque| 	Aniquilação Mútua: Ambos os jogadores perdem 1 HP |

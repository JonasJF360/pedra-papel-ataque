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

* **Campeão Supremo:** O primeiro jogador a vencer **3 partidas completas**.

### 💔 Sistema de Partida (HP)

* **Vida Inicial:** Cada partida começa com ambos os jogadores com **10 HP**.
* **Fim da Partida:** A partida encerra quando o HP de um jogador chega a **0**. O sobrevivente ganha **+1 ponto** no placar geral e os HPs são resetados para 10.

### ⚡ Ataque Especial (Modo Fúria)

* **Gatilho:** Ativação automática **uma única vez por partida** ao atingir **$\le 5$ HP** (estando vivo).
* **Efeito Instantâneo:** Recupera **+2 HP** para si e aplica **-1 HP** de dano direto no oponente.

### 🔄 Regra Especial: O Revide do Papel (Anti-Apelação)

* **Gatilho:** Ocorre no confronto **Ataque Aéreo vs Papel** (independente de quem escolheu cada opção).
* **Probabilidade:** Existe uma chance aleatória de **25% a 50%** de o Papel ativar o contra-ataque.
* **Efeito do Revide:** Anula totalmente o dano do Ataque Aéreo e aplica **-1 HP** no jogador que tentou atacar (*"Ops! Parece que você se cortou no papel"*).
* **Falha no Revide:** Caso o contra-ataque não seja ativado pela sorte, aplica-se a regra padrão de **-3 HP** no jogador que usou Papel.

---

### 📜 Tabela de Confrontos e Impactos de HP

| JOGADOR 1 | JOGADOR 2 | Resultado da Rodada e Impacto no HP |
| --- | --- | --- |
| **Ataque** | **Papel** | **Padrão:** Ataque pulveriza Papel *(Jogador 2 perde 3 HP)*. **Revide (25%-50% chance):** Papel anula e contra-ataca *(Jogador 1 perde 1 HP)*. |
| **Ataque** | **Pedra** | Ataque Aéreo destrói Pedra *(Jogador 2 perde 2 HP)*. |
| **Pedra** | **Papel** | Pedra esmaga Papel *(Jogador 2 perde 1 HP)*. |
| **Papel** | **Papel** | **Sintonia Total:** Ambos os jogadores recuperam **+1 HP**. |
| **Pedra** | **Pedra** | **Empate:** Nada acontece *(Nenhum HP alterado)*. |
| **Ataque** | **Ataque** | **Aniquilação Mútua:** Ambos os jogadores perdem **-1 HP**. |

---
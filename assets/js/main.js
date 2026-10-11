(App => {

    const imagens = ['papel', 'pedra', 'ataque', 'especial']

    function numeroAleatorio(inicio = 0, fim = 10) {
        if (inicio > 1) fim = (fim - inicio) + 1;
        return inicio + Math.floor((Math.random() * fim));
    }

    // Seleciona todos os cartões do jogador
    const cartoes = document.querySelectorAll('.cartao-maquina');

    cartoes.forEach(cartao => {
        cartao.addEventListener('click', () => {
            // Adiciona a classe de animação
            cartao.classList.add('balancar');

            // Remove a classe assim que a animação termina (200ms = 0.2s)
            setTimeout(() => {
                cartao.classList.remove('balancar');
            }, 200);
        });
    });



})();
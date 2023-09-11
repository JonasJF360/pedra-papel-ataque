(App => {

    const imagens = ['papel', 'pedra', 'ataque', 'ataque-especial']

    function numeroAleatorio(inicio = 0, fim = 10) {
        if (inicio > 1) fim = (fim - inicio) + 1;
        return inicio + Math.floor((Math.random() * fim));
    }


})();
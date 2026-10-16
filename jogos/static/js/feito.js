buscarEquipe = function() {
    let busca = document.getElementById('busca').value;
    let equipes = document.getElementsByClassName('card');
    let semResultado = document.getElementById('sem-resultado');

    for (let i = 0; i < equipes.length; i++) {
        let equipe = equipes[i];
        let nome = equipe.getElementsByTagName('h3')[0].innerText;

        if (nome.toLowerCase().includes(busca.toLowerCase())) {
            equipe.style.display = 'block';
            semResultado.style.display = 'none';
        } else {
            equipe.style.display = 'none';
            semResultado.style.display = 'block';
        }
    }
}
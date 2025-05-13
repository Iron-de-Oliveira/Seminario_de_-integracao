console.log("js carregado")
function coletar_dados(){
    const data_nome = document.getElementById("nome").value;
    const data_email = document.getElementById("email").value;
    const data_senha = document.getElementById("password").value;
    const data_numero = document.getElementById("telefone").value;
    const data_local = document.getElementById("localizacao").value;

    const dados_usuario = {
        nome: data_nome,
        email: data_email,
        senha: data_senha,
        numero: data_numero,
        local: data_local
    };

     fetch('http://localhost:5000/usuario', {

        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados_usuario)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Erro ao cadastrar novo usuário");
    });

    var lista = document.getElementById("form");
  
    lista.selectedIndex = 0;

    window.location.href = "login_cadastro.html"
}    
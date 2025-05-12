console.log("js carregado")
function coletar_dados(){
    const data_nome = document.getElementById("name").value;
    const data_email = document.getElementById("email").value;
    const data_senha = document.getElementById("password").value;
    const data_local = document.getElementByID("localizacao").value;

    const dados_usuario = {
        nome: data_nome,
        email: data_email,
        senha: data_senha,
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
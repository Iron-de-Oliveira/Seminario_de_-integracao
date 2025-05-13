console.log("js carregado")
function coletar_dados(){
    const data_foto = document.getElementById("file").value;
    const data_categoria = document.getElementById("Categoria").value;
    const data_condicao = document.getElementById("condicao").value;
    const data_documentacao = document.getElementById("documentacao").value;
    const data_descricao = document.getElementByID("descricao").value;

    const dados_usuario = {
        foto: data_foto,
        categoria: data_categoria,
        condicao: data_condicao,
        documentacao: data_documentacao,
        descricao: data_descricao
    };

     fetch('http://localhost:5000/produto', {

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
        alert("Erro ao cadastrar novo produto");
    });

    var lista = document.getElementById("form");
  
    lista.selectedIndex = 0;

    window.location.href = "home.html"
}    
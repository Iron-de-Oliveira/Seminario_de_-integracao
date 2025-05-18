function coletar_dados() {
    const inputArquivo = document.getElementById("arquivo");
    const arquivo = inputArquivo.files[0];

    const categoria = document.getElementById("Categoria").value;
    const condicao = document.getElementById("condicao").value;
    const descricao = document.getElementById("descricao").value;

    const reader = new FileReader();
    reader.onload = function () {
        const imagemBase64 = reader.result; // aqui está a imagem em base64

        const dados = {
            categoria: categoria,
            condicao: condicao,
            descricao: descricao,
            foto: imagemBase64,
            status: "disponível"
        };

        fetch('http://127.0.0.1:5000/produto', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao salvar no banco");
            }
            return response.json();
        })
        .then(data => {
            alert(data.message);
            document.querySelector('form').reset();
            window.location.href = "/";
        })
        .catch(error => {
            console.error("Erro:", error); 
            alert("Erro ao cadastrar novo produto.");
        });
    };

    if (arquivo) {
        reader.readAsDataURL(arquivo);  // converte a imagem em base64
    } else {
        alert("Por favor, selecione uma imagem.");
    }
}

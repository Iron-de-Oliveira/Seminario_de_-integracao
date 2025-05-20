function coletar_dados() {
    const categoria = document.getElementById("Categoria").value;
    const condicao = document.getElementById("condicao").value;
    const descricao = document.getElementById("descricao").value;
    const arquivo = document.getElementById("arquivo").files[0];

    if (!arquivo) {
        alert("Por favor, selecione uma imagem.");
        return;
    }

    const formData = new FormData();
    formData.append("foto", arquivo);
    formData.append("categoria", categoria);
    formData.append("condicao", condicao);
    formData.append("descricao", descricao);
    formData.append("status", "disponível");

    fetch("/produto", {
        method: "POST",
        body: formData,
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
}

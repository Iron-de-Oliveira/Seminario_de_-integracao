console.log("js carregado")
function coletar_dados(){

    // Captura o input de arquivo corretamente
    const inputArquivo = document.getElementById('arquivo');
    if (!inputArquivo) {
        console.error("Elemento com id 'arquivo' não encontrado.");
        alert("Erro: campo de imagem não encontrado.");
        return;
  }
    const arquivos = inputArquivo.files;
    const arquivoFoto = (inputArquivo?.files?.length > 0) ? inputArquivo.files[0] : null;



    // coletar os dados do formulário
    const categoria = document.getElementById("Categoria").value;
    const condicao = document.getElementById("condicao").value;
    const descricao = document.getElementById("descricao").value.trim();

    // Cria um FormData para enviar dados e arquivos
    const formData = new FormData();
    formData.append('categoria', categoria);
    formData.append('condicao', condicao);
    formData.append('descricao', descricao);

    if (arquivoFoto) {
        formData.append('foto', arquivoFoto);
    }

    // Envia para o backend
    fetch('http://localhost:5000/produto', {
        method: 'POST',
        body: formData
    })
         .then(response => {
        if (!response.ok) {
            throw new Error("Erro ao salvar no banco");
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
        // Limpa o formulário
        document.querySelector('form').reset();
        // Redireciona para /
        window.location.href = "/";
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Erro ao cadastrar novo produto.");
    });
}
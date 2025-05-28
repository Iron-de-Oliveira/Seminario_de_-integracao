function retornar_home(){
    window.location.href = "/"
}

function foto_perfil() {
    const arquivo = document.getElementById("file").files[0];
    const user_id = localStorage.getItem("user_id"); 

    if (!arquivo) {
        alert("Por favor, selecione uma imagem.");
        return;
    }

    const formData = new FormData();
    formData.append("foto_perfil", arquivo);

    fetch(`/usuario/${user_id}`, {
        method: "PUT",
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
        window.location.href = "perfil_usuario.html";
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Erro ao atualizar a foto de perfil.");
    });
}

function deletar(idusuario) {
    console.log("ID recebido para deletar:", idusuario); // teste no console

    if (confirm("Tem certeza que deseja deletar sua conta?")) {
        fetch(`/usuario/${idusuario}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            window.location.reload();
        })
        .catch(error => {
            console.error('Erro ao deletar conta:', error);
            alert('Erro ao deletar conta.');
        });
    }
}


function suporte(){
    window.location.href = "/suporte.html"
}
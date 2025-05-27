function retornar(){
    window.location.href = ("/")
}

function chat(){
    window.location.href = ("/chat")
}

function compartilharLink() {
  const url = window.location.href;

  // Copia o link para a área de transferência
  navigator.clipboard.writeText(url).then(() => {
    alert("Link copiado para a área de transferência!");
  }).catch(err => {
    console.error("Erro ao copiar link: ", err);
  });
}
function caminho_cadastro() {
    const url = document.getElementById("btnCadastro").dataset.urlCadastro;
    window.location.href = url;
}

document.getElementById("form").addEventListener("submit", async function(e) {
  e.preventDefault(); // impede o recarregamento da página

  const formData = new FormData(e.target);
  const email = formData.get("email");
  const senha = formData.get("senha");

  const response = await fetch("/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    body: new URLSearchParams({
      email: email,
      senha: senha
    })
  });

  if (response.redirected) {
     window.location.href = response.url;
  } else {
    const text = await response.text();
    alert("Erro no login: " + text);
  }
});
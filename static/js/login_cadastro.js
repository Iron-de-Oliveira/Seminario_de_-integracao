function caminho_cadastro(){
    window.location.href = "cadastro.html"
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
    window.location.href = "home.html"; // redireciona se o login for bem-sucedido
  } else {
    const text = await response.text();
    alert("Erro no login: " + text);
  }
});
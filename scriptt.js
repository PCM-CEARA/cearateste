document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = this.email.value;
    const password = this.password.value;

    const storedUser = JSON.parse(localStorage.getItem('user'));

    if (storedUser && email === storedUser.email && password === storedUser.password) {
        localStorage.setItem('userLogged', JSON.stringify({ email }));
        window.location.href = 'index.html'; // Redireciona para index.html
    } else {
        document.getElementById('error-message').style.display = 'block'; // Exibe mensagem de erro
    }
});

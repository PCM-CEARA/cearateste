document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = this.email.value;
    const password = this.password.value;

    const user = { email, password };
    localStorage.setItem('user', JSON.stringify(user));

    alert('Registro realizado com sucesso! Agora você pode fazer login.');
    window.location.href = 'login.html';
});

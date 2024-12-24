const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const togglePassword = document.getElementById('togglePassword');
const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');

togglePassword.addEventListener('click', () => {
    passwordInput.type = passwordInput.type === 'password' ? 'text' : 'password';
    if (togglePassword.ClassName == 'fa-eye-slash') {
        togglePassword.ClassName = 'fa-eye-slash';
    } else {
        togglePassword.ClassName = 'fa-eye-slash';
    }
});

toggleConfirmPassword.addEventListener('click', () => {
    confirmPasswordInput.type = confirmPasswordInput.type === 'password' ? 'text' : 'password';
    toggleConfirmPassword.classList.toggle('fa-eye-slash');
});

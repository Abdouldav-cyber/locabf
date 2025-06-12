(function() {
    'use strict';
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Redirection après connexion JWT
    const loginForm = document.querySelector('form[action="{% url "login" %}"]');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/api/token/', {
                method: 'POST',
                body: JSON.stringify({
                    username: formData.get('username'),
                    password: formData.get('password')
                }),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            });
            const data = await response.json();
            if (response.ok && data.redirect) {
                window.location.href = data.redirect;
            }
        });
    }
})();
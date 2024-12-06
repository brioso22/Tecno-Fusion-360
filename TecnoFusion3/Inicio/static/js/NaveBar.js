document.addEventListener('DOMContentLoaded', function () {
    const toggleSwitch = document.getElementById('toggle-switch');
    const body = document.body;

    // Comprobar el estado del modo oscuro al cargar la página
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
        toggleSwitch.classList.add('active');
    }

    // Añadir evento de clic para alternar el modo oscuro
    toggleSwitch.addEventListener('click', function () {
        toggleSwitch.classList.toggle('active'); // Cambiar la clase para mover la bolita

        // Alternar el modo oscuro en el body y guardar el estado en localStorage
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
            localStorage.setItem('darkMode', 'disabled');
        } else {
            body.classList.add('dark-mode');
            localStorage.setItem('darkMode', 'enabled');
        }
    });
});



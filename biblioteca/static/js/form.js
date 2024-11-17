document.addEventListener('DOMContentLoaded', () => {
    const showFormButton = document.getElementById('show-form');
    const modal = document.getElementById('modal');
    const formContainer = document.getElementById('form-container');
    const radioButtons = document.querySelectorAll('.radio');

    // Mostrar el modal al hacer clic en el botón "Agregar libro"
    showFormButton.addEventListener('click', () => {
        modal.classList.add('active');
    });

    // Cerrar el modal
    const closeButton = modal.querySelector('button[popovertargetaction="hide"]');
    closeButton.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    // Cargar el formulario correspondiente según la selección del radio button
    radioButtons.forEach((radio) => {
        radio.addEventListener('change', (event) => {
            const selectedType = event.target.value;
            fetch(`/?type=${selectedType}`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Indicar que es una solicitud AJAX
                },
            })
                .then((response) => response.text())
                .then((html) => {
                    formContainer.innerHTML = html; // Insertar el formulario en el contenedor
                });
        });
    });
});

document.querySelectorAll('.edit-button').forEach((button) => {
    button.addEventListener('click', (event) => {
        const libroId = event.target.dataset.libroId;
        const tipo = event.target.dataset.tipo;

        fetch(`/editar/${libroId}/${tipo}/`, {
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' },
        })
            .then((response) => response.text())
            .then((html) => {
                document.getElementById('form-container').innerHTML = html;
            });
    });
});

document.querySelectorAll('.delete-button').forEach((button) => {
    button.addEventListener('click', (event) => {
        const libroId = event.target.dataset.libroId;
        const tipo = event.target.dataset.tipo;

        if (confirm('¿Estás seguro de que deseas eliminar este libro?')) {
            fetch(`/eliminar/${libroId}/${tipo}/`, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrftoken }, 
            }).then(() => {
                location.reload(); // Recargar la página después de eliminar
            });
        }
    });
});

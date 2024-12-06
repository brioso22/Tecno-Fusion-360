// Obtener el modal y los elementos del DOM
var modal = document.getElementById("modal");
var closeModal = document.getElementById("closeModal");
var zoomableImage = document.getElementById("zoomableImage");

// Variable para controlar el estado del zoom
var zoomed = false;

// Función para abrir el modal y establecer el contenido del producto
function openModal(product) {
    // Actualiza el contenido del modal con los datos del producto
    var productName = product.querySelector("h3").innerText;
    var productDescription = product.querySelector("p").innerText;
    var productPrice = product.querySelector(".price").innerText;
    var productImageSrc = product.querySelector("img").src;

    // Asignar los valores al modal
    zoomableImage.src = productImageSrc;
    modal.querySelector("h3").innerText = productName;
    modal.querySelector("p").innerText = productDescription;
    modal.querySelector(".price").innerText = productPrice;

    // Mostrar el modal
    modal.style.display = "block";
}

document.querySelectorAll('.product-card').forEach(card => {
    card.onclick = function() {
        // Obtén el ID del producto desde el atributo de datos o cualquier otro atributo del producto
        var productoId = card.getAttribute('data-producto-id');  // Asegúrate de agregar este atributo en el HTML

        // Redirigir a la URL correspondiente para 'vista_product' con el ID del producto
        window.location.href = "/tienda/vista_product/" + productoId + "/";
    }
});

// Cerrar el modal al hacer clic en el botón de cerrar
closeModal.onclick = function() {
    modal.style.display = "none";
    resetZoom(); // Restablecer el zoom al cerrar el modal
}

// Cerrar el modal al hacer clic fuera de la ventana del modal
window.onclick = function(event) {
    // Solo cerrar el modal si el clic no es dentro del formulario de comentarios
    if (event.target == modal && !event.target.closest('form')) {
        modal.style.display = "none";
        resetZoom(); // Restablecer el zoom al cerrar el modal
    }
}

// Función para restablecer el zoom
function resetZoom() {
    zoomableImage.style.transform = "scale(1)";
    zoomed = false;
}

// Alternar el zoom al hacer clic en la imagen
zoomableImage.onclick = function() {
    zoomed = !zoomed;
    if (zoomed) {
        zoomableImage.style.transform = "scale(2)";
    } else {
        zoomableImage.style.transform = "scale(1)";
    }
};

// Ajustar la posición de zoom según el movimiento del mouse
zoomableImage.addEventListener("mousemove", function(event) {
    if (zoomed) {
        const rect = zoomableImage.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width * 100;
        const y = (event.clientY - rect.top) / rect.height * 100;
        zoomableImage.style.transformOrigin = `${x}% ${y}%`;
    }
});

// Evita que el modal se cierre cuando se haga submit en el formulario de comentario
document.getElementById("commentForm").addEventListener("submit", function(event) {
    event.stopPropagation();  // Detiene la propagación del evento hacia el modal
});


// Función para mostrar el formulario de comentarios
function toggleCommentBox() {
    var commentContainer = document.getElementById("commentContainer");
    // Alternar visibilidad
    if (commentContainer.style.display === "none" || commentContainer.style.display === "") {
        commentContainer.style.display = "block";
    } else {
        commentContainer.style.display = "none";
    }
}

// Cerrar el modal cuando el usuario haga clic fuera de la caja de contenido
window.onclick = function(event) {
    if (event.target === document.getElementById("commentModal")) {
        closeModal();
    }
}












// Función para abrir la ventana emergente
function openPopup() {
    document.getElementById('popup').style.display = 'block';  // Muestra la ventana emergente
    document.getElementById('popupOverlay').style.display = 'block';  // Muestra el fondo de la ventana emergente
}

// Función para cerrar la ventana emergente
function closePopup() {
    document.getElementById('popup').style.display = 'none';  // Oculta la ventana emergente
    document.getElementById('popupOverlay').style.display = 'none';  // Oculta el fondo
}

// Si haces clic en el fondo, también cierra la ventana emergente
document.getElementById('popupOverlay').onclick = function() {
    closePopup();
}

// Si haces clic en el botón de cerrar, también cierra la ventana emergente
document.querySelector('.close-btn').onclick = function() {
    closePopup();
}

// Llamar a openPopup() cuando el usuario haga clic en el botón de abrir carrito
document.getElementById('abrir-popup').addEventListener('click', openPopup);




document.getElementById('search-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();  // Evita el envío predeterminado del formulario
        const searchQuery = this.value;
        if (searchQuery) {
            window.location.href = `/buscar/?q=${encodeURIComponent(searchQuery)}`;
        }
    }
});




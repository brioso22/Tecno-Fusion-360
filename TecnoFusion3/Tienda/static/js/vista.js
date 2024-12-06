document.addEventListener('DOMContentLoaded', function () {
    const zoomContainer = document.querySelector('.zoom-container');
    const productImg = document.querySelector('.product-img');
    const zoomLens = document.querySelector('.zoom-lens');

    let isZoomActive = false; // Controlar si el zoom está activo o no

    zoomContainer.addEventListener('click', (e) => {
        if (isZoomActive) {
            // Si el zoom está activo, desactivarlo
            zoomLens.style.display = 'none';
            productImg.style.transform = 'scale(1)'; // Restaurar el tamaño original de la imagen
        } else {
            // Si el zoom no está activo, activarlo
            zoomLens.style.display = 'block';
            const { left, top, width, height } = zoomContainer.getBoundingClientRect();
            const x = e.clientX - left;
            const y = e.clientY - top;

            // Ajustar la posición inicial de la lente de zoom
            moveLens(x, y);
        }
        // Alternar el estado de activación del zoom
        isZoomActive = !isZoomActive;
    });

    zoomContainer.addEventListener('mousemove', (e) => {
        if (isZoomActive) {
            const { left, top, width, height } = zoomContainer.getBoundingClientRect();
            const x = e.clientX - left;
            const y = e.clientY - top;

            moveLens(x, y);

            // Calcular el porcentaje de la posición del ratón para la imagen
            const scale = 2; // Aumento del zoom (puedes ajustarlo)
            const imgWidth = productImg.width;
            const imgHeight = productImg.height;
            const lensWidth = zoomLens.offsetWidth;
            const lensHeight = zoomLens.offsetHeight;

            // Aplicar el zoom a la imagen
            productImg.style.transform = `scale(${scale})`;
            productImg.style.transformOrigin = `${(x / width) * 100}% ${(y / height) * 100}%`;
        }
    });

    zoomContainer.addEventListener('mouseleave', () => {
        if (isZoomActive) {
            zoomLens.style.display = 'none'; // Ocultar la lente de zoom cuando el ratón sale
            productImg.style.transform = 'scale(1)'; // Restaurar el tamaño de la imagen
            isZoomActive = false; // Desactivar el zoom
        }
    });

    function moveLens(x, y) {
        const lensWidth = zoomLens.offsetWidth;
        const lensHeight = zoomLens.offsetHeight;
        const zoomContainerWidth = zoomContainer.offsetWidth;
        const zoomContainerHeight = zoomContainer.offsetHeight;

        // Ajustar la posición de la lente de zoom
        let lensX = x - lensWidth / 2;
        let lensY = y - lensHeight / 2;

        // Asegurarse de que la lente no salga fuera de los límites del contenedor
        if (lensX < 0) lensX = 0;
        if (lensY < 0) lensY = 0;
        if (lensX > zoomContainerWidth - lensWidth) lensX = zoomContainerWidth - lensWidth;
        if (lensY > zoomContainerHeight - lensHeight) lensY = zoomContainerHeight - lensHeight;

        zoomLens.style.left = `${lensX}px`;
        zoomLens.style.top = `${lensY}px`;
    }
});




























// Obtener el modal y otros elementos
var modal = document.getElementById("filterModal");
var btn = document.getElementById("openModal"); // No es necesario, pero si quieres abrirlo desde un botón adicional
var span = document.getElementById("closeModal");
var applyBtn = document.getElementById("applyFilters");

// Obtener el valor del rango de precio y mostrarlo en el modal
var priceRange = document.getElementById("priceRange");
var priceValue = document.getElementById("priceValue");

priceRange.oninput = function() {
    priceValue.textContent = priceRange.value;
}

// Función para mostrar el modal
function showFilterModal() {
    modal.style.display = "block"; // Muestra el modal cuando el radio button es seleccionado
}

// Cerrar modal al hacer clic en el botón de cerrar
span.onclick = function() {
    modal.style.display = "none";
}

// Cerrar modal si el usuario hace clic fuera del contenido del modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Aplicar filtros (solo cerrar el modal por ahora)
applyBtn.onclick = function() {
    // Aquí puedes capturar los valores seleccionados y hacer algo con ellos (por ejemplo, filtrar productos)
    var selectedPrice = priceRange.value;
    var selectedBrand = document.getElementById("brand").value;

    console.log("Filtrar por precio: $" + selectedPrice + " y marca: " + selectedBrand);

    // Cerrar modal después de aplicar los filtros
    modal.style.display = "none";
}

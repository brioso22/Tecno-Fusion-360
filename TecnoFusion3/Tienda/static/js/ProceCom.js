document.addEventListener('DOMContentLoaded', function() {
    // Togglers de productos
    const productCheckboxes = document.querySelectorAll('.product-checkbox');
    const selectedProductsInput = document.getElementById('selected-products');
    
    productCheckboxes.forEach(checkbox => {
        const toggler = checkbox.closest('.toggler');
        const svgOn = toggler.querySelector('.toggler-on');
        const svgOff = toggler.querySelector('.toggler-off');
        
        function updateTogglerVisibility() {
            if (checkbox.checked) {
                svgOn.style.display = 'block';
                svgOff.style.display = 'none';
            } else {
                svgOn.style.display = 'none';
                svgOff.style.display = 'block';
            }
            
            // Actualizar el campo hidden con los productos seleccionados
            updateSelectedProducts();
        }
        
        checkbox.addEventListener('change', function() {
            updateTogglerVisibility();
        });
        
        updateTogglerVisibility();
        
        const label = toggler.querySelector('label');
        label.addEventListener('click', function(e) {
            e.preventDefault();
            checkbox.checked = !checkbox.checked;
            updateTogglerVisibility();
        });
    });

    // Función para actualizar el campo hidden de productos seleccionados
    function updateSelectedProducts() {
        const selectedProducts = Array.from(productCheckboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);
        
        selectedProductsInput.value = selectedProducts.join(',');
    }

    // Métodos de pago
    const onlinePaymentRadio = document.getElementById('payment-online');
    const onlinePaymentForm = document.getElementById('online-payment-form');
    const transferPaymentRadio = document.getElementById('payment-transfer');
    const transferForm = document.getElementById('transfer-form');
    const cashPaymentRadio = document.getElementById('payment-cash');

    // Función para mostrar el formulario correspondiente
    function updatePaymentFormVisibility() {
        // Mostrar/ocultar el formulario de pago en línea
        onlinePaymentForm.style.display = onlinePaymentRadio.checked ? 'block' : 'none';

        // Mostrar/ocultar el formulario de transferencia bancaria
        transferForm.style.display = transferPaymentRadio.checked ? 'block' : 'none';
    }

    // Inicializar el estado de los formularios
    updatePaymentFormVisibility();

    // Añadir eventos a las opciones de método de pago
    [onlinePaymentRadio, transferPaymentRadio, cashPaymentRadio].forEach(radio => {
        radio.addEventListener('change', updatePaymentFormVisibility);
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const carritoLista = document.querySelector('#carrito-lista tbody');

    if (!carritoLista) {
        console.error('No se encontró el elemento tbody dentro de "carrito-lista"');
        return;
    }

    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    if (carrito.length === 0) {
        carritoLista.innerHTML = '<tr><td colspan="4" style=" color:#fff;"  >El carrito está vacío</td></tr>';
    } else {
        carrito.forEach(juego => {
            const fila = document.createElement('tr');
            fila.innerHTML = `
                <td style=" color:#fff;">${juego.nombre}</td>
                <td style=" color:#fff;">${juego.precio}</td>
                <td><button class="eliminar-juego" class="button-B" data-id="${juego.id}">Eliminar</button></td>
            `;
            carritoLista.appendChild(fila);
        });

        
        document.querySelectorAll('.eliminar-juego').forEach(boton => {
            boton.addEventListener('click', eliminarJuego);
        });
    }

    const botonVaciarCarrito = document.getElementById('vaciar-carrito');
    botonVaciarCarrito.addEventListener('click', vaciarCarrito);
});

function eliminarJuego(event) {
    const juegoId = event.target.getAttribute('data-id');
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    carrito = carrito.filter(juego => juego.id != juegoId);
    localStorage.setItem('carrito', JSON.stringify(carrito));
    location.reload();
}

function vaciarCarrito() {
    localStorage.removeItem('carrito');
    location.reload(); 
}


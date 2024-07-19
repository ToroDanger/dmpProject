var swiper = new Swiper(".mySwiper-1",{
    slidesPerView:1,
    spaceBetween: 30,
    loop:true,
    pagination:{
        el:".swiper-pagination",
        clickable:true,
    },
    navigation: {
        nextEl:".swiper-button-next",
        prevEl:".swiper-button-prev",
    }

});

var swiper = new Swiper(".mySwiper-2",{
    slidesPerView:3,
    spaceBetween: 20,
    loop:true,
    loopFillGroupWithBlank:true,
    navigation: {
        nextEl:".swiper-button-next",
        prevEl:".swiper-button-prev",
    },
    breakpoints:{
        0:{
            slidesPerView:1,
        },
        520:{
            slidesPerView:2,
        },
        950:{
            slidesPerView:3,
        }
    }

});

let tabInputs = document.querySelectorAll(".tabInput");

tabInputs.forEach(function(input){

    input.addEventListener('change', function(){
        let id = input.ariaValueMax;
        let thisSwiper = document.getElementById('swiper' + id);
        thisSwiper.swiper.update();
    })

});


// let loadMoreBtn = document.querySelector('#load-more');
// let currentItem = 4;

// loadMoreBtn.onclick =() =>{
//     let boxes = [...document.querySelectorAll('.box-container .box')];
//     for(var i = currentItem; i < currentItem + 4; i++){
//         boxes[i].style.display = 'inline-block';
//     }
//     currentItem += 4;
//     if(currentItem >= boxes.length){
//         loadMoreBtn.style.display = 'none'
//     }
// };












//Carrito

// document.addEventListener('DOMContentLoaded', () => {
//     const carrito = document.getElementById('carrito');
//     const elementos1 = document.querySelector('.card-container');
//     const lista = document.querySelector('#lista-carrito tbody');
//     const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

//     cargarEventListeners();

//     function cargarEventListeners() {
//         elementos1.addEventListener('click', comprarElemento);
//         carrito.addEventListener('click', eliminarElemento);
//         vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
//     }

//     function comprarElemento(e) {
//         e.preventDefault();

//         if (e.target.classList.contains('agregar-carrito')) {
//             const elemento = e.target.parentElement;
//             console.log("Elemento agregado al carrito:", elemento); 
//             leerDatosElemento(elemento);
//         }
//     }

//     function leerDatosElemento(elemento) {
//         const infoElemento = {
//             imagen: elemento.querySelector('img').src,
//             titulo: elemento.querySelector('span').textContent,
//             precio: elemento.querySelector('.precio').textContent,
//             id: elemento.querySelector('button').getAttribute('data-id')
//         }
//         console.log("Datos del elemento:", infoElemento); 
//         insertarCarrito(infoElemento);
//     }

//     function insertarCarrito(elemento) {
//         console.log("Insertando en el carrito:", elemento);
//         const row = document.createElement('tr');
//         row.innerHTML = `
//             <td>
//                 <img src="${elemento.imagen}" width=100 />
//             </td>
//             <td>
//                 ${elemento.titulo}
//             </td>
//             <td>
//                 ${elemento.precio}
//             </td>
//             <td>
//                 <a href="#" class="borrar" data-id="${elemento.id}">X</a>
//             </td>
//         `;

//         lista.appendChild(row);
//     }

//     function eliminarElemento(e) {
//         e.preventDefault();

//         if (e.target.classList.contains('borrar')) {
//             e.target.parentElement.parentElement.remove();
//         }
//     }

//     function vaciarCarrito() {
//         while (lista.firstChild) {
//             lista.removeChild(lista.firstChild);
//         }
//         return false;
//     }
// });
// document.addEventListener('DOMContentLoaded', () => {
//     const botonesAgregar = document.querySelectorAll('.agregar-carrito');

//     botonesAgregar.forEach(boton => {
//         boton.addEventListener('click', (event) => {
//             const juegoId = event.target.getAttribute('data-id');
//             agregarAlCarrito(juegoId);
//         });
//     });
// });

// function agregarAlCarrito(juegoId) {
//     // Ejemplo de información de los juegos
//     const juegos = {
//         1: { id: 1, nombre: "Nombre del Juego 1", detalle: "Detalle del Juego 1", precio: "10.00" },
//         2: { id: 2, nombre: "Nombre del Juego 2", detalle: "Detalle del Juego 2", precio: "15.00" },
//         // Agrega más juegos según sea necesario
//     };

//     let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

//     const juegoSeleccionado = juegos[juegoId];
//     if (!juegoSeleccionado) {
//         console.error(`Juego con ID ${juegoId} no encontrado.`);
//         return;
//     }
    
//     if (!carrito.some(juego => juego.id == juegoId)) {
//         carrito.push(juegoSeleccionado);
//         localStorage.setItem('carrito', JSON.stringify(carrito));
//         alert("Juego agregado al carrito");
//     } else {
//         alert("Este juego ya está en el carrito");
//     }
// }

document.addEventListener('DOMContentLoaded', () => {
    const botonesAgregar = document.querySelectorAll('.agregar-carrito');

    botonesAgregar.forEach(boton => {
        boton.addEventListener('click', (event) => {
            const juegoId = event.target.getAttribute('data-id');
            console.log(`Botón clicado con ID: ${juegoId}`);
            agregarAlCarrito(juegoId);
        });
    });
});

function agregarAlCarrito(juegoId) {
    console.log(`Buscando el juego con ID: ${juegoId}`);
    
    const card = document.querySelector(`.card-1[data-id="${juegoId}"]`);
    console.log(`Elemento card encontrado: ${card ? card.outerHTML : 'No encontrado'}`);
    
    if (!card) {
        console.error(`No se encontró el juego con ID ${juegoId}.`);
        return;
    }

    // Actualiza los selectores para coincidir con las clases en tu HTML
    const nombreElement = card.querySelector('span');
    const precioElement = card.querySelector('p.job');

    console.log(`Nombre Elemento: ${nombreElement ? nombreElement.outerHTML : 'No encontrado'}`);
    console.log(`Precio Elemento: ${precioElement ? precioElement.outerHTML : 'No encontrado'}`);

    if (!nombreElement || !precioElement) {
        console.error(`Elementos necesarios no encontrados para el juego con ID ${juegoId}.`);
        return;
    }

    const nombre = nombreElement.textContent.trim();
    const precio = precioElement.textContent.trim();
    
    console.log(`Nombre del juego: ${nombre}`);
    console.log(`Precio del juego: ${precio}`);
    
    // Si hay un elemento para detalle, se agrega opcionalmente
    const detalleElement = card.querySelector('.detalle');
    const detalle = detalleElement ? detalleElement.textContent.trim() : '';
    
    const juego = {
        id: juegoId,
        nombre: nombre,
        detalle: detalle,
        precio: precio
    };
    
    console.log(`Datos del juego:`, juego);
    
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    
    if (!carrito.some(juego => juego.id == juegoId)) {
        carrito.push(juego);
        localStorage.setItem('carrito', JSON.stringify(carrito));
        alert("Juego agregado al carrito");
    } else {
        alert("Este juego ya está en el carrito");
    }
}


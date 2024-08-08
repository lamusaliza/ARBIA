document.getElementById("sendButton").addEventListener("click", function() {
    const loader = document.querySelector(".loader");

    // Añadir la clase que activa el cambio de color
    loader.classList.add("breathing");

    // Después de 3 segundos, quitar la clase para regresar al estado original
    setTimeout(() => {
        loader.classList.remove("breathing");
    }, 3000);
});

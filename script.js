document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popup");
    const closePopup = document.getElementById("closePopup");
  
    // Mostrar el pop-up al cargar la página
    popup.style.display = "flex";
  
    // Cerrar el pop-up al hacer clic en "Aceptar"
    closePopup.addEventListener("click", () => {
      popup.style.display = "none";
    });
  });
  
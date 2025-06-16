function validarFormulario() {
  const name = document.getElementById("name").value.trim();
  const sname = document.getElementById("sname").value.trim();
  const email = document.getElementById("email").value.trim();
  const tel = document.getElementById("tel").value.trim();
  const city = document.getElementById("city").value.trim();
  const pais = document.getElementById("pais").value.trim();
  const cdfrente = document.getElementById("cdfrente").value.trim();
  const cdatras = document.getElementById("cdatras").value.trim();
  const check = document.getElementById("check").checked;

  if (!name || !sname ||  !email ||  !tel ||  !city ||  !pais || !cdfrente || !cdatras) {
    alert("Por favor completa todos los campos.");
    return false;
  }

  if (!check) {
    alert("Debes aceptar los términos y condiciones.");
    return false;
  }

  alert("Formulario registrado correctamente. ¡Gracias! A casa platitaa 🤑🤑");  
  document.getElementById("formulario").submit();

}
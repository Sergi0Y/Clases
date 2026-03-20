// Obtenemos la referencia al contenedor en el HTML
const pokemonInfoContainer = document.getElementById('pokemon-info');


/* pokeBtn.addEventListener('click', ()=>{
  //Obtenemos valor de input
  const pokemonName = poke-demos.value;
  pokeApi(pokemonName);
}) */

// Hacemos la petición a la PokéAPI
fetch('https://pokeapi.co/api/v2/pokemon/charizard')
  .then(response => response.json())
  .then(data => {
    // Creamos el contenido HTML con los datos de la API
    const pokemonHTML = `
    
      <h2>${data.name}</h2>
      <img src="${data.sprites.front_shiny}" alt="${data.name}" width="200px" height="200px">
      <img src="${data.sprites.front_default}" alt="${data.name}" width="200px" height="200px">
      <img src="${data.sprites.back_default}" alt="${data.name}" width="200px" height="200px">
      <p><strong>Altura:</strong> ${data.height / 10} m</p>
      <p><strong>Peso:</strong> ${data.weight / 10} kg</p>
    `;

    // Insertamos el HTML en nuestro contenedor
    pokemonInfoContainer.innerHTML = pokemonHTML;
  })
  .catch(error => {
    // Manejamos cualquier error que pueda ocurrir
    pokemonInfoContainer.innerHTML = '<p>No se pudo encontrar el Pokémon.</p>';
    console.error('Error al obtener los datos del Pokémon:', error);
  });

fetch('https://pokeapi.co/api/v2/pokemon/charizard')
  .then(response => response.json())
  .then(data => {
    // Creamos el contenido HTML con los datos de la API
    const pokemonHTML = `
      <h2>${data.name}</h2>
      <img src="${data.sprites.front_default}" alt="${data.name}">
      <p><strong>Altura:</strong> ${data.height / 10} m</p>
      <p><strong>Peso:</strong> ${data.weight / 10} kg</p>
    `;

    // Insertamos el HTML en nuestro contenedor
    pk.innerHTML = pokemonHTML;
  })
  .catch(error => {
    // Manejamos cualquier error que pueda ocurrir
    pk.innerHTML = '<p>No se pudo encontrar el Pokémon.</p>';
    console.error('Error al obtener los datos del Pokémon:', error);
  }); 



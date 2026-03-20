// Obtiene la referencia al contenedor en el HTML
const pokeContainer = document.getElementById('function-pk');
const pokeBtn = document.getElementById('pokeBtn');
const pokeNameI = document.getElementById('pokeNameI');

// La función ahora acepta un parámetro: pokemonName
function pokeApi(pokemonName) {
    if (!pokemonName) {
        pokeContainer.innerHTML = '<p>Por favor, ingresa un nombre de Pokémon.</p>';
        return;
    }
    pokeContainer.innerHTML = `<p>Buscando a ${pokemonName}...</p>`;
    // Usamos el nombre del parámetro en la URL de la API
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`)
        .then(response => {
            // Manejamos el caso de que la respuesta no sea exitosa
            if (!response.ok) {
                throw new Error('No se pudo encontrar el Pokémon. Intenta con otro nombre.');
            }
            return response.json();
        })
        .then(data => {
            // Creamos el contenido HTML con los datos de la API
            const pokemonHTML = `
                <h2>${data.name}</h2>
                <img src="${data.sprites.front_default}" alt="${data.name}">
                <img src="${data.sprites.front_shiny}" alt="${data.name}">
                <p><strong>Altura:</strong> ${data.height / 10} m</p>
                <p><strong>Peso:</strong> ${data.weight / 10} kg</p>
            `;
            pokeContainer.innerHTML = pokemonHTML;
        })
        .catch(error => {
            // Manejamos cualquier error que pueda ocurrir
            pokeContainer.innerHTML = `<p style="color: white; background-color: black";>${error.message}</p>`;
            console.error('Error al obtener los datos del Pokémon:', error);
        });
}

// Escuchamos el evento 'click' en el botón para ejecutar la función
pokeBtn.addEventListener('click', () => {
    // Obtenemos el valor del input del usuario
    const pokemonName = pokeNameI.value;
    // Llamamos a la función con el nombre que el usuario escribió
    pokeApi(pokemonName);
});
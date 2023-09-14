movieslist = document.getElementById("list_movies");
async function fetchTitle(){
    const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    const data = await response.json();
    const movies = data.results;
    movies.forEach(movie => {
        const li = document.createElement("li");
        li.textContent = movie.title;
        movieslist.appendChild(li); 
    });
    }
fetchTitle();
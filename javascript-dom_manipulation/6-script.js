characterElement = document.getElementById("character");
async function fetchName(){
    const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
    const data = await response.json();
    const thename = data.name;
    characterElement.textContent = thename;
}
fetchName();
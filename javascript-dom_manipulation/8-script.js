window.onload = () => {
  let helloElement = document.getElementById("hello");
  async function fetchHello(){
      const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
      const data = await response.json();
      const value = data.hello;
      helloElement.textContent = value;
      }
fetchHello();
}
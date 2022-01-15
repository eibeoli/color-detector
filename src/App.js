import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  const [query,setQuery] = useState();

  const getLink = event => {
    event.preventDefault();
    fetch('/api/get_index', {
    method : 'POST',
    headers : {
      'Content-Type' : 'application/json'
    },
    body : JSON.stringify({
      query: query,

    })
  }).then((response) => response.json())
    .then((data) => {
      show_image(data.image, 300 ,300);
    });
  }
  
  function show_image(src, width, height) {
    var img = document.createElement("img");
    img.src = src;
    img.width = width;
    img.height = height;
    //img.alt = alt;

    // This next line will just add it to the <body> tag
    var mainContainer = document.getElementById("Color");
    mainContainer.innerHTML = "";
    mainContainer.appendChild(img);
    
}

  return (
    <div className="App">
      <div class="Title"><i>Color Detector</i></div>
      <div id="Text">
        <ul>
        <li>Enter a word and an image will be generated, along with five prominent colors.</li>
        </ul>
      </div>
      <div id="Color"></div>
       <form id="Input-Container" onSubmit={getLink}>
          <input value={query}
          onChange={(event) => setQuery(event.target.value)} type="text" name="search"></input>
          <input type="submit" value="detect"></input>
        </form>


       
    </div>
    
    
  );
}

export default App;

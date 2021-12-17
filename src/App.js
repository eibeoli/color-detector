import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  const [query,setQuery] = useState();
  const [pack, setPack] = useState({});

  const getLink = event => {
    console.log("hello?");
    event.preventDefault();
    fetch('/api/get_index', {
    method : 'POST',
    headers : {
      'Content-Type' : 'application/json'
    },
    body : JSON.stringify({
      query: query
    })
  }).then((response) => response.json())
    .then((data) => {
      setPack(data.image);
      //displayImage(pack);
      show_image(data.image, 300 ,300);
      //show_colors(data.colors)
    });
  }

  //display colors as 

  function displayImage(data){
    var link = query["image"];
    //var colors = pack["colors"]

    var img = document.createElement("img");
    img.src = link;
    img.width = 300;
    img.height = 300;
    //img.alt = alt;

    // This next line will just add it to the <body> tag
    var mainContainer = document.getElementById("Color");
    mainContainer.innerHTML = "";
    mainContainer.appendChild(img);
  }
  

  //for each rbg thing in colors, display it lol

  function displayLink(data){ //replace link ever
    var mainContainer = document.getElementById("Color");
    console.log("scream");
    mainContainer.innerHTML = 'Link: ' + data.image;
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

function show_colors(src){
  var color = document.createElement("img");
  color.src = src;

    // This next line will just add it to the <body> tag
    var mainContainer = document.getElementById("Color");
    //mainContainer.innerHTML = ""; should be filled?
    mainContainer.appendChild(color);
}

  /*function displayLink(data){
    var mainContainer = document.getElementById("Color");
    mainContainer.src = data.image;
    document.body.appendChild(mainContainer);
  }*/

  return (
    <div className="App">
      <div class="Title"><i>Color Detector</i></div>
      <div id="Text">
        <ul>
        <li>App made with React/Flask/Python, hosted on AWS</li>
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



function showPoster(){
  //alert('video end')
  const el = document.getElementById('vid');
  //var elem = document.createElement("img");
  //elem.setAttribute("src", "static/vid-poster.png");
  //elem.setAttribute("height", "768");
  //elem.setAttribute("width", "1024");
  //elem.setAttribute("alt", "Poster");
  //el.appendChild(elem);
    el.innerHTML= '<img class="ximg-kenburns" src="{{ url_for(\'static\',filename=img\vid-poster.png" alt="image2" style="max-width:100%;"> '

}

//var v = document.getElementById('v');
//v.addEventListener('canplaythrough', function(e) {
  //console.log(e.type, this.seekable.end(0));
//});


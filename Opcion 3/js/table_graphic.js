//Load JSON  file 
function loadJSON(callback , file) {

    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', file, true);
    xobj.onreadystatechange = function() {
        if (xobj.readyState == 4 && xobj.status == "200") {
            callback(xobj.responseText);

        }
    }
    xobj.send(null);

}
//When the user click on income, call this function to generate the graphic 
function generateGraph(idUser){
  console.log("Me han llamado");
  loadJSON(function(response) {
    // Do Something with the response e.g.
    jsonresponse = JSON.parse(response);
    
    var x=get_keys(jsonresponse);
   
    var id=x.shift();
    var y_values=[];
 
      for (var i = 0; i < jsonresponse.length; i++) {
        if(jsonresponse[i][id]==idUser){
          for (var j = 0; j < x.length; j++) {
            y_values.push(jsonresponse[i][x[j]]);

          }
    }
  }
  generatePlotly(x,y_values);
    
  },'graphic.json');  
}
//Generate the Plotly Graphic 
function generatePlotly(x,y){
  console.log(x);
  console.log(y);
  (function() {
  var d3 = Plotly.d3;

  var WIDTH_IN_PERCENT_OF_PARENT = 10,
      HEIGHT_IN_PERCENT_OF_PARENT = 50;

  var gd3 = d3.select('body')
      .append('div')
      .style({
          width: WIDTH_IN_PERCENT_OF_PARENT + '%',
          'margin-left': (100 - WIDTH_IN_PERCENT_OF_PARENT) / 2 + '%',


          height: HEIGHT_IN_PERCENT_OF_PARENT + 'vh',
          'margin-top': (100 - HEIGHT_IN_PERCENT_OF_PARENT) / 2 + 'vh'
      });


    TESTER = document.getElementById('graph');
 
    console.log( Plotly.BUILD );    

    var gd = gd3.node();

    data=[{
        type: 'bar',
        x: x,
        y: y,
        marker: {
            color: '#C8A2C8',
            line: {
                width: 0.5
            }
        }
    }]
    layout={
        title: 'INCOME',
        autosize: false,
        width: 550,
        font: {
            size: 16
        }
    }
    Plotly.newPlot(TESTER, data,layout);

    window.onresize = function() {
        Plotly.Plots.resize(gd);
    };

    })();
}
//Get the keys of JSON
function get_keys(json) {
  var col = [];
  for (var i = 0; i <  json.length; i++) {
      for (var key in  json[i]) {
          if (col.indexOf(key) === -1) {
              
              col.push(key);
          }
      }
  }
  return col;
 
}





loadJSON(function(response) {
  jsonresponse = JSON.parse(response);
  var col = get_keys(jsonresponse);
  var table = document.createElement("table");
  var tr = table.insertRow(-1);                   // TABLE ROW.
  for (var i = 0; i < col.length; i++) {
          var th = document.createElement("th");      // TABLE HEADER.
          th.innerHTML = col[i];
          tr.appendChild(th);
          tr.setAttribute('class', 'tbl-header');  
          
  }

  var th = document.createElement("th");      // TABLE HEADER.
  th.innerHTML = " ";
  tr.appendChild(th);
  var divContainerHeader = document.getElementById("showHeaders");

  divContainerHeader.innerHTML = "";
  divContainerHeader.appendChild(table);
    // ADD JSON DATA TO THE TABLE AS ROWS.
  for (var i = 0; i < jsonresponse.length; i++) {

        tr = table.insertRow(-1);

        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);

            tabCell.innerHTML = jsonresponse[i][col[j]];
        }

        var btn = document.createElement("BUTTON");
        btn.setAttribute("class","btn btn-success");
        btn.setAttribute("id",jsonresponse[i][col[0]]);
        tr.setAttribute("align","center");
        btn.setAttribute("data-toggle","modal");
        btn.setAttribute("data-target","#myModal");    
        var t = document.createTextNode("Income");
        btn.appendChild(t);

        tr.appendChild(btn);
        var id_temp=jsonresponse[i][col[0]];
        document.getElementById(id_temp).onclick = function() {
          console.log(this.id);
          generateGraph(this.id);

        };

    }

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById("showData");
    table.setAttribute('class', '');  
    divContainer.innerHTML = "";
    divContainer.appendChild(table);
    
  
},'tabledata.json');  



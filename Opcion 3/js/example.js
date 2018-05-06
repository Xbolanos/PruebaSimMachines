function loadJSON(callback) {

    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'tabledata.json', true);
    xobj.onreadystatechange = function() {
        if (xobj.readyState == 4 && xobj.status == "200") {

            // .open will NOT return a value but simply returns undefined in async mode so use a callback
            callback(xobj.responseText);

        }
    }
    xobj.send(null);

}
//var myList =[{"id":1,"first_name":"Ardelis","last_name":"Spenceley","email":"aspenceley0@npr.org","gender":"Female","ip_address":"131.208.29.28"},
//{"id":2,"first_name":"Jacques","last_name":"Gorch","email":"jgorch1@earthlink.net","gender":"Male","ip_address":"198.25.227.146"}
//]
var myList=[]
loadJSON(function(response) {
  // Do Something with the response e.g.
  jsonresponse = JSON.parse(response);

  // Assuming json data is wrapped in square brackets as Drew suggests
  myList=jsonresponse;
  console.log(myList);
  


  
});  


$(document).ready(function(e) {
  $.getJSON( "tabledata.json" , function( result ){
      myList=result;
      console.log(myList);
      
    });
});

// Builds the HTML Table out of myList.
function buildHtmlTable(selector) {

  var columns = addAllColumnHeaders(myList, selector);

  for (var i = 0; i < myList.length; i++) {
    var row$ = $('<tr/>');
    for (var colIndex = 0; colIndex < columns.length; colIndex++) {
      var cellValue = myList[i][columns[colIndex]];
      if (cellValue == null) cellValue = "";
      row$.append($('<td/>').html(cellValue));
    }
    $(selector).append(row$);
  }
}


// Adds a header row to the table and returns the set of columns.
// Need to do union of keys from all records as some records may not contain
// all records.
function addAllColumnHeaders(myList, selector) {
  var columnSet = [];
  var headerTr$ = $('<tr/>');

   
   
  for (var i = 0; i < myList.length; i++) {
    var rowHash = myList[i];
    for (var key in rowHash) {
      if ($.inArray(key, columnSet) == -1) {
        columnSet.push(key);
        headerTr$.append($('<th/>').html(key));
      }
    }
  }



$(selector).append(headerTr$);
  return columnSet;
}


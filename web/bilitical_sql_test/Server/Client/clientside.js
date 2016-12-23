$('#insertbtn').on('click', function(event) { //insert article 
    console.log('worked1');
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/insert",
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({"artID": document.getElementById('addArticle').value,"newsURL": document.getElementById('addArtURL').value, "viewpoint": document.getElementById('addArtViewpoint').value, "datePublished": document.getElementById('addDate').value, "adminID": document.getElementById('addArtAdmin').value}),
        success: function(data){
            $('#resultDisplay').text('The article has been inserted!');
        }
    });
});

$('#searchbtn').on('click', function(event) { //search article
    console.log('worked1');
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/search",
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({"searchViewpoint": document.getElementById('searchViewpoint').value, "searchJournalist": document.getElementById('searchJournalist').value}),
        success: function(data){
            $('#resultDisplay').text(data);
        }
    });
});

$('#journsearchbtn').on('click', function(event) { //look up journalist
    console.log('worked1');
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/journalist",
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({"lookup2": document.getElementById('lookupViewpoint').value, "lookup3": document.getElementById('lookupAge').value}),
        success: function(data){
            $('#resultDisplay').text(data);
        }
    });
});

$('#mostartbtn').on('click', function(event) { //most articles
    console.log('worked1');
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/article",
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({"most1": document.getElementById('NumArt').value}),
        success: function(data){
            $('#resultDisplay').text(data);
        }
    });
});

$('#increasebtn').on('click', function(event) { //increase age
    console.log('worked1');
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/journalistage",
        dataType: "json",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({"increase1": document.getElementById('increaseJourn').value, "increase2": document.getElementById('increaseAge').value}),
        success: function(data){
            $('#resultDisplay').text('The Journalist age has been increased');
        }
    });
});

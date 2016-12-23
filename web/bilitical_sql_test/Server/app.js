var mysql = require('mysql');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var path = require('path');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root"
});
var port = process.env.PORT || 8080;

con.connect(function(err){
    if(err){
        console.log('Error connection to Db');
        return;
    }

    console.log('Connection established');
});

app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

app.use(express.static('Client'));

app.get('/', function(req,res){
    res.sendFile(path.join(__dirname + '/Client/homepage.html'));
});

app.post('/insert', function(req, res){
    var article = {articleID: parseInt(req.body.artID),URL: req.body.newsURL, viewpoint: req.body.viewpoint, datePublished: req.body.datePublished, journalistName: null, mediaID: null, topicID: null, adminID: req.body.adminID}; 

    con.query('INSERT INTO bilitical.article SET ?', article, function(err, rows){
        if(err) throw err;

        res.json({message:'insert is cool'});
    });

    
});

app.post('/journalist', function(req, res){
    console.log(req.body.lookup2);
    console.log(req.body.lookup3);

    var min = 0;
    var max = 0;

    if(req.body.lookup3 == "20-25"){
        min = 20;
        max = 25;
    } else if(req.body.lookup3 == "26-30"){
        min = 26;
        max = 30;
    } else if(req.body.lookup3 == "31-40"){
        min = 31;
        max = 40;
    } else if(req.body.lookup3 == "41-60"){
        min = 41;
        max = 60;
    } else {
        console.log('fuck');
        min = 20;
        max = 70;
    }
    console.log(min);
    // cannot figure out why this query does not work -- it works for other similar queries
    con.query('SELECT * FROM bilitical.journalist WHERE politicalStance = ? AND (age >= ? AND age <= ?)', [req.body.lookup2,min,max],function(err, row){
        var responseString='';
        if(row != null){
            for(var i = 0; i < row.length; i++){
                responseString = responseString + 'The Journalist\'s name is: '+row[i].journalistName+'\n\n\n';
            }
        }
        res.json(responseString);
    });

});

app.post('/article', function(req, res){
    console.log('got em 3');
    console.log(req.body.most1);

    con.query('SELECT COUNT(journalistName) AS count FROM bilitical.article Where journalistName=?',[req.body.most1],function(err,rows){
        console.log(rows[0].count);
        res.json(req.body.most1 + ' completed '+rows[0].count+' articles.');
    });

});

app.post('/journalistage', function(req, res){
    var currentAge = 0;
    var newAge = 0;
    con.query('SELECT * FROM bilitical.journalist WHERE journalistName = ?', [req.body.increase1],function(err, rows){
        if(err) throw err;

        currentAge = rows[0].age;
        newAge = currentAge + parseInt(req.body.increase2);

        con.query('UPDATE bilitical.journalist SET age=? Where journalistName=?', [newAge,req.body.increase1], function (err,result){
            if(err) throw err;

            console.log('updated');
        })
    });
    res.json({message:'increase age is cool'});
});

app.post('/search', function(req, res){

    con.query('SELECT * FROM bilitical.article WHERE viewpoint = ? AND journalistName = ?', [req.body.searchViewpoint,req.body.searchJournalist],function(err, rows){
        var responseString='';
        for(var i = 0; i < rows.length; i++){
            responseString = responseString + 'The ArticleID is: '+rows[i].articleID+' The Article URL is: '+rows[i].URL+'\n\n\n';
        }

        res.json(responseString);
    });
});



app.listen(port);
console.log('Magic happens on port '+port);
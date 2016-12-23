var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017')

var Article = require('./models/article');


router.get('/', function(req, res, next) {
    Article.find(function(err,articles){
        if(err)
            res.send(err);
            
        res.json(articles);
    });
});


router.get('/conservative', function(req,res,next){
    Article.find({'viewpoint': "Conservative"}, function(err,docs){
        if(err)
            res.send(err);

        res.json(docs);
        
    });
});

router.get('/liberal', function(req,res,next){
    Article.find({'viewpoint': "Liberal"}, function(err,docs){
        if(err)
            res.send(err);

        res.json(docs);
        
    });
});

router.get('/progressive', function(req,res,next){
    Article.find({'viewpoint': "Progressive"}, function(err,docs){
        if(err)
            res.send(err);

        res.json(docs);
        
    });
});

router.get('/center', function(req,res,next){
    Article.find({'viewpoint': "Centered"}, function(err,docs){
        if(err)
            res.send(err);

        res.json(docs);
        
    });
});


router.delete('/:article_id',function(req,res,next){
    Article.remove({_id: req.params.article_id},function(err,tweet){
        if(err) res.send(err);

        res.json({message: 'Successfully deleted'});
    });
});

router.put('/', function(req, res, next) {
    res.send('Got a PUT request for the api');
});


router.post('/', function(req, res, next) {
    var article = new Article();
    article.title = req.body.title;
    article.articleURL = req.body.articleURL;
    article.viewpoint = req.body.viewpoint;
    article.dateAdded = req.body.dateAdded;
    article.dateWritten = req.body.dateWritten;
    article.flagged = req.body.flagged;
    article.save(function(err){
        if(err)
        res.send(err);

        res.json({message:'Article added to database.'});
    });
});


router.post('/conservative',function(req,res,next){
    res.json();
});


router.delete('/', function(req, res, next) {
    res.send('Got a DELETE request for the api');
});


module.exports = router;
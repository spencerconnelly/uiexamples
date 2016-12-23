var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ArticleSchema = new Schema({
    title: String,
    articleURL: String,
    viewpoint: String,
    dateAdded: String,
    dateWritten: String,
    flagged: Boolean,
});

module.exports = mongoose.model('Article',ArticleSchema);
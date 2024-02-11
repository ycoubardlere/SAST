const express = require('express');
const router = express.Router();
const DOMPurify = require('dompurify');

router.get('/greeting', (req, res) => {
    const { name } = req.query;
    const sanitizedName = DOMPurify.sanitize(name);
    res.send('<h1> Hello :' + sanitizedName + '</h1>');
});

router.get('/greet-template', (req, res) => {
    const name = req.query.name;
    const sanitizedName = DOMPurify.sanitize(name);
    res.render('index', { user_name: sanitizedName });
});

module.exports = router;
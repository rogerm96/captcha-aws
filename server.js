const express = require('express');
const app = express();
const morgan = require('morgan');

app.use(morgan('dev'));

app.get('/', (req,res) => res.send('<h1>This my first server web on AWS</h1>'));

app.listen(8080, () => {
    console.log('run server on port 80!');
});
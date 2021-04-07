const express = require('express');
const app = express();
const morgan = require('morgan');

app.use(morgan('dev'));

app.get('/', (req,res) => {
    res.send('Hello world');
});

app.listen(3000, () => {
    console.log('run server on port 3000!');
});
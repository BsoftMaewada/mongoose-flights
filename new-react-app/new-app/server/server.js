require("dotenv").config();

const express = require('express');// 1.
const app = express();//1.

const path = require('path');//3.
const cors = require('cors');//3.


//7. Mongoose connection import
require('./mongoose-connection');


app.get('/helloworld', (req, res, next) => {
    res.send('Hello World!');
})//2. to check if the app is up and running using localhost:5000/helloworld route

const PORT = 5000;//1.


/** MIDDLEWARE **/

//4.
//Cors
app.use(cors());
// to serve static files and to serve the react build 
app.use(express.static(path.join(__dirname, '..', 'build')));
app.use(express.static('public'));

//5. Express version of body-parser
app.use(express.json());

//3.
//IS THE REACT FULL STACK MAGIC MIDDLEWARE
/*
ANY REQUEST not covered by routes express makes -- will get piped to this middleware
and this middleware's job is to handover control to react
*/
app.use((req, res, next) => {
    console.log(req.headers);
    res.sendFile(path.join(__dirname, "..", "build", "index.html"));
});

app.listen(process.env.PORT || 5000, () => {
    console.log('listening on port ' + PORT);
}); //1.
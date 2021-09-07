
//1.
const express = require('express');
const app = express();
//5.
const path = require('path');
const cors = require('cors');
//6. npm install cors on terminal
//7. go to json file and update scripts paste start, start-client and start-dev

//8. Cors

//Cors
app.use(cors());
// to serve static files and to serve the react build
app.use(express.static(path.join(__dirname, "..", "build")));
app.use(express.static("public"));


//1.
app.get('/helloworld', (req, res) => {
    res.send('Hello World')
});
//3.
app.use((req, res, next) => {
    console.log(req.headers),
        res.sendFile(path.join(__dirname, '..',
            'build', 'index.html'));
})
//2.
app.listen(5000, () => {
    console.log("successfully connected")
})
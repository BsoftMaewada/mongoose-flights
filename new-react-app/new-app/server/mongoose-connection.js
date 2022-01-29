//6. DB config
const mongoose = require('mongoose');

//connect to MongoDB
//replacing config/keys with process.env
mongoose.connect(process.env.DB_URL, {
    useNewUrlParser: true,})
    .then(() => console.log('MongoDB successfully connected'))
    .catch((err) => console.log(err));
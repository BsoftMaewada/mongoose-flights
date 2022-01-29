//9. Creating Schema

const mongoose = require('mongoose');
const Schema = mongoose.Schema;


//Creating schema

const UserSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    date: {
        type: String,
        default: Date.now
    }
});

//10.
const User = mongoose.model('User', UserSchema);
module.exports = User;
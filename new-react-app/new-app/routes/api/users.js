const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

//Load User Model
const User = require('../../models/User');

//Pull the errors and isValid variables from our validateRegisterInput(req.body) function and check input validation
//@route POST api/users/register
//@desc Register User
//@access Public

router.post('/register', (req, res) => {

    User.findOne({ email: req.body.email }).then((user) => {
        if (user) {
            return res.status(400).json({ email: 'Email already exists' });
        } else {
            const newUser = new User({
                name: req.body.name,
                email: req.body.email,
                password: req.body.password
            });

        
            //Hash passwork before saving in database
            bcrypt.genSalt(10, (err, salt) => {
                bcrypt.hash(newUser.password, salt, (err, hash) => {
                    if (err) throw err;
                    newUser.password = hash;
                    newUser
                        .save()
                    .then(user = res.json(user))
                        .catch(err => console.log(err));
                });
            });
        }
    });
});

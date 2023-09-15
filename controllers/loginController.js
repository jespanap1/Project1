const path = require("path");

const controller = {

    getLogin: (req, res) => {
        res.sendFile(path.join(__dirname, '../views/login.html'));
    },
};

module.exports = controller;
const path = require("path");

const controller = {

    getRegister: (req, res) => {
        res.sendFile(path.join(__dirname, '../views/register.html'));
    },
};

module.exports = controller;
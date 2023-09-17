const express = require('express');
const router = express.Router();

const registerController = require('../controllers/registerController');

// @GET /products
router.get('/', registerController.getRegister);
// @POST /products
router.post('/', registerController.postRegister);





module.exports = router;
require('dotenv').config()
const express = require("express");
const app = express();
const http = require("http");

http.createServer({}, app).listen(process.env.PORT, function () {
	console.log("Server Start, Serving on port 3000");
});

// ROUTES
const api = require('./routes/api')
app.use('/api', api)
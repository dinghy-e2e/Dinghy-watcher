require('dotenv').config()
const express = require("express");
const app = express();
const http = require("http");

http.createServer({}, app).listen(process.env.PORT, function () {
	console.log("Server Start, Serving on port 3000");
});

// ROUTES
const birds = require('./routes/birds')
app.use('/birds', birds)
const api = require('./routes/api')
app.use('/api', api)

// GET method route
app.get('/', (req, res) => {
  ans = {response:'GET request to the homepage'}
  ans = {response2:'GET request to the homepage'}
  res.json(ans)
})

// POST method route
app.post('/', (req, res) => {
  res.send('POST request to the homepage')
})

app.all('/secret', (req, res, next) => {
  console.log('Accessing the secret section ...')
  next() // pass control to the next handler
})

app.get('/users/:userId/books/:bookId', (req, res) => {
  res.send(req.params)
})

app.route('/book')
  .get((req, res) => {
    res.send('Get a random book')
  })
  .post((req, res) => {
    res.send('Add a book')
  })
  .put((req, res) => {
    res.send('Update the book')
  })

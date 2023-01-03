const express = require('express')
const router = express.Router()

var AWS = require("aws-sdk");
var uuid = require('uuid');

AWS.config.getCredentials(function(err) {
  if (err) console.log(err.stack);
  // credentials not loaded
  else {
    AWS.config.region = 'us-west-1';
    console.log("Access key:", AWS.config.credentials.accessKeyId);
  }
});

console.log("Region: ", AWS.config.region);
// middleware that is specific to this router
router.use((req, res, next) => {
  console.log('Time: ', Date.now())
  next()
})
// define the home page route
router.get('/', (req, res) => {
  var ec2 = new AWS.EC2({apiVersion: '2016-11-15'});
  var params = {
    DryRun: false
  };
  // Call EC2 to retrieve policy for selected bucket
  ec2.describeInstances(params, function(err, data) {
    if (err) {
      console.log("Error", err.stack);
    } else {
      console.log("Success", JSON.stringify(data));
    }
  });

  res.send('AWS actions')
})
// define the about route
router.get('/about', (req, res) => {
  res.send('About birds')
})

module.exports = router
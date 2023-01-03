var os = require('os');
var request = require('request');

var id = 1
var osl = os.cpus().length

var data = {}
data.id = id
data.cpus = osl
data.totalmem = os.totalmem()

function myFunc(arg) {
  var avg_load = os.loadavg();
  var precent = parseFloat(( avg_load[0] / osl ) * 100)
  data.freemem = os.freemem()
  data.cpuprecent = precent
  data.name = "ec2-dev"
  console.log(data)

  // console.log ("total mem: " + data.totalmem )

  // console.log ("free mem: " + data.freemem )

  // console.log("Load average (1 minute):"
  //             + String(avg_load[0]));
  
  // console.log("Load precentage: " + precent + "%")
  var clientServerOptions = {
    uri: 'http://server:3000/api/',
    body: JSON.stringify(data),
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
  }
  request(clientServerOptions, function (error, response) {
      if (error){
        console.log(error);
        return
      }
      // console.log("Res: " + response.body);
      return;
  });
}

setInterval(myFunc, 5000);
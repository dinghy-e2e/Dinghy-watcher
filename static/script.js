

async function makeRequest() {
    try {
      const response = await fetch("status");

      
      console.log('response.status: ', response.status); // 👉️ 200
      console.log(response);
  
    } catch (err) {
      console.log(err);
    }
  }
  
  makeRequest();
  
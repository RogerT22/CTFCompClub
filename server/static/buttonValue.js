function sendOver(val) {
  //console.log("Hello");
  var entry = {
    message: val
  };
  //console.log("Hello");
  fetch('/thepersonifcationoffear', {
    method: "POST",
    credentials:"include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type" : "application/json"
    })
  })
  .then( function(response){
    //console.log(response)
    if(response.status !== 200) {
      console.log("Nope");
      return;
    }
    response.json().then(function(data){
          console.log(data);
    }
    )
  })
}

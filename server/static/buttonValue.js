function sendOver(val) {
  var entry = {
    message: val
  };
    fetch('/MultipleOf516', {
    method: "POST",
    credentials:"include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type" : "application/json"
    })
  })
  .then( function(response){
    if(response.status !== 200) {
      console.log("FUCK");
      return;
    }
    response.json().then(function(data)
      console.log(data);
    )
  })

}

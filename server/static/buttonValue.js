function sendOver(val) {
  var entry = {
    number: parseInt(val)
  }
  fetch('/MultipleOf516', {
    method: "POST",
    credentials:"include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type" : "application/json"
    })
  })
}

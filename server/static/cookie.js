// 10 milli seconds
//console.log(DateTime.Now);
var currentdate = new Date();
var datetime = "Last Sync: " + currentdate.getDay() + "/" + currentdate.getMonth()
+ "/" + currentdate.getFullYear() + " @ "
+ currentdate.getHours() + ":"
+ currentdate.getMinutes() + ":" + currentdate.getSeconds();
console.log(datetime);
var instant = 1/24 * 1/60 * 1/60;
var mycookie = Cookies.get("test");
if(mycookie == "yes") {
  fetch('/cookies', {
    method: "GET",
    credentials:"include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type" : "application/json"
    })
  })
}
Cookies.set('YOYO', 'value', { expires: 1/24 * 1/60 * 30/60});
Cookies.set('test', 'no', { expires: 1/24 * 1/60 * 1/60});
console.log(document.title);

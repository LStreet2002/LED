var button = document.querySelector(".select")

var bvalue = { led: button.id }


function post(address = "") {
    var post = new XMLHttpRequest();
    post.open('POST', "http/json", true);
    if (type == "POST") {
        post.send(JSON.stringify(bvalue));
        console.log(bvalue)
    }

}
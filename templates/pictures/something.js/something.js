var button = document.querySelector(".select")

var bvalue = { led: button.id }


function post(light) {
    var post = new XMLHttpRequest();
    post.open('POST', "http/status", true);
    if (type == "POST") {
        post.send(JSON.stringify({
            "led": light
        }));
        xhr.send(da)
        console.log(bvalue);

    }

}
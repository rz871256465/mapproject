
socket = new WebSocket("ws://127.0.0.1:8000/chathome/{{ name_id }}/");

socket.onopen = function(event){
    //let tag = document.createElement("div");
    //tag.innerText = "[socket connection successful]";
    //document.getElementById("message").appendChild(tag);
    let tag = document.createElement("div");
    tag.innerText = "You have been paired with user2";
    tag.classList.add("chat");
    tag.classList.add("broadcast");
    document.getElementById("message").appendChild(tag);
}

//当websocket接收到服务端发来的消息时，自动会触发这个函数。
socket.onmessage = function(event){
    
    let tag = document.createElement("div");
    tag.innerText = event.data;
    tag.classList.add("chat");
    tag.classList.add("send");
    document.getElementById("message").appendChild(tag);

    

}

function sendMessage(){
    var tag = document.getElementById("txt");
    
    socket.send(tag.value);
}


const messageInp = document.getElementById("messageInp");
const SendButton = document.getElementById('SendButton');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const msgcontainer = document.querySelector(".msgcontainer");

let html = "";
SendButton.addEventListener('click',(e)=>
{   
    const options = {
        method:"POST",
        body:JSON.stringify({'message':messageInp.value}),
        headers:{
            'content-Type':"application/json",
            'X-CSRFToken': csrftoken
        }
    };

    fetch('get-response/', options).
    then(res => res.json()).
    then((res) =>{
    console.log(res);
    html = `
    <div class="right message">me:${res.UserMessage}</div>
    <div class="left message">Bot:${res.BotReply}</div>`;
}).
catch(err => console.log(err));
msgcontainer.innerHTML += html;
});
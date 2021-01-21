const messageInp = document.getElementById("messageInp"); //accessing the messageinput by user.
const form = document.getElementById('send-container');  //form container.
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.
const msgcontainer = document.querySelector(".msgcontainer"); //accessing the message box.

function gotoBottom(){
    //This function is for automatic scroll donw the scroll bar when the message is appearing inside the message container.
    var element = document.getElementById("scrollmsg"); //accessing the scroll bar element
    element.scrollTop = element.scrollHeight - element.clientHeight;
};

const append = (message, position)=>{
    //This function will append the message and the position which are coming from the below socket.on function to the front end.
    const messageElement = document.createElement('div'); //creating a div block.
    messageElement.innerText = message; // insert the message of user and bot in the div block.
    messageElement.classList.add('message'); //adding the message class in the div block.
    messageElement.classList.add(position); //adding the position class in the div block(left for bot, right for user).
    msgcontainer.append(messageElement); //appending the element in message box.
    gotoBottom(); //after that the container will get scroll down.
};



form.addEventListener('submit',(e)=>
//This event listener will listen to the event when the form get submitted and after that it will send and fetch API request to the server to store the user message and getting the reply from bot.
{   
    e.preventDefault(); //this will prevent the reload of the page.
    append(`you: ${messageInp.value}`, 'right') //this will send the user message and position to the append function. 
    const options = {
        //there are the POST method options which will go with the API request.
        method:"POST", //POST method.
        body:JSON.stringify({'message':messageInp.value}), //convert the user message into string.
        headers:{
            //headers will send the info of the content type and csrf token in the backend.
            'content-Type':"application/json",
            'X-CSRFToken': csrftoken
        }
    };

    //fethc API request.
    fetch('get-response/', options). //sending the request to the 'get-response/' end point of the backend.
    then(res => res.json()). //converting the the response into json format.
    then((res) =>{
        //now it will send the bot response into the append function with its position.
        append(`Bot: ${res.BotReply}`, 'left')
        messageInp.value = ""; //after that it will empty the value of user message.
}).

//if any error occured it will show in message.
catch(() => 
    append('Sorry, server Problem!', 'left')
    );
});

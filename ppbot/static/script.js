let form = document.getElementById("user_text_form")
let json_map = "https://maps.googleapis.com/maps/api/js?"
let spinner = document.getElementById("spinner")
let user_question = document.querySelector("#user_input").value


// quand j'appuie sur le bouton je ne recharge pas la page
function request_ajax(url ,data, headers) {
    return fetch(url, {
        method: "POST",
        body: data,
        headers: headers
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

form.addEventListener("submit", function(event) {
    event.preventDefault();

    request_ajax("/search", user_question, {
        "Content-Type": "plain/text"
    })
    .then(response => {
        console.log(response);
        console.log(user_question);
    })
})
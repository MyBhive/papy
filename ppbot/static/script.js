let form = document.getElementById("user_text_form")
let json_map = "https://maps.googleapis.com/maps/api/js?"
let spinner = document.getElementById("spinner")


// quand j'appuie sur le bouton je ne recharge pas la page
form.addEventListener("submit", function (event) {

    event.preventDefault();


    // appel au serveur
    fetch('/search', {
        method: 'POST',
        body: new FormData(form)
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        let result = document.getElementById('chat_box')
        result.innerHTML = `<p class="col-md-5 offset-md-7col-lg-4">
        <img src="../static/img/quest.png" alt="question" class="mr-3 mt-3 rounded-circle" style="width: 30px;">
        ${data.body} </p> `
    })
})

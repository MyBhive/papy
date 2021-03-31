let form = document.getElementById("user_text_form");
let json_map = "https://maps.googleapis.com/maps/api/js?";
let spinner = document.getElementById("spinner");
let user_question = document.querySelector("#user_input");



// quand j'appuie sur le bouton je ne recharge pas la page
function request_ajax(url ,data, headers) {
    return fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: headers
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

form.addEventListener("submit", function (event) {
    event.preventDefault();

    spinner.style.visibility="visiblie";
    let user_input = document.querySelector("#user_input").value
    request_ajax("/search", user_input, {
        "Content-Type": "application/json"
    })
    .then(response => {
        show_user();
    })
})




function initMap(location, address, key){
    /*
    Je crée la carte googlemap
    location: localité
    address: adresse à marquer
    key: api clef
    */

    let script = document.createElement("script");
    script.src = json_map + "key=" + key + "&callback=initmaps";
    script.defer = true;
    console.log(location)
    window.initmaps = function() {
        const map = new google.maps.Map(document.getElementById("map"), {
            center: location,
            zoom: 15,
            mapTypeId: google.maps.mapTypeId.ROADMAP,
            mapTypeControl: true, 
            scrollwheel: false
        });
        new google.maps.Marker({ 
            position: location,
            map,
            title: address,
        });
        map.setTilt(45);
    } 
    document.getElementById("map").appendChild(script);
}

// Fonction pour HTML
function show_user() {
    let insert_input_user = document.createElement("div");
    insert_input_user.className = "user_print";
    insert_input_user.innerHTML = `<p>
    <img src="../static/img/quest.png" alt="Question" class="mr-3 mt-3 rounded-circle" style="width: 30px;">${user_input}</p>`;
    document.getElementById("bot").appendChild(insert_input_user);
    console.log("ok ça s'affiche")
}

function user_ask() {
    let questionElt = document.createElement("div");
    let titleQuestion = document.createElement("h2");
    titleQuestion.textContent = document.getElementById(user_input);
    questionElt.className = "col-lg-8 box";
    questionElt.appendChild(titleQuestion);
}

function answer() {
    let answerElt = document.createElement("div");
    answerElt.className = "offset-lg-2 col-lg-10";
}

function show_answer(response) {
    let insert_answer = document.createElement("P");
    let chat = document.getElementById("chat_box")
    insert_answer.className = "col-md-5 offset-md-7col-lg-4" ;
    insert_answer.innerHTML = '<img src="../static/img/pap.png" alt="Papy" class="mr-3 mt-3 rounded-circle" style="width: 30px;">'+ response;
    insert_answer.id = "bot_answer"
    chat.appendChild(insert_answer);
}
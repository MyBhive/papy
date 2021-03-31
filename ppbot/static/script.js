let form = document.getElementById("user_text_form");
let json_map = "https://maps.googleapis.com/maps/api/js?";
let spinner = document.getElementById("spinner");
let user_question = document.querySelector("#user_input");
const map_key = "AIzaSyA6pDUb-mZVASzAclRmgzkCQolxA7wTEwM";



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

    spinner.style.visibility="visible";
    let user_input = document.querySelector("#user_input").value
    request_ajax("/search", user_input, {
        "Content-Type": "application/json"
    })
    .then(response => {
        console.log(response);
        show_user();
        show_answer(response["wiki"]);
        initMap(response["coordinate"], response["address"], map_key);
    })
    spinner.style.visibility="hidden";
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
            mapTypeId: 'satellite',
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
    insert_input_user.innerHTML = `<p><img src="../static/img/quest.png" alt="Question" class="mr-3 mt-3 rounded-circle" style="width: 30px;">${user_input.value}</p>`;
    document.getElementById("bot").appendChild(insert_input_user);
    user_input.value = "";
    console.log("ok ça s'affiche")
}

function answer() {
    let answerElt = document.createElement("div");
    answerElt.className = "offset-lg-2 col-lg-10";
}

function show_answer(wiki_quote) {
    let insert_input_user = document.createElement("div");
    insert_input_user.innerHTML = `<p><img src="../static/img/pap.png" alt="Papy" class="mr-3 mt-3 rounded-circle" style="width: 30px;">${wiki_quote}</p>`;
    document.getElementById("bot").appendChild(insert_input_user);
    user_input.value = "";
    console.log("ok ça s'affiche")
}
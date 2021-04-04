let form = document.getElementById("user_text_form");
let json_map = "https://maps.googleapis.com/maps/api/js?";
let spinner = document.getElementById("spinner");
let user_question = document.querySelector("#user_input");
let map_key = "AIzaSyA6pDUb-mZVASzAclRmgzkCQolxA7wTEwM";
let map_index = 0;


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

    spinner.style.display="inline-block";
    let user_input = document.querySelector("#user_input").value
    request_ajax("/search", user_input, {
        "Content-Type": "application/json"
    })
    .then(response => {
        console.log(response);
        show_user();
        show_answer(response["wiki"]);
        initMap(response["coordinate"], response["address"]); 
    })
    spinner.style.display="none";
})


function initMap(location, address) {

    div_id = "map" + String(map_index);
    let div_map = document.createElement("div");
    div_map.id = div_id;
    div_map.className = "map_css";
    let chat_box = document.getElementById("bot");
    chat_box.appendChild(div_map);
        map = new google.maps.Map(document.getElementById(div_id), {
            center: location,
            zoom: 15,
            mapTypeId: 'satellite',
        });
        marker = new google.maps.Marker({ 
            position: location,
            map: map,
            title: address,
        });
        map_index++;
    } 


 


// Fonction pour HTML
function show_user() {
    let insert_input_user = document.createElement("div");
    insert_input_user.innerHTML = `<p><img src="../static/img/quest.png" alt="Question" class="mr-3 mt-3 rounded-circle" style="width: 30px;">${user_input.value}</p>`;
    document.getElementById("bot").appendChild(insert_input_user);
    user_input.value = "";
    console.log("ok ça s'affiche")
}

function show_answer(wiki_quote) {
    let insert_input_user = document.createElement("div");
    insert_input_user.innerHTML = `<p><img src="../static/img/pap.png" alt="Papy" class="mr-3 mt-3 rounded-circle" style="width: 30px;">${wiki_quote}</p>`;
    document.getElementById("bot").appendChild(insert_input_user);
    user_input.value = "";
    console.log("ok ça s'affiche")
}
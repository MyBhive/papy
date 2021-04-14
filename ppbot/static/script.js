let form = document.getElementById("user_text_form");
let spinner = document.getElementById("spinner");
let user_question = document.querySelector("#user_input");
let map_index = 0;


// function to make a ajax request-------------------
function request_ajax(url ,data, headers) {
    return fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: headers
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

// function to make input restriction-------------------
function valid_input(analize_input) {
    if (analize_input.trim(" ", "") === "")
    return 1;
    if (analize_input.length >= 200)
    return 2;
    if (analize_input)
    return 0;
}

// When the user click on the button or click enter, the program starts
form.addEventListener("submit", function (event) {
    event.preventDefault();
    spinner.style.display = "inline-block";
    
    let user_input = document.querySelector("#user_input").value
    if (valid_input(user_input) == 1) {
        wrong_answer_reaction();
        spinner.style.display = "none";
    }
    if (valid_input(user_input) == 2){
        wrong_answer_reaction();
        spinner.style.display = "none";
    }
    if (valid_input(user_input) == 0) {
        request_ajax("/search", user_input, {
        "Content-Type": "application/json"
    })
    .then(response => {
        console.log(response);
        show_user();
        show_answer(response["wiki"]);
        initMap(response["coordinate"], response["address"]); 
        spinner.style.display = "none";
    })
    return 0;
    }
});

// Function to initialize the google map----------------------
function initMap(location, address) {
// generate id for my 2 necessaries div
    frame_id = "frame"+ String(map_index);
    div_id = "map" + String(map_index);
// create the container div to receive the div where the map will be
    let frame_map = document.createElement("div");
    frame_map.id = frame_id;
    frame_map.className = "frame_css";
// create the div where the map will be
    let div_map = document.createElement("div");
    div_map.id = div_id;
    div_map.className = "map_css";
    let chat_box = document.getElementById("bot");
// include div in each other
    chat_box.appendChild(frame_map);
    frame_map.appendChild(div_map);
// create the map
        map = new google.maps.Map(div_map, {
            center: location,
            zoom: 17,
            mapTypeId: 'satellite'
        });
        marker = new google.maps.Marker({ 
            position: location,
            map: map,
            title: address
        });
// add +1 to the index that for reload the id of each div can change 
    map_index++;
}

// Function to show the user input in a chat bubble in HTML---------------------------
function show_user() {
    let insert_input_user = document.createElement("div");
    insert_input_user.innerHTML = `<p id="user_quest"><img src="../static/img/quest.png" alt="Question" class="mr-3 mt-2 rounded-circle" style="width: 30px;">${user_input.value}</p>`;
    document.getElementById("bot").appendChild(insert_input_user);
    user_input.value = "";
}

// Function to show the wiki answer in a chat bubble in HTML-----------------
function show_answer(wiki_quote) {
    let insert_wiki = document.createElement("div");
    insert_wiki.innerHTML = `<p><img src="../static/img/pap.png" alt="Papy" class="mr-3 mt-3 rounded-circle" style="width: 30px;">${wiki_quote}</p>`;
    document.getElementById("bot").appendChild(insert_wiki);
    user_input.value = "";
}

function wrong_answer_reaction() {
    let wrong = document.createElement("div");
    wrong.innerHTML = `<p><img src="../static/img/pap.png" alt="Papy" class="mr-3 mt-2 rounded-circle" style="width: 30px;">Parle plus fort et articule basard!</p>`;
    document.getElementById("bot").appendChild(wrong);
    user_input.value = "";
}
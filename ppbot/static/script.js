let form = document.querySelector("#user_text_form");
// quand j'appuie sur le bouton je ne recharge pas la page
form.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("vous avez appuyé sur valider");
// Envoyer le contenu du formulaire au serveur pour qu'il soit exploité
    fetch("/result", {
        method: "POST",
        body: new FormData(form)
    })

})

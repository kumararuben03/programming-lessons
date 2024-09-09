let email = document.getElementById("email");
let password = document.getElementById("password");
let form = document.querySelector("form");

form.addEventListener("submit", (e) => {
    const errors = [];
    console.log("Hello");

    if(email.value.trim()===""){
        errors.push("Username required");
    }

    if(password.value.length<4){
        errors.push("Password must be at least 4 characters");
    }

    if(errors.length > 0){
        e.preventDefault();
        alert(errors.join(','))
    }
})
function validarcorreo() {
    let email = document.getElementById("email").value;

    if (email.search(/(@duocuc.cl)|(@gmail.com)/) === -1){
        document.getElementById("email").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
        "Correo invalido</div>";
    }else {
        document.getElementById("email").style.border = "1px solid lightgrey";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
        "Correo Permitido</div>";
    }
}

function validarCrearCuenta() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("pass").value;
    let email = document.getElementById("email").value;

    if (email.search(/(@duocuc.cl)|(@gmail.com)/) === -1){
        document.getElementById("email").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
        "Correo invalido</div>";
    }else {
        document.getElementById("email").style.border = "1px solid lightgrey";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
        "Correo Permitido</div>";
    }

    if (String(user).length >= 5 && String(user).length <= 20) {
        if (String(pass).length >= 8) {
            document.getElementById("username").style.border = "1px solid lightgrey";
            document.getElementById("pass").style.border = "1px solid lightgrey";
            document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
                "Acceso Concedido</div>"
        } else {
            document.getElementById("pass").style.border = "1px solid red";
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                "Contraseña debe tener minimo 8 caracteres</div>"

        }
    } else {
        document.getElementById("username").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Usuario debe tener minimo 5 y maximo 20 caracteres</div>"
        document.getElementById("pass").style.border = "1px solid red";
    }
}

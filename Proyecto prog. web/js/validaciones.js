function validarcorreo() {
    let email = document.getElementById("email").value;

    if (email.search(/(@duocuc.cl)|(@gmail.com)/) === -1){
        document.getElementById("email").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
        "Correo invalido</div>";
    }else {
        document.getElementById("email").style.border = "1px solid lightgrey";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-20 mx-auto text-center'>" +
        "Correo Permitido</div>";
    }
}

function validarCrearCuenta() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("pass").value;
    let email = document.getElementById("email").value;

    if (email.search(/(@duocuc.cl)|(@gmail.com)/) === -1){
        document.getElementById("email").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
        "Correo invalido</div>";
    }else {
        document.getElementById("email").style.border = "1px solid lightgrey";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-20 mx-auto text-center'>" +
        "Correo Permitido</div>";
    }

    if (String(user).length >= 5 && String(user).length <= 20) {

        if (email.search(/(@duocuc.cl)|(@gmail.com)/) !== -1) {
            if (String(pass).length >= 8) {
                document.getElementById("username").style.border = "1px solid lightgrey";
                document.getElementById("pass").style.border = "1px solid lightgrey";
                // Mostrar un mensaje de éxito indicando que el acceso está concedido
                document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-20 mx-auto text-center'>" +
                    "Acceso concedido</div>";
            } else {
                document.getElementById("pass").style.border = "1px solid red";
                document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
                    "La contraseña debe tener al menos 8 caracteres</div>";
            }
        } else {
            document.getElementById("username").style.border = "1px solid red";
            document.getElementById("pass").style.border = "1px solid red";
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
                "Ingresa un correo electrónico válido</div>";
        }
    } else {
        document.getElementById("username").style.border = "1px solid red";
        document.getElementById("pass").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-10 mx-auto text-center'>" +
            "El nombre de usuario debe tener entre 5 y 20 caracteres</div>";
    }
    
}


function validarInicioSesion() {
    let pass = document.getElementById("passInicioSesion").value;
    let email = document.getElementById("emailInicioSesion").value;

    if (email.search(/(@duocuc.cl)|(@gmail.com)/) === -1){
        document.getElementById("emailInicioSesion").style.border = "1px solid red";
        document.getElementById("resultadoInicio").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
        "Correo invalido</div>";
    }else {
        document.getElementById("emailInicioSesion").style.border = "1px solid lightgrey";
        document.getElementById("resultadoInicio").innerHTML = "<div class='alert alert-success w-20 mx-auto text-center'>" +
        "Correo Permitido</div>";
    }

        if (email.search(/(@duocuc.cl)|(@gmail.com)/) !== -1) {
            if (String(pass).length >= 8) {
                document.getElementById("emailInicioSesion").style.border = "1px solid lightgrey";
                document.getElementById("passInicioSesion").style.border = "1px solid lightgrey";
                document.getElementById("resultadoInicio").innerHTML = "<div class='alert alert-success w-20 mx-auto text-center'>" +
                    "Acceso concedido</div>";
            } else {
                document.getElementById("passInicioSesion").style.border = "1px solid red";
                document.getElementById("resultadoInicio").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
                    "La contraseña debe tener al menos 8 caracteres</div>";
            }
        } else {
            document.getElementById("emailInicioSesion").style.border = "1px solid red";
            document.getElementById("passInicioSesion").style.border = "1px solid red";
            document.getElementById("resultadoInicio").innerHTML = "<div class='alert alert-danger w-20 mx-auto text-center'>" +
                "Ingresa un correo electrónico válido</div>";
        }
    
}
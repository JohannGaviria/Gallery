document.getElementById("btn-login").addEventListener("click", login);
document.getElementById("btn-register").addEventListener("click", register);
window.addEventListener("resize", pageWidth);

var loginForm = document.querySelector(".login-form");
var registerForm = document.querySelector(".register-form");
var loginRegisterContainer = document.querySelector(".login-register-container");
var backBoxLogin = document.querySelector(".back-box-login");
var backBoxRegister = document.querySelector(".back-box-register");

function pageWidth() {

    if (window.innerWidth > 850) {
        backBoxRegister.style.display = "block";
        backBoxLogin.style.display = "block";
    } else {
        backBoxRegister.style.display = "block";
        backBoxRegister.style.opacity = "1";
        backBoxLogin.style.display = "none";
        loginForm.style.display = "block";
        loginRegisterContainer.style.left = "0px";
        registerForm.style.display = "none";
    }
}

pageWidth();

function login() {
    if (window.innerWidth > 850) {
        loginForm.style.display = "block";
        loginRegisterContainer.style.left = "10px";
        registerForm.style.display = "none";
        backBoxRegister.style.opacity = "1";
        backBoxLogin.style.opacity = "0";
    } else {
        loginForm.style.display = "block";
        loginRegisterContainer.style.left = "0px";
        registerForm.style.display = "none";
        backBoxRegister.style.display = "block";
        backBoxLogin.style.display = "none";
    }
}

function register() {
    if (window.innerWidth > 850) {
        registerForm.style.display = "block";
        loginRegisterContainer.style.left = "410px";
        loginForm.style.display = "none";
        backBoxRegister.style.opacity = "0";
        backBoxLogin.style.opacity = "1";
    } else {
        registerForm.style.display = "block";
        loginRegisterContainer.style.left = "0px";
        loginForm.style.display = "none";
        backBoxRegister.style.display = "none";
        backBoxLogin.style.display = "block";
    }
}

//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------

$(document).ready(function () {
    $("#password-toggle-login").click(function () {
        var passwordInput = $("#password-login");
        var icon = $(this).find("i");

        if (passwordInput.attr("type") === "password") {
            passwordInput.attr("type", "text");
            icon.removeClass("fa-eye").addClass("fa-eye-slash");
            $(this).addClass("active");
        } else {
            passwordInput.attr("type", "password");
            icon.removeClass("fa-eye-slash").addClass("fa-eye");
            $(this).removeClass("active");
        }
    });
});

//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------

$(document).ready(function () {
    $("#password-toggle-register").click(function () {
        var passwordInput = $("#password-register");
        var icon = $(this).find("i");

        if (passwordInput.attr("type") === "password") {
            passwordInput.attr("type", "text");
            icon.removeClass("fa-eye").addClass("fa-eye-slash");
            $(this).addClass("active");
        } else {
            passwordInput.attr("type", "password");
            icon.removeClass("fa-eye-slash").addClass("fa-eye");
            $(this).removeClass("active");
        }
    });
});

//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------

var pageTitle = document.getElementById("pageTitle");
var loginButton = document.getElementById("btn-login");
var registerButton = document.getElementById("btn-register");

loginButton.addEventListener("click", function () {
    pageTitle.innerText = "Iniciar Sesión";
});

registerButton.addEventListener("click", function () {
    pageTitle.innerText = "Registrarse";
});
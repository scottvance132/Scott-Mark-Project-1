let usernameInput = document.getElementById('username-input');
let passwordInput = document.getElementById('password-input');
let loginButton = document.getElementById('login-button');

loginButton.addEventListener('click', async (e) => {
    e.preventDefault()
    // console.log('credentials', usernameInput.value, passwordInput.value)
    let res = await fetch('http://127.0.0.1:8080/login', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            "username": usernameInput.value,
            "password": passwordInput.value
        })
    })

    if (res.status == 200) {
        let data = await res.json();
        console.log("Logged in!")
        sessionStorage.setItem("username", usernameInput.value)
        //sessionStorage.setItem('role', 'employee')
        //window.location.href="./user.html"
        if (sessionStorage.getItem("role") == 'employee') {
            window.location.href="./user.html"
        }
        else if (sessionStorage.getItem("role" == 'finance_manager')) {
            window.location.href="./finance_manager.html"
        }
    }

    else if (res.status != 200) {
        console.log("Unsuccessful login")
    }


});
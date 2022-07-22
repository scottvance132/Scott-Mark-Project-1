// let author = document.getElementById('author');
let submitButton = document.getElementById("submit-btn");
let statusButtons = document.querySelectorAll('input[name="status"]')
let username = sessionStorage.getItem('username')


submitButton.addEventListener('click', async (e) => {
    let selectedStatusButton;
    for (let radioBtn of statusButtons) {
        if (radioBtn.checked) {
            selectedStatusButton = radioBtn
            break;
        }
    }
    e.preventDefault();
    try {
        let res = await fetch(`http://127.0.0.1:8080/reimbursements/17`, {
            'credentials': 'include',
            'method': 'PUT',
            'headers': {
                'Content-Type': 'application/json'},
                'body': JSON.stringify({
                    "status": selectedStatusButton.value,
                    "resolver": username
                })})
        if (res.status == 200) {
            console.log("Updated!")
            window.location.href="./finance_manager.html"
        } else {
            console.log("Not 201");
        }
        
        // let data = await res.json();

        // addReimbursement(data);
        
    } catch(err) {
        console.log(err);
    }
});

// function addReimbursement(reimb) {
    
    
// };
let addButton = document.getElementById("submit-btn");
let amount = document.getElementById('amount');
let description = document.getElementById('description');
let author = document.getElementById('author');
let typeButtons = document.querySelectorAll('input[name="type"]')
let username = sessionStorage.getItem('username')


addButton.addEventListener('click', async (e) => {
    let selectedTypeButton;
    for (let radioBtn of typeButtons) {
        if (radioBtn.checked) {
            selectedTypeButton = radioBtn
            break;
        }
    }
    e.preventDefault();
    try {
        let res = await fetch(`http://127.0.0.1:8080/users/${username}/reimbursements`, {
            'credentials': 'include',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json'},
                'body': JSON.stringify({
                    "reimbursement_amount": amount.value,
                    "type": selectedTypeButton.value,
                    "description": description.value,
                    "author": author.value
                })})
        if (res.status == 201) {
            window.location.href="./user.html"
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
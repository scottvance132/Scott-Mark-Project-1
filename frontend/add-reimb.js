let addButton = document.getElementById("submit-btn");
let amount = document.getElementById('amount');
let description = document.getElementById('description');
// let author = document.getElementById('author');
let typeButtons = document.querySelectorAll('input[name="type"]');
let username = sessionStorage.getItem('username');
let receipt = document.getElementById('receipt');
// let receiptConfirmButton = document.getElementById('receipt-confirm-button');

// receiptConfirmButton.addEventListener('click', () =. {

// })

// JSON.stringify({
//     "reimbursement_amount": amount.value,
//     "type": selectedTypeButton.value,
//     "description": description.value,
//     "author": username,
//     "receipt": ("receipt", receipt.files[0])


addButton.addEventListener('click', async (e) => {
    let selectedTypeButton;
    for (let radioBtn of typeButtons) {
        if (radioBtn.checked) {
            selectedTypeButton = radioBtn
            break;
        }
    }
    e.preventDefault();
    const formData = new FormData();
    // const image = new Blob([JSON.stringify({
    //     receipt: receipt.value,
    // })], {
    //     type: 'image/jpeg'
    // });
    // console.log(image)
    formData.append("receipt", receipt.files[0])
    formData.append("description", description.value)
    formData.append("reimbursement_amount", amount.value)
    formData.append("type", selectedTypeButton.value)
    formData.append("author", username)
    console.log(...formData);
    if (!receipt.files[0]) {
        alert("You must upload an image of your receipt!")
    } else {
    try {
        let res = await fetch(`http://127.0.0.1:8080/users/${username}/reimbursements`, {
            'credentials': 'include',
            'method': 'POST',
            
                'body':  formData
                })
            console.log(res)
        if (res.status == 201) {
            window.location.href="./user.html"
        } else {
            let err = await res.json();
            console.log("Not 201");
            alert(err.message);
        }
        
        // let data = await res.json();

        // addReimbursement(data);
        
    } catch(err) {
        console.log(err);
        alert(err.message);
    }}
});

// function addReimbursement(reimb) {
    
    
// };
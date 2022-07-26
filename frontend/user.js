let logoutButton = document.getElementById('logout-button');
let reimbursementTbodyElement = document.getElementById('reimb-table-body');
let addReimbursementButton = document.getElementById('add-reimb-btn');
let username = sessionStorage.getItem('username');
let dropdownButton = document.getElementById('dropdown-btn');
let selectedStatus = document.querySelector('#status-select');
let refreshButton = document.getElementById('refresh-table-btn');
console.log(selectedStatus)
// console.log(dropdownButton)

// var userID = '<%=session.getAttribute("user_info")%>';
// alert(userID);

// console.log(userID)



document.addEventListener('DOMContentLoaded', async (e) => {

    console.log("Hello There")
    try {
        let res = await fetch(`http://127.0.0.1:8080/users/${username}/reimbursements`, {
        'credentials': 'include',
        'method': 'GET',
        'headers': {
            'Content-Type': 'application/json'}});
        
        let data = await res.json();
        console.log(data)

        addReimbursementsToTable(data.reimbursements)
        localStorage.setItem('table_data', data.reimbursements);
    } catch(err) {
        console.log(err);
    }
}
);

logoutButton.addEventListener('click', async (e) => {
    e.preventDefault()
    let res = await fetch('http://127.0.0.1:8080/logout', {
        
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
    })

    if (res.status == 200) {
        console.log("Logged out!")
        window.location.href="./login.html"
    }
});

var q_status;

selectedStatus.addEventListener('change', (e) => {
    //e.preventDefault();
    q_status = e.target.value;
} )

dropdownButton.addEventListener('click', async (e) => {
    e.preventDefault()
    let res = await fetch(`http://127.0.0.1:8080/users/${username}/reimbursements?status=${q_status}`, {
        'credentials': 'include',
        'method': 'GET',
        'headers': {
            'Content-Type': 'application/json'}});
    
    let data = await res.json();
    console.log(q_status)

    reimbursementTbodyElement.innerHTML = ""

    localStorage.getItem('table-data');
})

refreshButton.addEventListener('click', async (e) => {
    //e.preventDefault()
    let res = await fetch(`http://127.0.0.1:8080/users/${username}/reimbursements`, {
        'credentials': 'include',
        'method': 'GET',
        'headers': {
            'Content-Type': 'application/json'}});
    
    let data = await res.json();
    console.log(q_status)

    reimbursementTbodyElement.innerHTML = ""

    addReimbursementsToTable(data.reimbursements);
})

function addReimbursementsToTable(reimb_obj) {
    console.log(typeof(reimb_obj))
      for (reimb of reimb_obj) {  
        let row = document.createElement('tr');

        let idCell = document.createElement('td');
        idCell.innerHTML = reimb.reimb_id
        let amntCell = document.createElement('td');
        amntCell.innerHTML = reimb.amount
        let submitCell = document.createElement('td');
        submitCell.innerHTML = reimb.submitted;
        let submitByCell = document.createElement('td');
        submitByCell.innerHTML = reimb.author
        let resolvedCell = document.createElement('td');
        resolvedCell.innerHTML = reimb.resolved;
        let resolvedByCell = document.createElement('td');
        resolvedByCell.innerHTML = reimb.resolver
        let statusCell = document.createElement('td');
        statusCell.innerHTML = reimb.status
        let typeCell = document.createElement('td');
        typeCell.innerHTML = reimb.type
        let descCell = document.createElement('td');
        descCell.innerHTML = reimb.description
        let receiptCell = document.createElement('td');
        let anchorCell = document.createElement('a');
        anchorCell.setAttribute('href', reimb.receipt);
        anchorCell.innerText = 'receipt';
        receiptCell.appendChild(anchorCell);

        row.appendChild(idCell);
        row.appendChild(amntCell);
        row.appendChild(submitCell);
        row.appendChild(submitByCell);
        row.appendChild(resolvedCell);
        row.appendChild(resolvedByCell);
        row.appendChild(statusCell);
        row.appendChild(typeCell);
        row.appendChild(descCell);
        row.appendChild(receiptCell);

        reimbursementTbodyElement.appendChild(row);
    }
};

addReimbursementButton.addEventListener('click', async (e) => {
    e.preventDefault();


    window.location.href="./add-reimb.html"});
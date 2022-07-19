let logoutButton = document.getElementById('logout-button')

document.addEventListener('DOMContentLoaded', async function loadReimbursements() {
    console.log("Hello There")
    try {
        let res = await fetch(`http://127.0.0.1:8080/users/1/reimbursements`);

        let data = await res.json();

        addReimbursementsToTable(data);
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

function addReimbursementsToTable(reimb) {
    let reimbursementTbodyElement = document.getElementById('reimb-table-body');

    let row = document.createElement('tr');

    let idCell = document.createElement('td');
    idCell.innerHTML = reimb.reimb_id
    let amntCell = createElement('td');
    amntCell.innerHTML = reimb.amount
    let submitByCell = createElement('td');
    submitByCell.innerHTML = reimb.author
    let resolvedByCell = createElement('td');
    resolvedByCell.innerHTML = reimb.resolver
    let statusCell = createElement('td');
    statusCell.innerHTML = reimb.status
    let typeCell = createElement('td');
    typeCell.innerHTML = remb.type
    let descCell = createElement('td');
    descCell.innerHTML = reimb.description
    let receiptCell = createElement('td');
    receiptCell.innerHTML = reimb.receipt

    row.appendChild(idCell);
    row.appendChild(amntCell);
    row.appendChild(submitByCell);
    row.appendChild(resolvedByCell);
    row.appendChild(statusCell);
    row.appendChild(typeCell);
    row.appendChild(descCell);
    row.appendChild(receiptCell);

    reimbursementTbodyElement.appendChild(row);
};
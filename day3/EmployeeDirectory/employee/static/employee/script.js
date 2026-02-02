
let employees = [
    {
        name: "Melba",
        job: "Manager",
        salary: 50000,
        fullTime: true
    },
    {
        name: "Rahul",
        job: "Developer",
        salary: 40000,
        fullTime: false
    }
    
    
];


let list = document.getElementById("employeeList");


if (employees.length === 0) {
    list.innerHTML = "<li>No employees available.</li>";
} else {

    
    for (let i = 0; i < employees.length; i++) {
        let emp = employees[i];

        let statusText = "";
        let statusColor = "";

        if (emp.fullTime) {
            statusText = "Full-Time";
            statusColor = "green";
        } else {
            statusText = "Part-Time";
            statusColor = "red";
        }

        list.innerHTML += `
            <li>
                Name: ${emp.name} <br>
                Job: ${emp.job} <br>
                Salary: ₹${emp.salary} <br>
                <span style="color:${statusColor}">
                    ${statusText}
                </span>
            </li><br>
        `;
    }
}

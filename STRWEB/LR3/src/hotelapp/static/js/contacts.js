let currentPage = 1;
const rowsPerPage = 3;
let sortDirection = {
    name: 'asc',
    phone: 'asc',
    email: 'asc'
};

let rows;

document.addEventListener("DOMContentLoaded", () => {
    rows = document.querySelectorAll('.employee-row');
    displayRows();
});

// Function to show/hide preloader
function togglePreloader(show) {
    const preloader = document.getElementById('preloader');
    preloader.style.display = show ? 'flex' : 'none';
}

function displayRows() {
    const totalRows = rows.length;
    const totalPages = Math.ceil(totalRows / rowsPerPage);

    const allRows = document.querySelectorAll('.employee-row');

    // Hide all rows
    allRows.forEach((row) => {
        row.style.display = 'none';
    });

    console.log(rows);

    // Calculate start and end indices for current page
    const start = (currentPage - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    // Show only the rows for the current page
    for (let i = start; i < end && i < totalRows; i++) {
        rows[i].style.display = '';
    }

    // Update pagination info
    document.getElementById('page-info').textContent = `Страница ${currentPage} из ${totalPages}`;

    // Enable or disable buttons based on current page
    document.getElementById('prev-page').disabled = currentPage === 1;
    document.getElementById('next-page').disabled = currentPage === totalPages;
}

function changePage(direction) {
    const totalRows = document.querySelectorAll('.employee-row').length;
    const totalPages = Math.ceil(totalRows / rowsPerPage);

    currentPage += direction;

    // Ensure current page is within bounds
    if (currentPage < 1) {
        currentPage = 1;
    } else if (currentPage > totalPages) {
        currentPage = totalPages;
    }

    displayRows();
}

// Function to filter table based on user input
function filterTable() {
    togglePreloader(true);
    filterTimeout = setTimeout(() => {
        console.log("filtering");
        const input = document.getElementById('search-input').value.toLowerCase();
        allRows = document.querySelectorAll('.employee-row');
        
        togglePreloader(true);
    
        // Filter rows based on input
        rows = [];
        allRows.forEach(row => {
            const nameCell = row.cells[1].textContent.toLowerCase();
            const phoneCell = row.cells[3].textContent.toLowerCase();
            const emailCell = row.cells[4].textContent.toLowerCase();
            console.log(nameCell, phoneCell, emailCell);
    
            if (nameCell.includes(input) || phoneCell.includes(input) || emailCell.includes(input)) {
                rows.push(row);
            } 
        });
    
        currentPage = 1;
        displayRows();

        togglePreloader(false);
    }, 300);
}

// Function to show details of the selected employee
function showDetails(firstName, lastName, phoneNumber, email) {
   const detailsBlock = document.getElementById('details-block');
   const detailsContent = document.getElementById('details-content');

   detailsContent.innerHTML = `
       <strong>Имя:</strong> ${firstName} ${lastName}<br />
       <strong>Телефон:</strong> ${phoneNumber}<br />
       <strong>Email:</strong> ${email}
   `;
   detailsBlock.style.display = 'block';
}

// Function to sort the table by column
function sortTable(column) {
    const tableBody = document.getElementById('contacts-body');
    const rowsArray = Array.from(tableBody.rows);

    // Determine sort order based on current direction
    let direction;
    
    if (column === 'name') {
        direction = sortDirection.name === 'asc' ? 'desc' : 'asc';
        sortDirection.name = direction; // Update sort direction
        rowsArray.sort((a, b) => {
            const nameA = a.cells[1].textContent.trim().toLowerCase();
            const nameB = b.cells[1].textContent.trim().toLowerCase();
            return direction === 'asc' ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
        });
        
        updateSortIndicator(column, direction);
        
    } else if (column === 'phone') {
        direction = sortDirection.phone === 'asc' ? 'desc' : 'asc';
        sortDirection.phone = direction; // Update sort direction
        rowsArray.sort((a, b) => {
            const phoneA = a.cells[3].textContent.trim();
            const phoneB = b.cells[3].textContent.trim();
            return direction === 'asc' ? phoneA.localeCompare(phoneB) : phoneB.localeCompare(phoneA);
        });
        
        updateSortIndicator(column, direction);
        
    } else if (column === 'email') {
        direction = sortDirection.email === 'asc' ? 'desc' : 'asc';
        sortDirection.email = direction; // Update sort direction
        rowsArray.sort((a, b) => {
            const emailA = a.cells[4].textContent.trim().toLowerCase();
            const emailB = b.cells[4].textContent.trim().toLowerCase();
            return direction === 'asc' ? emailA.localeCompare(emailB) : emailB.localeCompare(emailA);
        });
        
        updateSortIndicator(column, direction);
        
    }

    // Clear existing rows and append sorted ones
    while (tableBody.firstChild) {
        tableBody.removeChild(tableBody.firstChild);
    }
    
    rowsArray.forEach(row => tableBody.appendChild(row));

   // Reset pagination and display first page after sorting
   currentPage = 1;
   displayRows();
}

// Function to update the sort indicator for the sorted column
function updateSortIndicator(column, direction) {
   const indicators = document.querySelectorAll('.sort-indicator');
   indicators.forEach(indicator => indicator.textContent = '');

   let indicatorText;
   if (direction === 'asc') {
       indicatorText = ' ↑';
   } else {
       indicatorText = ' ↓';
   }

   if (column === 'name') {
       indicators[0].textContent += indicatorText; // Name column is at index 0 in header
   } else if (column === 'phone') {
       indicators[1].textContent += indicatorText; // Phone column is at index 2 in header
   } else if (column === 'email') {
       indicators[2].textContent += indicatorText; // Email column is at index 3 in header
   }
}

// Initial call to display the first set of rows
document.addEventListener("DOMContentLoaded", function() {
   displayRows();
});

// Function to toggle the visibility of the employee form
function toggleForm() {
    const form = document.getElementById('employee-form');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}

// Function to validate URL
function validateURL(url) {
    const urlPattern = /^(http:\/\/|https:\/\/).+\.(php|html)$/;
    return urlPattern.test(url);
}

// Function to validate phone number
function validatePhone(phone) {
    const phonePattern = /^(8\d{10}|\+375\s?\(29\)\s?\d{3}[- ]?\d{2}[- ]?\d{2}|\+375\s?29\s?\d{3}[- ]?\d{2}[- ]?\d{2}|8\s?\(029\)\s?\d{7})$/;
    return phonePattern.test(phone);
}

// Function to reset validation styles for input fields
function resetValidationStyles() {
    const inputs = [
        document.getElementById('photo-url'),
        document.getElementById('phone-number'),
        document.getElementById('full-name'),
        document.getElementById('email')
    ];
    
    inputs.forEach(input => {
        input.classList.remove('invalid'); // Remove invalid class
        input.style.border = ''; // Reset border style
        input.style.backgroundColor = ''; // Reset background color
    });
    
    // Clear any validation messages
    document.getElementById('validation-message').textContent = '';
}

// Function to add an employee to the table
function addEmployee() {
    const fullName = document.getElementById('full-name').value.trim();
    const photoURL = document.getElementById('photo-url').value.trim();
    const phoneNumber = document.getElementById('phone-number').value.trim();
    const email = document.getElementById('email').value.trim();
    
    // Reset validation styles
    resetValidationStyles();

    let isValid = true;

    // Validate URL
    if (!validateURL(photoURL)) {
        document.getElementById('photo-url').classList.add('invalid');
        isValid = false;
        alert("Некорректный URL. Он должен начинаться с http:// или https:// и заканчиваться на .php или .html.");
    }

    // Validate Phone Number
    if (!validatePhone(phoneNumber)) {
        document.getElementById('phone-number').classList.add('invalid');
        isValid = false;
        alert("Некорректный номер телефона. Пожалуйста, проверьте формат.");
    }

    // If valid, add the row to the table
    if (isValid) {
        // togglePreloader(true);
        // Show preloader while processing

        // Simulate a delay for adding employee (e.g., API call)
        setTimeout(() => {
            const tableBody = document.getElementById('contacts-body');

            // togglePreloader(true);
            // Create a new row
            const newRow = document.createElement('tr');
            newRow.className = 'employee-row';
            newRow.setAttribute('onclick', `showDetails('${fullName}', '', '${phoneNumber}', '${email}')`);
            newRow.innerHTML = `
                <td><input type='checkbox' name='employee_selection'></td>
                <td>${fullName}</td>
                <td><img src="${photoURL}" alt="${fullName}" class='employee-photo'></td>
                <td>${phoneNumber}</td>
                <td>${email}</td>`;

            tableBody.appendChild(newRow);

            // Clear the form fields after adding
            clearFormFields();

            // Optionally hide the form again
            toggleForm();

            alert("Сотрудник успешно добавлен!", "green");
            rows = document.querySelectorAll('.employee-row');
            
            // Refresh the display rows if needed
            
            // Hide preloader after processing is complete
            // togglePreloader(false);
        }, 300); // Simulate a delay of one second for demonstration purposes
        console.log(rows);
        displayRows();
    }
}

// Function to clear all form fields
function clearFormFields() {
    document.getElementById('full-name').value = '';
    document.getElementById('photo-url').value = '';
    document.getElementById('phone-number').value = '';
    document.getElementById('email').value = '';

    // Reset any validation styles
    resetValidationStyles();
}
// Add mobile menu toggle functionality
document.querySelector('.menu-toggle').addEventListener('click', () => {
    const navLinks = document.querySelector('.nav-links');
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
});

// Example data fetching for stats (replace with backend integration)
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('totalUsers').textContent = '45'; // Fetch total users
    document.getElementById('totalDepartments').textContent = '8'; // Fetch departments
    document.getElementById('totalReports').textContent = '120'; // Fetch reports
});
document.addEventListener("DOMContentLoaded", function () {
    // Fetch and populate colleges
    fetch("backend/get_colleges.php")
        .then((response) => response.json())
        .then((data) => {
            const collegeDropdown = document.getElementById("college_id");
            const collegesTable = document.getElementById("colleges_table");

            let tableHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>College ID</th>
                            <th>College Name</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach((college) => {
                // Populate dropdown
                const option = document.createElement("option");
                option.value = college.id;
                option.textContent = college.name;
                collegeDropdown.appendChild(option);

                // Populate table rows
                tableHTML += `
                    <tr>
                        <td>${college.id}</td>
                        <td>${college.name}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table>`;
            collegesTable.innerHTML = tableHTML;
        });

    // Fetch and populate departments
    fetch("backend/get_departments.php")
        .then((response) => response.json())
        .then((data) => {
            const departmentDropdown = document.getElementById("department_id");
            const departmentsTable = document.getElementById("departments_table");

            let tableHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Department ID</th>
                            <th>Department Name</th>
                            <th>College</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach((dept) => {
                // Populate dropdown
                const option = document.createElement("option");
                option.value = dept.id;
                option.textContent = dept.name;
                departmentDropdown.appendChild(option);

                // Populate table rows
                tableHTML += `
                    <tr>
                        <td>${dept.id}</td>
                        <td>${dept.name}</td>
                        <td>${dept.college_name}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table>`;
            departmentsTable.innerHTML = tableHTML;
        });

    // Fetch and populate levels and courses
    fetch("backend/get_levels_courses.php")
        .then((response) => response.json())
        .then((data) => {
            const levelsCoursesTable = document.getElementById("levels_courses_table");

            let tableHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Level</th>
                            <th>Course Code</th>
                            <th>Course Name</th>
                            <th>Department</th>
                            <th>Students</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach((course) => {
                // Populate table rows
                tableHTML += `
                    <tr>
                        <td>${course.level}</td>
                        <td>${course.course_code}</td>
                        <td>${course.course_name}</td>
                        <td>${course.department_name}</td>
                        <td>${course.students_count}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table>`;
            levelsCoursesTable.innerHTML = tableHTML;
        });

    // Fetch and populate combined courses
    fetch("backend/get_combined_courses.php")
        .then((response) => response.json())
        .then((data) => {
            const combinedCoursesTable = document.getElementById("combined_courses_table");

            let tableHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Course Code</th>
                            <th>Course Name</th>
                            <th>Departments</th>
                            <th>Total Students</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach((combined) => {
                // Populate table rows
                tableHTML += `
                    <tr>
                        <td>${combined.course_code}</td>
                        <td>${combined.course_name}</td>
                        <td>${combined.departments.join(", ")}</td>
                        <td>${combined.students_count}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table>`;
            combinedCoursesTable.innerHTML = tableHTML;
        });

    // Fetch and populate venues
    fetch("backend/get_venues.php")
        .then((response) => response.json())
        .then((data) => {
            const venuesTable = document.getElementById("venues_table");

            let tableHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Venue Name</th>
                            <th>Capacity</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach((venue) => {
                // Populate table rows
                tableHTML += `
                    <tr>
                        <td>${venue.name}</td>
                        <td>${venue.capacity}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table>`;
            venuesTable.innerHTML = tableHTML;
        });

    // Fetch and populate staff
    fetch("backend/get_staff.php")
        .then((response) => response.json())
        .then((data) => {
            const staffTable = document.getElementById("staff_table");

            let tableHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Staff Name</th>
                            <th>Email</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach((staff) => {
                // Populate table rows
                tableHTML += `
                    <tr>
                        <td>${staff.name}</td>
                        <td>${staff.email}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table>`;
            staffTable.innerHTML = tableHTML;
        });
});

<?php
// Include database connection
include('db_connection.php');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="data_creation.css">
</head>
<body>
    <header>
        <h1>Admin Dashboard</h1>
        <nav>
            <ul>
                <li><a href="#colleges">Colleges</a></li>
                <li><a href="#departments">Departments</a></li>
                <li><a href="#levels">Levels & Courses</a></li>
                <li><a href="#venues">Venues</a></li>
                <li><a href="#staff">Staff List</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Colleges Section -->
        <section id="colleges">
            <h2>Manage Colleges</h2>
            <form action="add_college.php" method="post">
                <label for="college_name">College Name:</label>
                <input type="text" id="college_name" name="college_name" required>
                <button type="submit">Add College</button>
            </form>

            <h3>Existing Colleges</h3>
            <table>
                <thead>
                    <tr>
                        <th>College ID</th>
                        <th>College Name</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    // Fetch colleges from database
                    $colleges = $conn->query("SELECT * FROM colleges");
                    while ($college = $colleges->fetch_assoc()) {
                        echo "<tr>
                            <td>{$college['id']}</td>
                            <td>{$college['name']}</td>
                            <td>
                                <form action='delete_college.php' method='post' style='display:inline;'>
                                    <input type='hidden' name='college_id' value='{$college['id']}'>
                                    <button type='submit'>Delete</button>
                                </form>
                            </td>
                        </tr>";
                    }
                    ?>
                </tbody>
            </table>
        </section>

        <!-- Departments Section -->
        <section id="departments">
            <h2>Manage Departments</h2>
            <form action="add_department.php" method="post">
                <label for="college_id">Select College:</label>
                <select id="college_id" name="college_id" required>
                    <?php
                    // Fetch colleges for dropdown
                    $colleges = $conn->query("SELECT * FROM colleges");
                    while ($college = $colleges->fetch_assoc()) {
                        echo "<option value='{$college['id']}'>{$college['name']}</option>";
                    }
                    ?>
                </select>

                <label for="department_name">Department Name:</label>
                <input type="text" id="department_name" name="department_name" required>
                <button type="submit">Add Department</button>
            </form>

            <h3>Existing Departments</h3>
            <table>
                <thead>
                    <tr>
                        <th>Department ID</th>
                        <th>Department Name</th>
                        <th>College</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    // Fetch departments from database
                    $departments = $conn->query("SELECT d.id, d.name, c.name as college_name 
                                                 FROM departments d 
                                                 JOIN colleges c ON d.college_id = c.id");
                    while ($dept = $departments->fetch_assoc()) {
                        echo "<tr>
                            <td>{$dept['id']}</td>
                            <td>{$dept['name']}</td>
                            <td>{$dept['college_name']}</td>
                            <td>
                                <form action='delete_department.php' method='post' style='display:inline;'>
                                    <input type='hidden' name='department_id' value='{$dept['id']}'>
                                    <button type='submit'>Delete</button>
                                </form>
                            </td>
                        </tr>";
                    }
                    ?>
                </tbody>
            </table>
        </section>

        <!-- Additional sections (Levels, Venues, Staff) would follow similar structure -->
    </main>
</body>
</html>

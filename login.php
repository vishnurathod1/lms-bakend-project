<?php
session_start();

// Database connection
$servername = "localhost";
$username = "root";
$password = "Vishnu@123";
$dbname = "Registration";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Function to capitalize first letter
function capitalizeFirstLetter($string) {
    return ucfirst(strtolower($string));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = trim($_POST['email']);
    $password = $_POST['password'];
    $userType = $_POST['userType'];

    // Validation
    if (empty($email) || empty($password) || empty($userType)) {
        echo "<script>alert('All fields are required.'); window.history.back();</script>";
        exit();
    }

    // Check if user exists and password matches
    $stmt = $conn->prepare("SELECT * FROM users WHERE email = ? AND userType = ?");
    $stmt->bind_param("ss", $email, $userType);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        // Note: In a real application, password should be hashed. Here assuming plain text for simplicity.
        if ($user['password'] === $password) {
            $_SESSION['currentUser'] = $user;
            // Redirect based on user type
            if ($userType === 'admin') {
                header("Location: admin_home.html");
            } elseif ($userType === 'trainer') {
                $subject = $user['subject'];
                if ($subject === 'js') {
                    header("Location: js_trainer.html");
                } elseif ($subject === 'css') {
                    header("Location: css_trainer.html");
                } elseif ($subject === 'java') {
                    header("Location: java.html");
                } elseif ($subject === 'python') {
                    header("Location: Python.html");
                } else {
                    header("Location: subject_trainer.html");
                }
            } elseif ($userType === 'trainee') {
                header("Location: student_home.html");
            }
            exit();
        } else {
            echo "<script>alert('Invalid password.'); window.history.back();</script>";
            exit();
        }
    } else {
        echo "<script>alert('User not found.'); window.history.back();</script>";
        exit();
    }

    $stmt->close();
}

mysqli_close($conn);
?>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $first_name = $_POST['first_name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $transaction_code = $_POST['transaction_code'];

    // To send email, replace 'your_email@example.com' with your own email
    $to = 'francisnjaramba2@gmail.com.com';
    $subject = 'New Message from '.$first_name;
    $headers = 'From: '.$email."\r\n";

    if (!empty($message)) {
        mail($to, $subject, $message, $headers);
        echo "Your message has been sent successfully!";
    } else {
        echo "Please enter a message.";
    }
} else {
    echo "This page was accessed directly. Please use the form to submit data.";
}
?>

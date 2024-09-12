public class NotificationService {

    public void sendEmailNotification(String recipient, String message) {
        // Code to send email
        System.out.println("Sending Email to " + recipient + ": " + message);
    }

    // Removing unused methods for SMS and Push notifications

    public void sendNotification(String recipient, String message) {
        // As only email is supported currently, we simplify the method
        sendEmailNotification(recipient, message);
    }
}

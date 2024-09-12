public class NotificationService {
    
    public void sendEmailNotification(String recipient, String message) {
        // Code to send email
        System.out.println("Sending Email to " + recipient + ": " + message);
    }

    public void sendSMSNotification(String recipient, String message) {
        // Code to send SMS (currently not implemented)
        System.out.println("Sending SMS to " + recipient + ": " + message);
    }

    public void sendPushNotification(String recipient, String message) {
        // Code to send Push Notification (currently not implemented)
        System.out.println("Sending Push Notification to " + recipient + ": " + message);
    }

    public void sendNotification(String recipient, String message, String type) {
        if (type.equals("EMAIL")) {
            sendEmailNotification(recipient, message);
        } else if (type.equals("SMS")) {
            sendSMSNotification(recipient, message);
        } else if (type.equals("PUSH")) {
            sendPushNotification(recipient, message);
        } else {
            throw new IllegalArgumentException("Unknown notification type: " + type);
        }
    }
}

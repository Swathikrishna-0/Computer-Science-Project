import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from win10toast import ToastNotifier

def send_notification(message):
    toaster = ToastNotifier()
    toaster.show_toast("Security Alert", message, duration=10)

def send_email_alert(to_email, subject, body):
    from_email = "your_email@example.com"
    password = "your_password"
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    send_notification("High risk detected in package 'requests'")
    send_email_alert("recipient@example.com", "Security Alert", "Vulnerability found in 'requests' package.")

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

def send_attendance_email(subject, filename, faculty_email):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    email_user = 'facerecogsystem0@gmail.com'
    email_password = 'nscj vorj dfte rpey'

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = faculty_email
    msg['Subject'] = f'Attendance Report for {subject}'

    # Email body
    body = f'Please find the attendance report for {subject} attached.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the CSV file
    with open(filename, 'rb') as f:
        part = MIMEApplication(f.read(), Name=os.path.basename(filename))
        part['Content-Disposition'] = f'attachment; filename={os.path.basename(filename)}'
        msg.attach(part)

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, faculty_email, msg.as_string())
        server.quit()

        print(f"Email sent to {faculty_email} for {subject}")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Dictionary mapping subjects to faculty email IDs
subject_faculty_mapping = {
    'CC': 'gadalaymallika@gmail.com',
    'NLP': 'gadalaymallika@gmail.com',
    'PA': 'rahulsingh30145@gmail.com',
    'WA': 'kota.akshita0710@gmail.com',
    'POE': 'kota.akshita0710@gmail.com',
}

for subject, faculty_email in subject_faculty_mapping.items():
    subject_folder = f"./attendances/{subject}"
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    filename = f"{subject_folder}/{subject}_{date_str}_attendance.csv"

    # Assuming the attendance file has already been created with the correct data

    send_attendance_email(subject, filename, faculty_email)


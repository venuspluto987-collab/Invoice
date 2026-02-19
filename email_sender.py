import yagmail

def send_invoice(email, file_path):
    yag = yagmail.SMTP("yourmail@gmail.com", "APP_PASSWORD")

    yag.send(
        to=email,
        subject="Your Invoice",
        contents="Thank you for your business!",
        attachments=file_path
    )

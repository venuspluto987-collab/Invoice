import pdfkit

WKHTML_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=WKHTML_PATH)

def generate_invoice(name, amount):
    html = f"""
    <html>
    <body>
        <h1>INVOICE</h1>
        <h2>Customer: {name}</h2>
        <h2>Amount: ₹{amount}</h2>
    </body>
    </html>
    """

    file_name = f"invoice_{name}.pdf"

    pdfkit.from_string(html, file_name, configuration=config)

    return file_name   # ✅ MUST return string



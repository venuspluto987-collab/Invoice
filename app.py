from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pdfkit

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# wkhtmltopdf path
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

class Invoice(BaseModel):
    name: str
    product: str
    amount: str

@app.post("/create-pdf")
def create_pdf(data: Invoice):

    html = f"""
    <html>
    <body style='font-family:Arial'>
    <h1>Invoice</h1>
    <hr>
    <p><b>Customer:</b> {data.name}</p>
    <p><b>Product:</b> {data.product}</p>
    <p><b>Amount:</b> ₹{data.amount}</p>
    </body>
    </html>
    """

    pdf_file = "invoice.pdf"
    pdfkit.from_string(html, pdf_file, configuration=config)

    # ✅ MUST return FileResponse (not JSON)
    return FileResponse(pdf_file, media_type="application/pdf", filename="invoice.pdf")

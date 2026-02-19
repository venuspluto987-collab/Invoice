# invoice_generator.py

def generate_invoice(name, amount):
    return {
        "customer": name,
        "amount": amount,
        "status": "Invoice Generated Successfully"
    }

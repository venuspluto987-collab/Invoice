from sqlalchemy import Column, Integer, String, Float
from database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_email = Column(String)
    item = Column(String)
    amount = Column(Float)
    gst = Column(Float)
    total = Column(Float)

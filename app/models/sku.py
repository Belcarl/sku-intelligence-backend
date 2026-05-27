from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SKU(Base):
	__tablename__ = "skus"

	id = Column(Integer, primary_key=True, index=True)
	sku_code = Column(String, index=True)
	user_id = Column(Integer, ForeignKey("users.id"))

	def __repr__(self):
		return f"<SKU(id={self.id}, sku_code={self.sku_code}, user_id={self.user_id})>"

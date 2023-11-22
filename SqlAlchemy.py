import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer,String
engine = db.create_engine("sqlite:///employees.sqlite")
conn = engine.connect()
metadata = db.MetaData()
employee = db.Table('Employee', metadata,

db.Column('id', db.Integer(), primary_key=True),

db.Column('name', db.String(255), nullable=False),
db.Column('address', db.String(1024), default="Nammane"),
db.Column('pic_id', db.String(1024), default="default")
)

metadata.create_all(engine)
# Initialize a db session
Base = declarative_base()
session = sessionmaker(bind=engine)()
# Save an entry to DB.
class Employee_Company(Base):
    __tablename__ = "employee"
    name = Column(String)
    id = Column(Integer, primary_key=True)
    address = Column(String)
    pic_id = Column(String)
    def __init__(self, name, id, address, pic_id='default'):
        super().__init__()
        self.name = name
        self.id = id
        self.address = address
        self.pic_id = 'default'
    def save(self):
        session.add(self)
        session.commit()
    def get_by_id(self):
        emp = session.query(employee).filter_by(id=self.id).first()
        return emp
#
employee4 = Employee_Company("Srihari", 2, "JP Nagara")
#employee4.save()
print(employee4.get_by_id())
#session.add(employee4)
#session.commit()
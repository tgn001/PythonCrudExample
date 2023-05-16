from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, role, id=None):
        if id:
            self.id = id
        self.name = name
        self.role = role
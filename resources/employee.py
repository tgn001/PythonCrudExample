from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import EmployeeModel
from schemas import EmployeeSchema, EmployeeUpdateSchema

empblueprint = Blueprint("Employees", "employees", description="TechGeekNext - Employee CRUD operations")


@empblueprint.route("/employee/<string:emp_id>")
class Employee(MethodView):
    @empblueprint.response(200, EmployeeSchema)
    def get(self, emp_id):
        return EmployeeModel.query.get_or_404(emp_id)


    def delete(self, emp_id):
        emp = EmployeeModel.query.get_or_404(emp_id)
        db.session.delete(emp)
        db.session.commit()
        return {"message": "Employee deleted."}

    @empblueprint.arguments(EmployeeUpdateSchema)
    @empblueprint.response(200, EmployeeSchema)
    def put(self, emp_data, emp_id):
        emp = EmployeeModel.query.get(emp_id)

        if emp:
            emp.name = emp_data["name"]
            emp.role = emp_data["role"]
        else:
            emp = EmployeeModel(id=emp_id, **emp_data)

        db.session.add(emp)
        db.session.commit()

        return


@empblueprint.route("/employees")
class GetEmployees(MethodView):
    @empblueprint.response(200, EmployeeSchema(many=True))
    def get(self):
        return EmployeeModel.query.all()


@empblueprint.route("/employee")
class CreateEmp(MethodView):
    @empblueprint.arguments(EmployeeSchema)
    @empblueprint.response(201, EmployeeSchema)
    def post(self, emp_data):
        emp = EmployeeModel(**emp_data)
        try:
            db.session.add(emp)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating an employee.")

        return
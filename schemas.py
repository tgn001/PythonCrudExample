from marshmallow import Schema, fields

class EmployeeSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)

class EmployeeUpdateSchema(Schema):
    name = fields.Str()
    role = fields.Str()
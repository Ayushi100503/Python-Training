from contourpy.util import data
from flask import Flask, request, jsonify
app = Flask(__name__)
employees = [
    {"id":1, "name":"Ayushi", "age":22, "salary":100000},
    {"id":2, "name":"Ankur", "age":24, "salary":50000},
    {"id":3, "name":"Sriparna", "age":25, "salary":90000},
    {"id":4, "name":"Tuneer", "age":23, "salary":40000}
]
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees", methods=["POST"])
def add_employees():
    data = request.get_json()
    data["id"] = len(employees)+1
    employees.append(data)
    return "POST EXECUTED"


@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.get_json()
    for employee in employees:
        if employee["id"] == emp_id:
            employee.update(data)
            return jsonify({"message": "Employee updated successfully", "employee": employee})
    return jsonify({"message": "Employee not found"})


@app.route("/employees/<int:e_id>", methods=["DELETE"])
def delete_employee(e_id):
    global employees
    employees = [e for e in employees if e["id"] != e_id]
    return jsonify({"message": "Employee deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
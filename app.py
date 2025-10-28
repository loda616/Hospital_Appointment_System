from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps

from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from models import Appointment

from config import API_KEY

with app.app_context():
    db.create_all()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-api-key' in request.headers:
            token = request.headers['x-api-key']

        if not token or token != API_KEY:
            return jsonify({'message': 'Token is missing or invalid!'}), 401

        return f(*args, **kwargs)
    return decorated

@app.route('/api/appointments', methods=['POST'])
@token_required
def create_appointment():
    data = request.get_json()
    if not data or not all(key in data for key in ['patient_name', 'doctor_id', 'specialty', 'date_time']):
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        date_time = datetime.fromisoformat(data['date_time'])
        if date_time < datetime.now():
            return jsonify({'message': 'Appointment date must be in the future'}), 400
    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400

    new_appointment = Appointment(
        patient_name=data['patient_name'],
        doctor_id=data['doctor_id'],
        specialty=data['specialty'],
        date_time=date_time,
        status=data.get('status', 'Scheduled')
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    query = Appointment.query

    doctor_id = request.args.get('doctor_id')
    if doctor_id:
        query = query.filter_by(doctor_id=doctor_id)

    specialty = request.args.get('specialty')
    if specialty:
        query = query.filter_by(specialty=specialty)

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if start_date and end_date:
        try:
            start_date_obj = datetime.fromisoformat(start_date)
            end_date_obj = datetime.fromisoformat(end_date)
            query = query.filter(Appointment.date_time.between(start_date_obj, end_date_obj))
        except ValueError:
            return jsonify({'message': 'Invalid date format for date range filtering'}), 400

    appointments = query.all()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

@app.route('/api/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404
    return jsonify(appointment.to_dict()), 200

@app.route('/api/appointments/<int:id>', methods=['PUT'])
@token_required
def update_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404

    data = request.get_json()
    if 'date_time' in data:
        try:
            date_time = datetime.fromisoformat(data['date_time'])
            if date_time < datetime.now():
                return jsonify({'message': 'Appointment date must be in the future'}), 400
            appointment.date_time = date_time
        except ValueError:
            return jsonify({'message': 'Invalid date format'}), 400
    if 'status' in data:
        appointment.status = data['status']

    db.session.commit()
    return jsonify(appointment.to_dict()), 200

@app.route('/api/appointments/<int:id>', methods=['DELETE'])
@token_required
def delete_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404

    db.session.delete(appointment)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
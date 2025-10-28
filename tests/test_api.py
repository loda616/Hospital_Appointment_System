import unittest
import json
from app import app
from extensions import db
from models import Appointment
from datetime import datetime, timedelta

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_appointment_success(self):
        future_date = datetime.now() + timedelta(days=1)
        response = self.app.post('/api/appointments',
                                 data=json.dumps({
                                     'patient_name': 'John Doe',
                                     'doctor_id': 'DR200',
                                     'specialty': 'General Practice',
                                     'date_time': future_date.isoformat()
                                 }),
                                 content_type='application/json',
                                 headers={'x-api-key': 'your-secret-api-key'})
        self.assertEqual(response.status_code, 201)

    def test_create_appointment_missing_fields(self):
        response = self.app.post('/api/appointments',
                                 data=json.dumps({'patient_name': 'John Doe'}),
                                 content_type='application/json',
                                 headers={'x-api-key': 'your-secret-api-key'})
        self.assertEqual(response.status_code, 400)

    def test_create_appointment_past_date(self):
        past_date = datetime.now() - timedelta(days=1)
        response = self.app.post('/api/appointments',
                                 data=json.dumps({
                                     'patient_name': 'John Doe',
                                     'doctor_id': 'DR200',
                                     'specialty': 'General Practice',
                                     'date_time': past_date.isoformat()
                                 }),
                                 content_type='application/json',
                                 headers={'x-api-key': 'your-secret-api-key'})
        self.assertEqual(response.status_code, 400)

    def test_get_appointments_success(self):
        response = self.app.get('/api/appointments')
        self.assertEqual(response.status_code, 200)

    def test_get_appointment_not_found(self):
        response = self.app.get('/api/appointments/999')
        self.assertEqual(response.status_code, 404)

    def test_update_appointment_success(self):
        with app.app_context():
            future_date = datetime.now() + timedelta(days=1)
            appointment = Appointment(patient_name='Jane Doe', doctor_id='DR100', specialty='Cardiology', date_time=future_date)
            db.session.add(appointment)
            db.session.commit()
            appointment_id = appointment.appointment_id

        response = self.app.put(f'/api/appointments/{appointment_id}',
                                data=json.dumps({'status': 'Completed'}),
                                content_type='application/json',
                                headers={'x-api-key': 'your-secret-api-key'})
        self.assertEqual(response.status_code, 200)

    def test_delete_appointment_success(self):
        with app.app_context():
            future_date = datetime.now() + timedelta(days=1)
            appointment = Appointment(patient_name='Jane Doe', doctor_id='DR100', specialty='Cardiology', date_time=future_date)
            db.session.add(appointment)
            db.session.commit()
            appointment_id = appointment.appointment_id

        response = self.app.delete(f'/api/appointments/{appointment_id}',
                                   headers={'x-api-key': 'your-secret-api-key'})
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

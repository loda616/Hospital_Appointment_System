import unittest
import json
from app import app, db
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

    def test_create_appointment(self):
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

    def test_get_appointments(self):
        response = self.app.get('/api/appointments')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

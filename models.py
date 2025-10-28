from extensions import db

class Appointment(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    doctor_id = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Scheduled')

    def to_dict(self):
        return {
            'appointment_id': self.appointment_id,
            'patient_name': self.patient_name,
            'doctor_id': self.doctor_id,
            'specialty': self.specialty,
            'date_time': self.date_time.isoformat(),
            'status': self.status
        }
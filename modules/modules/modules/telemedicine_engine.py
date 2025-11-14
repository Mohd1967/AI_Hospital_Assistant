"""
telemedicine_engine.py
وظائف بسيطة لحجوزات الاستشارة عن بعد وتهيئة المعلومات للمستخدم.
(هذه نسخة مبسطة جداً للتجربة)
"""

APPOINTMENTS = []

def book_appointment(patient_name: str, datetime_str: str, specialty: str = "General"):
    appt = {
        "patient": patient_name,
        "datetime": datetime_str,
        "specialty": specialty,
        "status": "booked"
    }
    APPOINTMENTS.append(appt)
    return appt

def list_appointments():
    return APPOINTMENTS

if __name__ == "__main__":
    print(book_appointment("Ahmed", "2025-11-20 10:00", "Internal Medicine"))
    print(list_appointments())

# Hospital Appointment Scheduling API

This project is a simple, yet powerful, Hospital Appointment Scheduling API built with Python and Flask. It provides a complete set of CRUD endpoints for managing patient appointments, along with advanced features like filtering and token-based authentication.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete appointments.
- **Filtering:** Filter appointments by doctor, specialty, or a specific date range.
- **Authentication:** Secure `POST`, `PUT`, and `DELETE` endpoints with token-based authentication.
- **Detailed Documentation:** Comes with comprehensive API documentation to get you started quickly.

## Project Structure

```
.
├── app.py              # Main Flask application
├── models.py           # Database models
├── config.py           # Configuration for API key
├── requirements.txt    # Project dependencies
├── API_DOCUMENTATION.md # Detailed API documentation
└── instance/
    └── appointments.db # SQLite database file
```

## Getting Started

Follow these instructions to get the API up and running on your local machine.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

The API uses an API key to protect certain endpoints. You can set this key as an environment variable for better security.

**Set the API Key:**

-   **On macOS/Linux:**
    ```bash
    export API_KEY="your-custom-api-key"
    ```

-   **On Windows (Command Prompt):**
    ```bash
    set API_KEY="your-custom-api-key"
    ```

-   **On Windows (PowerShell):**
    ```bash
    $env:API_KEY="your-custom-api-key"
    ```

If you don't set this variable, the application will use the default key: `your-secret-api-key`.

### Running the Application

Once you've installed the dependencies and configured the API key, you can run the application with a single command:

```bash
flask run
```

The API will start on `http://127.0.0.1:5000`.

## How to Use the API

You can interact with the API using any HTTP client, such as `curl` or Postman. Here are some examples using `curl`.

### Create a New Appointment

To create a new appointment, you'll need to send a `POST` request with the appointment details and your API key in the header.

```bash
curl -i -X POST \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-custom-api-key" \
  -d '{"patient_name": "John Smith", "doctor_id": "DR300", "specialty": "Dermatology", "date_time": "2025-12-01T10:00:00"}' \
  http://127.0.0.1:5000/api/appointments
```

### Get All Appointments

You can retrieve all appointments with a simple `GET` request. No API key is needed for this endpoint.

```bash
curl -i http://127.0.0.1:5000/api/appointments
```

### Filter Appointments

You can also filter appointments by `doctor_id`, `specialty`, or a date range.

-   **By Doctor ID:**
    ```bash
    curl -i "http://127.0.0.1:5000/api/appointments?doctor_id=DR300"
    ```

-   **By Date Range:**
    ```bash
    curl -i "http://127.0.0.1:5000/api/appointments?start_date=2025-12-01T00:00:00&end_date=2025-12-31T23:59:59"
    ```

### Update an Appointment

To update an appointment, send a `PUT` request with the fields you want to change. Remember to include your API key.

```bash
curl -i -X PUT \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-custom-api-key" \
  -d '{"status": "Completed"}' \
  http://127.0.0.1:5000/api/appointments/1
```

### Delete an Appointment

You can delete an appointment by sending a `DELETE` request with the appointment ID.

```bash
curl -i -X DELETE \
  -H "x-api-key: your-custom-api-key" \
  http://127.0.0.1:5000/api/appointments/1
```

For more detailed information on each endpoint, check out the [API Documentation](API_DOCUMENTATION.md).

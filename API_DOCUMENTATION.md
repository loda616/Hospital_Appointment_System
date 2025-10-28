# Hospital Appointment Scheduling API Documentation

## Introduction

The Hospital Appointment Scheduling API allows clients to manage patient appointments with doctors. It provides CRUD (Create, Read, Update, Delete) operations for appointment records.

## Authentication

The API uses a simple token-based authentication mechanism. To access the protected endpoints (`POST`, `PUT`, `DELETE`), you need to include an API key in the `x-api-key` header of your request.

**API Key:** `your-secret-api-key`

## Endpoints

The base path for all endpoints is `/api/appointments`.

---

### 1. Create a new appointment

*   **Method:** `POST`
*   **Endpoint:** `/api/appointments`
*   **Description:** Creates a new appointment record.
*   **Authentication:** Required.
*   **Request Body:**
    ```json
    {
        "patient_name": "Jane Doe",
        "doctor_id": "DR100",
        "specialty": "Cardiology",
        "date_time": "2025-11-15T14:00:00"
    }
    ```
*   **Success Response (201 Created):**
    ```json
    {
        "appointment_id": 1,
        "patient_name": "Jane Doe",
        "doctor_id": "DR100",
        "specialty": "Cardiology",
        "date_time": "2025-11-15T14:00:00",
        "status": "Scheduled"
    }
    ```
*   **Error Response (400 Bad Request):**
    ```json
    {
        "message": "Missing required fields"
    }
    ```
    ```json
    {
        "message": "Appointment date must be in the future"
    }
    ```

---

### 2. Retrieve all appointments

*   **Method:** `GET`
*   **Endpoint:** `/api/appointments`
*   **Description:** Retrieves a list of all appointments. Supports filtering.
*   **Authentication:** Not required.
*   **Query Parameters (Optional):**
    *   `doctor_id` (string): Filter by doctor's ID.
    *   `specialty` (string): Filter by specialty.
    *   `start_date` (string): The start of the date range (ISO 8601 format).
    *   `end_date` (string): The end of the date range (ISO 8601 format).
*   **Success Response (200 OK):**
    ```json
    [
        {
            "appointment_id": 1,
            "patient_name": "Jane Doe",
            "doctor_id": "DR100",
            "specialty": "Cardiology",
            "date_time": "2025-11-15T14:00:00",
            "status": "Scheduled"
        }
    ]
    ```

---

### 3. Retrieve a specific appointment

*   **Method:** `GET`
*   **Endpoint:** `/api/appointments/{id}`
*   **Description:** Retrieves a single appointment by its `appointment_id`.
*   **Authentication:** Not required.
*   **Success Response (200 OK):**
    ```json
    {
        "appointment_id": 1,
        "patient_name": "Jane Doe",
        "doctor_id": "DR100",
        "specialty": "Cardiology",
        "date_time": "2025-11-15T14:00:00",
        "status": "Scheduled"
    }
    ```
*   **Error Response (404 Not Found):**
    ```json
    {
        "message": "Appointment not found"
    }
    ```

---

### 4. Update an existing appointment

*   **Method:** `PUT`
*   **Endpoint:** `/api/appointments/{id}`
*   **Description:** Updates the date, time, or status of an existing appointment.
*   **Authentication:** Required.
*   **Request Body:**
    ```json
    {
        "date_time": "2025-11-15T15:00:00",
        "status": "Completed"
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
        "appointment_id": 1,
        "patient_name": "Jane Doe",
        "doctor_id": "DR100",
        "specialty": "Cardiology",
        "date_time": "2025-11-15T15:00:00",
        "status": "Completed"
    }
    ```
*   **Error Response (404 Not Found):**
    ```json
    {
        "message": "Appointment not found"
    }
    ```

---

### 5. Delete an appointment

*   **Method:** `DELETE`
*   **Endpoint:** `/api/appointments/{id}`
*   **Description:** Deletes an appointment record.
*   **Authentication:** Required.
*   **Success Response (204 No Content):** (No response body)
*   **Error Response (404 Not Found):**
    ```json
    {
        "message": "Appointment not found"
    }
    ```

# API Key Generation Guide

## Understanding the API Authentication

This Hospital Appointment Scheduling API uses a **single, static API key** for authenticating requests to protected endpoints (`POST`, `PUT`, `DELETE`). This key acts as a shared secret for the entire service. The system is not designed to generate unique keys for individual users.

The API key must be set as an environment variable named `API_KEY` on the server where the application is running. It is crucial for the security of your API that this key is a **strong, cryptographically random string**.

**Warning:** Do not use simple, predictable strings or default keys in a production environment.

## How to Generate a Secure API Key

Here are several recommended methods for generating a secure and random API key. You only need to use one of these methods.

### Method 1: Using OpenSSL

OpenSSL is a robust and widely available tool on most Linux, macOS, and Windows (with WSL or Git Bash) systems. This command generates 32 random bytes and Base64 encodes them, which is an excellent format for an API key.

1.  Open your terminal.
2.  Run the following command:

    ```bash
    openssl rand -base64 32
    ```

3.  **Example Output:**

    ```
    wJ/3q+s9g8b/v6a7d8e+f9g/h0i+j1k/l2m/n3o/p4q/r5s=
    ```

4.  Copy the generated string. This is your new API key.

### Method 2: Using Python

Python's built-in `secrets` module is designed for generating cryptographically strong random numbers suitable for managing secrets like API keys.

1.  Open your terminal.
2.  Run the following command:

    ```bash
    python -c 'import secrets; print(secrets.token_hex(32))'
    ```

3.  **Example Output:**
    ```
    c2e0f8b1a3d6e5f4a1b3c2d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4
    ```
4.  Copy the generated hexadecimal string. This is your new API key.

## How to Use the Generated Key

Once you have generated your key, you must set it as the `API_KEY` environment variable on your server.

For detailed instructions on how to set the environment variable, please refer to the **Configuration** section in the [README.md](README.md) file.

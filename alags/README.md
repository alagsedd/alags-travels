# Alags - Social Media Application

Alags is a full-stack social media application built with a Flask backend and a React frontend.

## Project Structure

```
alags/
├── backend/        # Flask backend application
│   ├── app.py      # Main Flask application file, app factory
│   ├── config.py   # Configuration settings (dev, prod, test)
│   ├── models/     # SQLAlchemy database models
│   ├── routes/     # (To be added) API Blueprints/routes
│   ├── migrations/ # Flask-Migrate migration scripts
│   ├── tests/      # (To be added) Backend tests
│   ├── .env        # Environment variables for backend
│   └── requirements.txt # Python dependencies
│
├── frontend/       # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── components/ # (To be added) React components
│   │   ├── pages/      # (To be added) Page components
│   │   ├── App.js
│   │   ├── index.js
│   │   └── ... (other React files)
│   ├── .env        # Environment variables for frontend (if any)
│   └── package.json  # Node dependencies and scripts
│
└── README.md       # This file
```

## Setup and Running Locally

### Prerequisites

*   Python 3.8+ and pip
*   Node.js (v16+) and npm

### Backend (Flask)

1.  **Navigate to the backend directory:**
    ```bash
    cd alags/backend
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Copy the example `.env` file if you need to make local modifications, though the defaults should work for SQLite development.
    Ensure `FLASK_APP=app.py` and `FLASK_ENV=development` are set (they are in the provided `.env`).

5.  **Set up the database:**
    From the `alags/backend` directory:
    ```bash
    # If you are setting up for the first time or need to re-migrate:
    # (Assumes FLASK_APP=app.py is set in .env or exported)
    # flask db init  (Only if migrations folder doesn't exist)
    # flask db migrate -m "Initial setup"
    flask db upgrade
    ```
    *Note: The initial migration has been created. `flask db upgrade` ensures your schema is up to date.*

6.  **Run the Flask development server:**
    From the `alags/backend` directory:
    ```bash
    flask run
    ```
    The backend will typically be available at `http://127.0.0.1:5000`.

### Frontend (React)

1.  **Navigate to the frontend directory:**
    ```bash
    cd alags/frontend
    ```
    *(If you are in `alags/backend`, you'd do `cd ../frontend`)*

2.  **Install Node dependencies:**
    ```bash
    npm install
    ```

3.  **Run the React development server:**
    ```bash
    npm start
    ```
    The frontend will typically be available at `http://localhost:3000` and should open automatically in your browser.

## Further Development

(Placeholder for future information on API design, component structure, etc.)

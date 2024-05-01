# password-checker-app

## Description

Password-checker-app is a simple web application built to help users assess the security, strength of their passwords. It checks various criteria such as uppercase letters, lowercase letters, digits, symbols, and whether the password has been breached in any known data leaks. Additionally, it calculates the entropy of the password to provide an indication of its randomness.

## Features

- Check if the password contains uppercase letters, lowercase letters, digits, and symbols
- Determine if the password has been involved in any known data breaches
- Calculate the entropy of the password to assess its randomness
- Generate a new secure password

## Installation

1. Clone the repository: `git clone https://github.com/zhensvans/password-checker-app.git`


2. Navigate to the project directory: `cd password-checker-app`


3. Install the required dependencies: `pip install -r requirements.txt`


4. Set the `FLASK_APP` environment variable to `main.py`: `export FLASK_APP=main.py`


5. Optionally, set `FLASK_ENV` to `development` for debug mode: `export FLASK_ENV=development`


6. Run the Flask application using the `flask run` command: `flask run`

## Database Implementation

The application uses SQLite as its database to store breached passwords and their breach counts. The `database.py` module handles database creation, table creation, data insertion, and querying. The database is initialized on application startup and populated with breached password data fetched from an external API.

## Usage

- Enter your password on the main page for analysis.
- Submit the form to view analysis results, including breach status, entropy, and suggestions for password improvement if needed.
- Click "Generate New Password" to create a secure password.

## Contact

For any inquiries or feedback regarding password-checker-app, 
please contact [Zhenya](mailto:zhenya.vardanyan6@gmail.com).


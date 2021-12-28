# Homomorphic-Encryption-and-Its-applications-to-e-voting

# Create Virtual Environment
python3 -m venv venv

# 1. To activate virtual environment

venv\Scripts\activate

# 2. To downlaoad all files in venv (Activate virtual environment first)

python -m pip install -r requirements.txt

# To exit virtual environment

deactivate

# To run the application

set FLASK_APP=application.py
set FLASK_ENV=development
flask run

# To upload to AWS

zip .ebextension, app, application.py, requirements.txt together.

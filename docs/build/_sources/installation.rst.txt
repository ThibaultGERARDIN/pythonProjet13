Installation
============

To install and run the project locally:

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd oc-lettings-site
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root with required environment variables:
   - `SECRET_KEY`
   - `DEBUG`
   - `SENTRY_DSN`
   - `DJANGO_SETTINGS_MODULE`
   - `DJANGO_ALLOWED_HOSTS`

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the server:
   ```
   python manage.py runserver
   ```

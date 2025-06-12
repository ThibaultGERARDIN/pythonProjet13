Testing
=======

Tests use pytest and pytest-django.

To run tests locally:
```
pytest --cov=. --cov-report=term
```

Tests are automatically run on GitHub Actions with minimum 80% coverage threshold.

Tests include:
- Model string representations
- View response status and templates
- Error pages (404 and 500)

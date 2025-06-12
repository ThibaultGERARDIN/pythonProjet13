Deployment
==========

Deployment is handled via Docker and GitHub Actions.

CI/CD Overview:
- Push to `main` triggers tests and container build
- Docker image is pushed to Docker Hub
- Production is hosted on Render using latest Docker image

Manual Deployment:
- Trigger the GitHub Actions deployment job manually or via Render dashboard

Ensure static files are collected:
```
python manage.py collectstatic
```

Render Setup:
- Create new Web Service
- Use Docker image from Docker Hub
- Add environment variables via Render dashboard

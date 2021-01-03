![All Might Smiling](https://i.pinimg.com/originals/23/08/66/230866ae0c37f86aef99a0e8f8d6264f.gif)

# MyCollegeAI - AI based college suggester platform

Students will be able to list of college based on their life decisions (achieved from the psychometric test).

### Technical Stack

- Django
- PostgreSQL [SQLite for Local]
- Redis
- Celery
- AWS [For Deployment]

### Local Setup:

1. Clone the repository
2. Install `direnv` and hook it to your shell for your *nix OS.
3. Copy contents of `.envrc.example` to `.envrc`
   - paste `export DJANGO_SETTINGS_MODULE=settings.local` (others are not mandatory for local)
3. Create a virtual environment using venv
3. `pip install -r requirements.txt` for installing all dependencies
4. `python manage.py collectstatic`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`

To run the project:
1. Clone the repository
```bash
git clone https://github.com/Ripsime-Arutyunyan/UniversityCRM.git
```
2. Switch to branch 'registration'
```bash
git fetch --all
git checkout registration
```
3. Install the requirements
```bash
pip install -r requirements.txt
```
4. Run migration
```bash
python manage.py migrate
```
5. Create super user
```bash
python manage.py createsuperuser
```
6. Run the server
```bash
python manage.py runserver
```


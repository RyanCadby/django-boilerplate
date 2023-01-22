## Getting Started

1. Install and start local postgres server
```
brew install postgresql@13
brew services start postgresql@13
```

2. Clone repo

3. Install correct python version
```
brew install python@3.11
```

3. Start virtual environment with correct python version (inside project directory)
```
virtualenv -p /opt/homebrew/bin/python3.11 venv
```

4. Install packages from requirements.txt
```
pip install -r /path/to/requirements.txt 
```

5. [Install Node](https://nodejs.org/en/download/) globally on your machine

6. install project node modules
```
cd /path/to/project/directory
npm install
```

7. Run dev sass compiler
```
gulp dev
```

8. Connect Django to your Postgres server
    - edit manag.py

8. Run Django server (with venv active)
```
cd /path/to/directory/with/manage.py
python manage.py runserver
```

** you should be up and running now and ready to dev **


## Tools & Requirements
- [Python venv](https://docs.python.org/3/library/venv.html)
- Python 3.11.1
```
brew install python@3.11
```
- Postgres 
```
brew install postgresql@13
```
- [Postico](https://eggerapps.at/postico2/)
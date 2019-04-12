User manual
---

to clone project:
```bash
git clone https://gitlab.com/ssmei/todo-django
```

to configure project:
```bash
cd todo-django
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
```

to start server:
```bash
python3 manage.py runserver
```
then enter the url provided from terminal output to the browser.

**Have fun!**
---
---
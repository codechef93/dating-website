## Together we build a dating website in Python

### Installation 

To run this project on your PC,

Step 1:  **Install Python**. On the [Python](https://www.python.org/) website, click `Downloads` and select `Download for Windows`, then run the downloaded file.


Step 2:  **Install Django**. You may install [Django](https://docs.djangoproject.com/en/3.2/topics/install/#installing-official-release) by command:

    python -m pip install Django

Step 3:  **Download source code** from this repository. 
The easiest way is to click `Code` and then `Download ZIP` at the top-right corner of this page.  Extract the downloaded file and you will get a folder `dating-website-django-master`.

Step 4:  Now you can **run it locally** on your PC/laptop. Using Windows' *Command Prompt* or *PowerShell*,

    cd Downloads\dating-website-django-master
    python manage.py runserver

Step 5:  To enter **main page**, open http://localhost:8000/ using your web browser (eg. Chrome browser or Microsoft Edge).

Step 6:  To reset the admin **password**:

    python manage.py createsuperuser



### Some URLs
* The main page http://localhost:8000/    
* **Member list** http://localhost:8000/user/list/
* **Django Administration** to add/edit/delete users http://localhost:8000/admin/



### About this project
This project is to create a dating website primarily in **Python**, making it **open-source** and sharing the source code on GitHub. We will build this website together with you if you are interested.

Let's join us and contribute your idea, skill, experience, business view, as administrator, as facilitator, as website users etc. Various forms of participation are welcome.

### Technology stack
- Front-end:
    - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - [W3.CSS](https://www.w3schools.com/w3css/default.asp)
    - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - There is **neither** *jQuery* **nor** *Bootstrap*.

- Backend: [Django 3.x](https://www.djangoproject.com/)

- Database: [sqlite3](https://sqlite.org/index.html) (will migrate to [PostgreSQL](https://www.postgresql.org/) later)

# Films

This is the repo of my films' collection website!

It's a Django project that displays my collection of films.

## Table of Contents

- [Information](#information)
- [App Structure](#app-structure)
- [Installation](#installation)
- [Deploy](#deploy)
- [Authors](#authors)

## App Structure

- [static/](film/main/static): The files used by the website (images, documents, css & javascript…)
- [templates/](film/main/templates): The html templates of the pages
- [views.py](film/main/views.py): the code launch when loading a page
- [film/](film/film): the settings files (urls, wsgi, settings) used by Django
- [manage.py](film/manage.py): the main file that runs the website

## Installation

> You need to have python3 and pip installed on your machine

1. Clone git repository

    ```bash
    git clone git@github.com:julsql/film_website.git
    ```

2. Don't forget to add the settings file in `./film/film`

3. Configure the python virtual environment

    ```bash
    pip install virtualenv
    cd film_website
    python3 -m venv env
    source env/bin/activate
    ```
   
4. Install the libraries

    ```bash
    pip install -r requirements.txt
   ```

5. Launch the website

    ```bash
    cd film
    ./manage.py runserver 
    ```
6. To leave the virtual environment
    ```bash
    deactivate
    ```

## Deploy

You need to configure your VM.

Don't forget to download git, python, apache2, pip on your VM:
    
```bash
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install postgresql
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install libapache2-mod-wsgi-py3
sudo apt-get install git
sudo apt-get install python3-venv
```

After installing the project as explained in [Installation](#installation)
you can configure the VM as follows:

```bash
sudo nano /etc/apache2/sites-available/myconfig.conf
```

```
<VirtualHost *:80>
    ServerName film.h.minet.net
    ServerAdmin admin@email.fr

    AddDefaultCharset UTF-8

    Alias /static /home/username/film_website/film/main/static/
    <Directory /home/username/film_website/film/main/static/>
        Require all granted
    </Directory>

    <Directory /home/username/film_website/film/film/>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess film_process python-home=/home/username/film_website/env python-path=/home/username/film_website/film
    WSGIProcessGroup film_process
    WSGIScriptAlias / /home/username/film_website/film/film/wsgi.py process-group=film_process

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

You load the configuration and restart the apache server
```bash
sudo a2ensite myconfig.conf
sudo service apache2 restart
```

> To unload a configuration: `sudo a2dissite myconfig.conf`

## Authors

- Jul SQL
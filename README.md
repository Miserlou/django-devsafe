![django-devsafe](http://i.imgur.com/MhtKl25.gif)

django-devsafe
==============

Safely work with a production database in an insecure environment. Scrambles sensitive user data.

Quick start
-----------

0. Install django-devsafe

    ```python
    pip install django-devsafe
    ```

1. Add "devsafe" to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = (
      ...
      'devsafe',
    )
    ```

2. Invoke devsafe!

    ```bash
    python manage.py devsafe
    ```

Usage
----------

```bash
Usage: manage.py devsafe [options] 

Scrambles your sensitive user data. By default, this just does email addresses and passwords. Omits superusers and staff.

EXAMPLE:

/manage.py devsafe

Options:
  -v VERBOSITY, --verbosity=VERBOSITY
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=all output
  --settings=SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath=PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Print traceback on exception
  --dry                 Dry run, does not actually scramble data. Default
                        False.
  --quiet               Be quiet. Default False.
  --version             show program's version number and exit
  -h, --help            show this help message and exit
```

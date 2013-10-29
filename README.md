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
  --dry                 Dry run, does not actually scramble data. Default
                        False.
  --quiet               Be quiet. Default False.

```

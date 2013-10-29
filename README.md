![django-devsafe](http://i.imgur.com/MhtKl25.gif)

django-devsafe
==============

Safely work with a production database in an insecure environment.

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

![django-devsafe](http://i.imgur.com/MhtKl25.gif)

django-devsafe
==============

Safely work with a production database in an insecure environment. **django-devsafe** scrambles sensitive user data so that you don't accidentally expose the private information of your users during testing.

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

2. Optionally, you can use your settings file to define additional profile fields to scramble. Your User object must
have a **get_profile()** method to access these fields.

    ```python
    DEVSAFE_FIELDS = ['secret_payment_token', 'secret_api_key']
    ```

3. Invoke devsafe!

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

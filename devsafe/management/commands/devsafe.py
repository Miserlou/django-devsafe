from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

from mail_templated import send_mail
from optparse import make_option
import random
import string

class Command(BaseCommand):
    """
    Scrambles your sensitive user data.

    """
    option_list = BaseCommand.option_list + (
         make_option('--dry',
         	action="store_true",
         	dest="dry",
            help='Dry run, does not actually scramble data. Default False.',
            default=False),
         make_option('--quiet',
         	action="store_false",
         	dest="verbose",
            help='Be quiet. Default False.',
            default=True),
    )

    help = '''Scrambles your sensitive user data. By default, this just does email addresses and passwords. Omits superusers and staff.

EXAMPLE:

/manage.py devsafe'''
    def handle(self, **options):
        dry =  bool(options.get('dry'))
        verbose =  bool(options.get('verbose'))

        # Get Users
        users = User.objects.filter(Q(is_staff=False) | Q(is_superuser=False)).order_by('-date_joined')

        for user in users:

            if verbose:
                print "Scrambling " +  str(user.username) + ' (' + str(user.email) + ').'

            if not dry:

                new_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(24))
                new_email = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(12)) + '@' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(24)) + '.com'

                user.set_password(new_password)
                user.email = new_email
                user.save()



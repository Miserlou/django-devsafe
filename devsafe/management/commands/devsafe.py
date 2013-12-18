from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

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

                new_password = randomString(24)
                new_email = randomString(12) + '@' + randomString(12) + '.com'

                user.set_password(new_password)
                user.email = new_email

                if settings.DEVSAFE_FIELDS:
                    profile = user.get_profile()

                    for field in settings.DEVSAFE_FIELDS:
                        try:
                            setattr(profile, field, randomString(12))
                        except Exception, e:
                            print e

                    profile.save()

                user.save()

def randomString(size):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(size))

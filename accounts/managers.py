from django.db import models


class AccountManager(models.Manager):
    """
    Manager class for the Account model. Provides:

    * filtering based on status of accounts
    * account creation
    * account user creation
    """

    def active(self):
        return self.get_query_set().filter(is_active=True)

    def get_by_user(self, user):
        """
        Returns a queryset of Account objects based on a User object, likely
        passed form a request.
        """
        return self.get_query_set().filter(users__user=user)

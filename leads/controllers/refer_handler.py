from leads.models import ReferLead


class ReferHandler:

    @staticmethod
    def refer(phone_number: str = None, email: str = None):
        """Store referred leads to database."""
        try:
            ReferLead.objects.create(
                email=email,
                mobile=phone_number
            )
            return True
        except BaseException:
            return False

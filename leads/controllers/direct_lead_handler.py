from college.models import AppliedCollege, College
from leads.models import DirectLead


class DirectLeadHandler:

    @staticmethod
    def store_from_contact_us(name: str, phone_number: str, email: str, text: str):
        """Record it in the model."""
        try:
            DirectLead.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                text=text,
            )
            return True
        except (AttributeError, ValueError):
            return False


class ApplyCollegeHandler:

    @staticmethod
    def store(profile, college_uuid):
        college = College.objects.get(uuid=college_uuid)
        try:
            AppliedCollege.objects.create(
                profile=profile,
                college=college
            )
            return True, college
        except BaseException:
            AppliedCollege.objects.get(
                profile=profile,
                college=college
            ).delete()
            return False, college

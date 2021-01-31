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

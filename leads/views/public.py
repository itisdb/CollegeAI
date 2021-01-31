"""Public views for leads."""
from django.views.generic.base import View

from leads.controllers.direct_lead_handler import DirectLeadHandler


class ContactUs(View):
    """Handles all contact us form actions."""

    def get(self, request, *args, **kwargs):
        """Load the contact us page."""
        pass

    def post(self, request, *args, **kwargs):
        """Handle the contact us form."""
        name = request.data.get('name')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        text = request.data.get('text')
        extras = request.data

        is_done = DirectLeadHandler().store_from_contact_us()

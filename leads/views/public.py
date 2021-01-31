"""Public views for leads."""
from django.shortcuts import render
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

        is_done = DirectLeadHandler().store_from_contact_us(
            name, phone_number, email, text
        )
        if is_done:
            return render('pages/public/contact.html', {'message': 'You will be contacted soon!'})
        return render('pages/public/contact.html', {'error': 'Failed to save! Please try again.'})

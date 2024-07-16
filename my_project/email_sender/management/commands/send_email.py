from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Send email with screenshot attachment'

    def handle(self, *args, **kwargs):
        base_dir = 'D:\\dya\\itershala\\automategform\\my_project\\email_sender\\management\\commands'
        screenshot_path = os.path.join(base_dir, 'confirmation_page.png')

        if not os.path.exists(screenshot_path):
            self.stderr.write(f"Error: File not found: {screenshot_path}")
            return

        email = EmailMessage(
            'Subject Here',
            'Body Here',
            'vidyaadgar97@gmail.com',  # Use the same email address as EMAIL_HOST_USER
            
        )

        email.attach_file(screenshot_path)

        try:
            email.send()
            self.stdout.write(self.style.SUCCESS('Email sent successfully'))
        except Exception as e:
            self.stderr.write(f"Error sending email: {e}")

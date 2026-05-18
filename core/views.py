from django.shortcuts import render
from django.core.mail import send_mail

def landing_page(request):
    return render(request, 'landing.html')

def about_page(request):
    return render(request, 'about.html')

def team_page(request):
    return render(request, 'team.html')

def nexax_page(request):
    return render(request, 'nexax.html')

def nexaschool_page(request):
    return render(request, 'nexaschool.html')

def ai_service_page(request):
    return render(request, 'service_ai.html')

def app_development_page(request):
    return render(request, 'service_app_dev.html')

def web_development_page(request):
    return render(request, 'service_web_dev.html')

def contact_page(request):
    # Check if the user submitted the contact form
    if request.method == "POST":
        # 1. Grab the data from the HTML form using the name="..." attributes
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        user_email = request.POST.get('email', '')
        subject_line = request.POST.get('subject', '')
        message_body = request.POST.get('message', '')

        # 2. Format how the email will look when it arrives in your inbox
        full_message = f"""
New Contact Form Submission from Revah Tech Website!

From: {first_name} {last_name}
Email: {user_email}

Subject: {subject_line}

Message:
{message_body}
"""
        # 3. Send the email securely via Django
        try:
            send_mail(
                subject=f"Website Contact: {subject_line}",
                message=full_message,
                from_email=None, # Uses the default email host from settings.py
                recipient_list=['revah.tech.official@gmail.com'], 
                fail_silently=False,
            )
            # 4. Reload the page and trigger the green success message
            return render(request, 'contact.html', {'email_success': True})
            
        except Exception as e:
            # If the email fails (e.g., wrong password in settings), print the error to your console
            print(f"Email failed to send: {e}")

    # If they just navigated to the page normally, show the empty form
    return render(request, 'contact.html')
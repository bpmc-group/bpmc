from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.models import User
import csv
from django.http import HttpResponse

@login_required
def reporting_landing(request):
    return render(request, 'reporting/landing.html')


def export_users_csv(request):
    # Create the HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_report.csv"'

    # Create the CSV writer
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'First Name', 'Last Name', 'Full Name', 'Email', 'Hire Date',
        'Employment Status', 'Username', 'Department', 'Phone Numbers',
        'Pay Rule', 'Hourly Rate', 'Badge Number', 'Is Active'
    ])

    # Write user data rows
    for user in User.objects.all():
        writer.writerow([
            user.id, user.first_name, user.last_name, user.employee_full_name,
            user.email, user.hire_date, user.employment_status, user.username,
            user.department_description,
            f"{user.phone_number_1 or ''} {user.phone_number_2 or ''} {user.phone_number_3 or ''}",
            user.pay_rule, user.hourly_wage_rate, user.badge_number,
            'Yes' if user.is_active else 'No'
        ])

    return response
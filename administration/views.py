from django.shortcuts import render, redirect
from api.models import AccessProfile, Permission
from administration.forms import AccessProfileForm, PermissionFormSet
from django.shortcuts import render, redirect, get_object_or_404
from api.models import AccessProfile, User
from django.contrib import messages
from .forms import AccessProfileForm
from functools import wraps
from api.models import Permission
import logging

logger = logging.getLogger(__name__)


def admin_home(request):
    return render(request, 'administration/home.html')

def user_management(request):
    return render(request, 'administration/user_management.html')

def add_user(request):
    return render(request, 'administration/add_user.html')

def function_access_profiles(request):
    return render(request, 'administration/function_access_profiles.html')

FUNCTIONS = {
    'Administration': 'administration.views.admin_home',          # Maps to admin_home view
    'User Management': 'administration.views.user_management',    # Maps to user_management view
    'Add User': 'administration.views.add_user',                  # Maps to add_user view
    'Function Access Profiles': 'administration.views.function_access_profiles',  # Maps to function_access_profiles view
    'Create Access Profile': 'administration.views.create_access_profile',        # Maps to create_access_profile view
    'Edit Access Profile': 'administration.views.edit_access_profile',            # Maps to edit_access_profile view
    'Assign Profiles to Users': 'administration.views.assign_profile_to_user',    # Maps to assign_profile_to_user view

    # Manage Timecards
    'Manage Timecards': 'manage_timecards.views.home',            # Maps to the home view in manage_timecards app

    # Punch Management
    'Punch Management': 'punch.views.punch_landing',             # Maps to punch_landing view

    # Reporting
    'Reporting Landing': 'reporting.views.reporting_landing',     # Maps to reporting_landing view
    'Export Users CSV': 'reporting.views.export_users_csv',        # Maps to export_users_csv view

    # Schedule Management
    'Manage Schedules': 'manage_schedules.views.schedule_home',   # Maps to schedule_home view

    # View Schedules
    'View Schedules': 'view_schedule.views.view_schedule',        # Maps to view_schedule view
    'Get Schedule': 'view_schedule.views.get_schedule',           # Maps to get_schedule view (API)

    # View Timecards
    'View Timecards': 'view_timecard.views.view_timecard',         # Maps to view_timecard view
    'Get Timecards': 'view_timecard.views.get_timecard',           # Maps to get_timecard view (API)
}

def create_access_profile(request):
    if request.method == "POST":
        profile_form = AccessProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save()

            # Process permissions from the form data
            for function_name in FUNCTIONS:
                can_view = request.POST.get(f"{function_name}_can_view", False)

                Permission.objects.create(
                    access_profile=profile,
                    function_name=function_name,
                    can_view=bool(can_view),
                )
            return redirect("function_access_profiles")  # Redirect to access profiles list
    else:
        profile_form = AccessProfileForm()

    return render(
        request,
        "administration/create_access_profile.html",
        {"profile_form": profile_form, "functions": FUNCTIONS},
    )


def edit_access_profile(request):
    profiles = AccessProfile.objects.all()
    selected_profile = None
    permissions = None

    if request.method == "POST":
        profile_id = request.POST.get("profile")
        if profile_id:
            selected_profile = get_object_or_404(AccessProfile, id=profile_id)
            profile_form = AccessProfileForm(request.POST, instance=selected_profile)
            permission_formset = PermissionFormSet(request.POST, queryset=selected_profile.permissions.all())

            if profile_form.is_valid() and permission_formset.is_valid():
                profile_form.save()
                permission_formset.save()  # Save changes to the permissions
                return redirect("function_access_profiles")
        else:
            profile_form = AccessProfileForm()
            permission_formset = PermissionFormSet(queryset=Permission.objects.none())
    else:
        profile_id = request.GET.get("profile")
        if profile_id:
            selected_profile = get_object_or_404(AccessProfile, id=profile_id)
            profile_form = AccessProfileForm(instance=selected_profile)
            permission_formset = PermissionFormSet(queryset=selected_profile.permissions.all())
        else:
            profile_form = AccessProfileForm()
            permission_formset = PermissionFormSet(queryset=Permission.objects.none())

    return render(
        request,
        "administration/edit_access_profile.html",
        {
            "profiles": profiles,
            "selected_profile": selected_profile,
            "profile_form": profile_form,
            "permission_formset": permission_formset,
        },
    )


def assign_profile_to_user(request):
    from api.models import AccessProfile  # Import inside the function to avoid circular imports
    users = User.objects.all()
    profiles = AccessProfile.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user")
        profile_id = request.POST.get("profile")

        try:
            # Debugging Logs
            print(f"User ID from POST: {user_id}")
            print(f"Profile ID from POST: {profile_id}")

            user = User.objects.get(id=user_id)
            profile = AccessProfile.objects.get(id=profile_id)

            # Log the fetched objects
            print(f"Fetched User: {user}")
            print(f"Fetched Profile: {profile}")

            # Add the profile to the user's access profiles
            user.access_profiles.add(profile)
            user.save()

            # Success message to display to users
            messages.success(request, "Profile assigned successfully!")

        except AccessProfile.DoesNotExist:
            # Log the error and provide feedback to the user
            messages.error(request, "The selected profile does not exist.")
        except User.DoesNotExist:
            # Log the error and provide feedback to the user
            messages.error(request, "The selected user does not exist.")
        except Exception as e:
            # Log unexpected errors and notify the user
            print(f"Unexpected Error: {e}")
            messages.error(request, "An unexpected error occurred. Please try again.")

        return redirect("assign_profiles_to_user")  # Redirect to the same page or confirmation

    return render(request, "administration/assign_profiles_to_user.html", {
        "users": users,
        "profiles": profiles,
    })

def permission_required(function_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Get the user's access profiles
            user_profiles = request.user.access_profiles.all()
            logger.debug(f"User Profiles: {user_profiles}")

            # Check if the user has the required permission
            permissions = Permission.objects.filter(
                access_profile__in=user_profiles,
                function_name=function_name,
                can_view=True
            )
            logger.debug(f"Permissions for {function_name}: {permissions}")

            if permissions.exists():
                return view_func(request, *args, **kwargs)

            logger.warning(f"Access denied for user {request.user} to {function_name}")
            return redirect("permission_denied")
        return _wrapped_view
    return decorator


def permission_denied(request):
    return render(request, 'administration/permission_denied.html', status=403)





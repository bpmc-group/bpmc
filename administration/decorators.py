from functools import wraps
from django.shortcuts import redirect
from api.models import Permission
import logging

logger = logging.getLogger(__name__)

def permission_required(function_name):
    """
    Decorator to check if a user has the required permission for a specific function.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            logger.info(f"Checking permissions for user {request.user} on function {function_name}")

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
                logger.info(f"Permission granted for user {request.user} on {function_name}")
                return view_func(request, *args, **kwargs)

            logger.warning(f"Access denied for user {request.user} on {function_name}")
            return redirect("permission_denied")  # Redirect unauthorized users
        return _wrapped_view
    return decorator

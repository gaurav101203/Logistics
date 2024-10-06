#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Role_based_login_system.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Check if 'runserver' is in the command arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        # Dynamically bind to PORT if defined as an environment variable
        port = os.environ.get('PORT', '8000')
        sys.argv[2:] = ['0.0.0.0:' + port]  # Set host:port to '0.0.0.0:PORT'

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

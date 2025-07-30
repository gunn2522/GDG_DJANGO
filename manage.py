#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # --- FORCE THE CORRECT DATABASE URL ---
    # PASTE YOUR NEW NEON URL BETWEEN THE QUOTES
    os.environ['DATABASE_URL'] = "postgresql://neondb_owner:npg_AQiqbmwG9Ij0@ep-shy-hill-adidebm8-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    # ------------------------------------

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDG_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
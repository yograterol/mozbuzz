#!/usr/bin/env python
from django.core.management import execute_manager


try:
    import settings
except ImportError:
    import sys
    sys.stderr.write(
        "Error: Tried importing 'settings_local.py' and 'settings.py' "
        "but neither could be found (or they're throwing an ImportError)."
        " Please come back and try again later.")
    raise


if __name__ == "__main__":
    execute_manager(settings)

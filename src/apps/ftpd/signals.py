"""FTPd custom signals."""

import django.dispatch


motion_detected = django.dispatch.Signal(providing_args=['username', 'filename'])

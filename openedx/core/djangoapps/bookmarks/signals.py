"""
Signals for bookmarks.
"""
from django.dispatch.dispatcher import receiver

from xmodule.modulestore.django import SignalHandler


@receiver(SignalHandler.course_published)
def trigger_update_xblocks_cache_task(sender, course_key, **kwargs):  # pylint: disable=invalid-name,unused-argument
    """
    Trigger update_xblocks_cache() when course_published signal is fired.
    """
    from .. import bookmarks  # Importing tasks too early causes issues in tests.

    # Note: The countdown=0 kwarg is set to ensure the method below does not attempt to access the course
    # before the signal emitter has finished all operations. This is also necessary to ensure all tests pass.
    bookmarks.tasks.update_xblocks_cache.apply_async([unicode(course_key)], countdown=0)

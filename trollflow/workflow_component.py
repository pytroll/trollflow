import abc
from threading import Lock, ThreadError


class AbstractWorkflowComponent(object):
    __metaclass__ = abc.ABCMeta

    # @abc.abstractproperty
    slots = []

    def __init__(self):
        self.use_lock = False
        self.prev_lock = None
        self.lock = Lock()

    def release_lock(self):
        """Release the lock of the previous step."""
        if self.prev_lock is not None:
            try:
                self.prev_lock.release()
            except ThreadError:
                pass

    def acquire_lock(self):
        """Acquire lock and wait for its release"""
        if self.lock is not None:
            self.lock.acquire(True)

    @abc.abstractmethod
    def pre_invoke(self):
        """Execute block before invoking component."""
        return

    @abc.abstractmethod
    def invoke(self, context):
        """Execute the actual component."""
        return

    @abc.abstractmethod
    def post_invoke(self):
        """Execute block after invoking component."""
        return

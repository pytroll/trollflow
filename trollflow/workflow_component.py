import abc
from threading import Lock


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
            self.prev_lock.release()

    def aqcuire_lock(self):
        """Acquire lock and wait for its release"""
        if self.own_lock is not None:
            self.own_lock.acquire(block=True)

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

# renderlab/utils/factories.py

from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractFileSystem
from .services import OSFileSystem

class FileSystemFactory(AbstractFactory):
    """Factory for creating file system interfaces."""
    
    def create(self, **kwargs) -> AbstractFileSystem:
        """Returns the standard OS file system wrapper."""
        return OSFileSystem()
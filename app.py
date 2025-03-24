import sys
from typing import TextIO

from config import DatabaseConfig
from repository import *
from service import *
from factories import *
from ui import ConsoleUI


class CloudShopApp:
    
    def __init__(self):
        self.db_config = DatabaseConfig()
        
        self.repository_factory = RepositoryFactory()
        self.user_repository = self.repository_factory.create_user_repository(self.db_config.db_type, file_path=self.db_config.get_user_db_path())
        self.listing_repository = self.repository_factory.create_listing_repository(self.db_config.db_type, file_path=self.db_config.get_listing_db_path())
        self.category_repository = self.repository_factory.create_category_repository(self.db_config.db_type, self.listing_repository, file_path=self.db_config.get_category_db_path())
        
        # Initialize services
        self.user_service = UserService(self.user_repository)
        self.listing_service = ListingService(self.listing_repository, self.category_repository, self.user_service)
        
        # Initialize command factory
        self.command_factory = CommandFactory(self.user_service, self.listing_service)
        
        # Initialize UI
        self.ui = ConsoleUI(self.command_factory)
    
    def run(self, input_stream: TextIO = sys.stdin, output_stream: TextIO = sys.stdout):
        self.ui.run(input_stream, output_stream)
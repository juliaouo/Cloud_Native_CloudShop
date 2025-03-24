from repository import *


class RepositoryFactory:
    """Factory for creating repositories based on storage type."""
    @staticmethod
    def create_user_repository(repo_type: str, **kwargs) -> UserRepository:
        """Create a user repository."""
        if repo_type == RepositoryType.MEMORY:
            return MemoryUserRepository()
        elif repo_type == RepositoryType.FILE:
            file_path = kwargs.get("file_path", "users.json")
            return FileUserRepository(file_path)
        else:
            raise ValueError(f"Unknown repository type: {repo_type}")
    
    @staticmethod
    def create_listing_repository(repo_type: str, **kwargs) -> ListingRepository:
        """Create a listing repository."""
        if repo_type == RepositoryType.MEMORY:
            return MemoryListingRepository()
        elif repo_type == RepositoryType.FILE:
            file_path = kwargs.get("file_path", "listings.json")
            return FileListingRepository(file_path)
        else:
            raise ValueError(f"Unknown repository type: {repo_type}")
    
    @staticmethod
    def create_category_repository(repo_type: str, listing_repository: ListingRepository, **kwargs) -> CategoryRepository:
        """Create a category repository."""
        if repo_type == RepositoryType.MEMORY:
            return MemoryCategoryRepository(listing_repository)
        elif repo_type == RepositoryType.FILE:
            file_path = kwargs.get("file_path", "categories.json")
            return FileCategoryRepository(listing_repository, file_path)
        else:
            raise ValueError(f"Unknown repository type: {repo_type}")

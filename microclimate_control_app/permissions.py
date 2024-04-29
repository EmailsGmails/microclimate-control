from rest_framework.permissions import BasePermission

APP_NAME = 'microclimate_control_app'

class CanAccessProject(BasePermission):
    """
    Permission class to check if a user has access to a project.
    """

    def has_permission(self, request, view):
        """
        Check if the user has permission to access the project.

        Args:
            request (HttpRequest): The HTTP request object.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in ['GET']:
            project_id = view.kwargs.get('project_pk', '')
            return request.user.has_perm(f'{APP_NAME}.can_access_project_{project_id}')
        else:
            return True

class CanUpdateProject(BasePermission):
    """
    Permission class to check if a user has permission to update a project.

    This permission class checks if the requesting user has the necessary permissions
    to update a project based on the project ID in the URL.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to update the project.

        Args:
            request: The incoming HTTP request.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in ['PUT', 'PATCH']:
            project_id = view.kwargs['pk']
            return request.user.has_perm(f'{APP_NAME}.can_update_project_{project_id}')
        else:
            return True

class CanAccessBuildingObject(BasePermission):
    """
    Permission class to check if a user has permission to access a building object.

    This permission class checks if the requesting user has the necessary permissions
    to access a building object based on the project and building IDs in the URL.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to access the building object.

        Args:
            request: The incoming HTTP request.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in ['GET']:
            project_id, building_id = view.kwargs.get('project_pk', ''), view.kwargs.get('pk', '')
            return request.user.has_perm(f'{APP_NAME}.can_access_project_{project_id}_building_{building_id}')
        else:
            return True

class CanCreateBuildingObject(BasePermission):
    """
    Permission class to check if a user has permission to create a building object.

    This permission class checks if the requesting user has the necessary permissions
    to create a building object based on the project ID in the URL.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to create a building object.

        Args:
            request: The incoming HTTP request.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method == 'POST':
            project_id = view.kwargs['project_pk']
            if project_id:
                return request.user.has_perm(f'{APP_NAME}.can_create_buildings_project_{project_id}')
            else:
                return False
        else:
            return True

class CanUpdateBuildingObject(BasePermission):
    """
    Permission class to check if a user has permission to update a building object.

    This permission class checks if the requesting user has the necessary permissions
    to update a building object based on the project ID in the URL.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to update a building object.

        Args:
            request: The incoming HTTP request.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in ['PUT', 'PATCH']:
            project_id = view.kwargs['project_pk']
            if project_id:
                return request.user.has_perm(f'{APP_NAME}.can_update_buildings_project_{project_id}')
            else:
                return False
        else:
            return True

class CanDeleteBuildingObject(BasePermission):
    """
    Permission class to check if a user has permission to delete a building object.

    This permission class checks if the requesting user has the necessary permissions
    to delete a building object based on the project ID in the URL.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to delete a building object.

        Args:
            request: The incoming HTTP request.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method == 'DELETE':
            project_id = view.kwargs['project_pk']
            if project_id:
                return request.user.has_perm(f'{APP_NAME}.can_delete_buildings_project_{project_id}')
            else:
                return False
        else:
            return True

class CanAccessBuildingContent(BasePermission):
    """
    Permission class to check if a user has permission to access building content.

    This permission class checks if the requesting user has the necessary permissions
    to access building content based on the project and building IDs in the URL.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to access building content.

        Args:
            request: The incoming HTTP request.
            view: The view associated with the request.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        user = request.user

        project_id, building_id = view.kwargs['project_pk'], view.kwargs['object_pk']
        if user.has_perm(f'{APP_NAME}.can_access_project_{project_id}') or \
           user.has_perm(f'{APP_NAME}.can_access_project_{project_id}_building_{building_id}'):
            return True

        return False

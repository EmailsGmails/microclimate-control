from rest_framework.permissions import BasePermission

APP_NAME = 'microclimate_control_app'

class CanAccessProject(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            project_id = view.kwargs.get('project_pk', '')
            return request.user.has_perm(f'{APP_NAME}.can_access_project_{project_id}')
        else:
            return True

class CanUpdateProject(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            project_id = view.kwargs['pk']
            return request.user.has_perm(f'{APP_NAME}.can_update_project_{project_id}')
        else:
            return True

class CanAccessBuildingObject(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            project_id, building_id = view.kwargs.get('project_pk', ''), view.kwargs.get('pk', '')
            return request.user.has_perm(f'{APP_NAME}.can_access_project_{project_id}_building_{building_id}')
        else:
            return True

class CanCreateBuildingObject(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            project_id = view.kwargs['project_pk']
            if project_id:
                return request.user.has_perm(f'{APP_NAME}.can_create_buildings_project_{project_id}')
            else:
                return False
        else:
            return True

class CanUpdateBuildingObject(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            project_id = view.kwargs['project_pk']
            if project_id:
                return request.user.has_perm(f'{APP_NAME}.can_update_buildings_project_{project_id}')
            else:
                return False
        else:
            return True

class CanDeleteBuildingObject(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            project_id = view.kwargs['project_pk']
            if project_id:
                return request.user.has_perm(f'{APP_NAME}.can_delete_buildings_project_{project_id}')
            else:
                return False
        else:
            return True

class CanAccessBuildingContent(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        project_id, building_id = view.kwargs['project_pk'], view.kwargs['object_pk']
        if user.has_perm(f'{APP_NAME}.can_access_project_{project_id}') or \
           user.has_perm(f'{APP_NAME}.can_access_project_{project_id}_building_{building_id}'):
            return True

        return False

class PostsPermission:
    def has_permission(self, request, view):

        if view.action == "list":
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj

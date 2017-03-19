class PostsPermission:
    def has_permission(self, request, view):

        if view.action in ("list", "retrieve"):
            return True

        if view.action == "create":
            return request.user.is_authenticated

        if view.action == "destroy":
            return True


        return False

    def has_object_permission(self, request, view, obj):
        # para ver el detalle de un objeto, si está publicado todos tienen permiso
        if request.method == 'GET' and obj.publish_at != None:
            return True
        else:
            return request.user.is_superuser or request.user == obj.owner
from rest_framework import mixins, viewsets

class CommentMixin(mixins.CreateModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    pass
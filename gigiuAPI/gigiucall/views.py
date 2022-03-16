from gigiucall.serializers import CallRegisterSerializer
from rest_framework import mixins
from rest_framework import generics

from gigiucall.models import CallRegister

# Create your views here.


class CallRegisterList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all registered calls, or register new calls
    """
    queryset = CallRegister.objects.all()
    serializer_class = CallRegisterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CallRegisterDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    """
    Retrieve, update or delete a call instance
    """
    queryset = CallRegister.objects.all()
    serializer_class = CallRegisterSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, *kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)


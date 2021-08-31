from .serializers import create_marhsmellow_instance
from . import create_app

marshmallow = create_marhsmellow_instance(create_app);

class TodoSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'title', 'description')
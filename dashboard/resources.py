from import_export import resources

from dashboard.models import Constructor


class ConstructorResource(resources.ModelResource):
    class Meta:
        model = Constructor


class AnotherConstructorResource(resources.ModelResource):
    class Meta:
        model = Constructor

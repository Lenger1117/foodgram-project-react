from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from recipes.models import (Ingredient, Recipe, Tag)

from .filters import IngredientFilter
from .pagination import Pagination
from .permissions import AuthorOrReadOnly
from .serializers import (CreateRecipeSerializer,
                          IngredientSerializer,
                          TagSerializer, RecipeSerializer)


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (IngredientFilter, )
    search_fields = ('^name', )
    pagination_class = None


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnly, ]
    pagination_class = Pagination
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    # filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeSerializer
        return CreateRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

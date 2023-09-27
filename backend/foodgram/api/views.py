from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics, ttfonts
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from recipes.models import (Ingredient,
                            Recipe,
                            Tag,
                            ShoppingCart,
                            Favorite,
                            IngredientRecipe)
from .filters import IngredientFilter, RecipeFilter
from .pagination import Pagination
from .permissions import AuthorOrReadOnly
from .serializers import (CreateRecipeSerializer,
                          IngredientSerializer,
                          TagSerializer,
                          ReadRecipeSerializer,
                          ShoppingCartSerializer,
                          FavoriteSerializer)


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
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadRecipeSerializer
        return CreateRecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    @action(detail=False, methods=['GET'],
            permission_classes=[IsAuthenticated],
            url_path='download_shopping_cart',)
    def download_shopping_cart(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = (
            "attachment; filename='shopping_cart.pdf'"
        )
        p = canvas.Canvas(response)
        comfortaa_bold = ttfonts.TTFont('Comfortaa-Bold',
                                        'data/Comfortaa-Bold.ttf')
        pdfmetrics.registerFont(comfortaa_bold)
        p.setFont('Comfortaa-Bold', 14)

        ingredients = IngredientRecipe.objects.filter(
            recipe__shopping_cart__user=request.user).values_list(
            'ingredient__name', 'amount', 'ingredient__measurement_unit')

        ingredient_list = {}
        for name, amount, unit in ingredients:
            if name not in ingredient_list:
                ingredient_list[name] = {'amount': amount, 'unit': unit}
            else:
                ingredient_list[name]['amount'] += amount
        height = 700

        p.drawString(100, 750, 'Список покупок:')
        for ingredient, (name, data) in enumerate(ingredient_list.items(),
                                                  start=1):
            p.drawString(
                80, height,
                f"{ingredient}. {name} – {data['amount']} {data['unit']}")
            height -= 25
        p.showPage()
        p.save()
        return response


class ShoppingCartView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        data = {
            'user': request.user.id,
            'recipe': recipe.id
        }
        serializer = ShoppingCartSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        if ShoppingCart.objects.filter(
           user=request.user, recipe=recipe).exists():
            ShoppingCart.objects.filter(
                user=request.user, recipe=recipe
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]
    pagination_class = Pagination

    def post(self, request, id):
        data = {
            'user': request.user.id,
            'recipe': id
        }
        if not Favorite.objects.filter(
           user=request.user, recipe__id=id).exists():
            serializer = FavoriteSerializer(
                data=data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        if Favorite.objects.filter(
           user=request.user, recipe=recipe).exists():
            Favorite.objects.filter(user=request.user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

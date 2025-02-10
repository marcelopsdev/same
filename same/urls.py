from django.urls import path
from apps.same.views import SamaList, SamaCreate, SamaUpdate, SameDetailView


urlpatterns = [
    path("same/", SamaList.as_view(), name="same"),
    path("cadastrar_same/", SamaCreate.as_view(), name="cadastrar_same"),
    path("editar_same/<int:pk>/", SamaUpdate.as_view(), name="editar_same"),
    path("imprimir_same/<int:pk>/", SameDetailView.as_view(), name="imprimir_same"),
]

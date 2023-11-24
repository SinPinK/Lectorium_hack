from django.urls import path
from .views import (
    TranscriptionAudio
)

urlpatterns = [
    path('test/', TranscriptionAudio.as_view()),
]
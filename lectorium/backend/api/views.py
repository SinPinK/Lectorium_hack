import json
import requests
import whisper
from rest_framework.views import APIView
from rest_framework.response import Response

class Test(APIView):
    def get(self, request, *args, **kwargs):
        test = 'Go Hack with back!'
        resp = test
        return Response(json.dumps(resp))


class TestW():
    def start(self):
        model = whisper.load_model("base")
        print("***")


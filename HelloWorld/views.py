from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app <br> HelloWorld !</h1>"""

   return HttpResponse(text)

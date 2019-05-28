from django.http import HttpResponse

def hello(request):
   print("hello")
   print("HII")
   print("welcome to hello world")
   import cx_Oracle
   conn = cx_Oracle.connect(user=r'User Name', password='Personal Password')
   c = conn.cursor()
   text = """<h1>welcome to my app <br> HelloWorld !</h1>"""
   print("No HII")

   return HttpResponse(text)

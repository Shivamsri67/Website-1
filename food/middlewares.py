from django.shortcuts import redirect
from django.http import HttpResponse

## Function Based Middleware

# def my_middleware(get_response):
#     print("One time Initialisation")

#     def my_function(request):
#         full_url = request.get_full_path()
#         print("Full url",full_url)
    
#     # Get the URL path without the domain and query parameters
#         path = request.path
#         print("path",path)
#          # Get the scheme (http or https) and domain
#         scheme = request.scheme
#         print("scheme",scheme)
#         host = request.get_host()
#         print("host",host)
    
#         print("Before view")

#         # if request.path=='/food/index/':
#         #     return redirect('food:home')
        

#         response=get_response(request)
#         if response.status_code==404:                    ## exception handling in fbv is done through status code
#             return HttpResponse("This is an incorrect URL")

    

        
#         print(response.charset)
#         print(response)
#         # print(response.content)
#         print('After View')
#         return response
#     return my_function

## Class Based Middleware

class my_middleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("logic before view")
        print(request.path)
        print(request.method)
        response=self.get_response(request)
        
        print(response.status_code)
        print("logic after view")
        if response.status_code==404:
            return HttpResponse("<h1>RAJ</h1>")
        return response
    
    def process_view(request,*args,**kwargs):
        return None
    
    def process_exception(self,request,exception):
        return None
    
    def process_template_response(self,request,response):
        response.context_data['key']='value'
        return response









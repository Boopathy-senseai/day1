from django.http import JsonResponse

def hai(request):
    data = {
        "Name":"Boopathy",
      
    }
    return JsonResponse(data)

from django.http import JsonResponse

def hai(request):
    data = {
        "Name":"Boopathy",
        "love":"i love panda br"
    }
    return JsonResponse(data)

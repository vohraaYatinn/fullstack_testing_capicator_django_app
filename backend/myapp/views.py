from django.http import JsonResponse

def test_api(request):
    data = {'message': 'This is a test API'}
    return JsonResponse(data)

def check_ip_origin(request):
    client_ip = request.META.get('REMOTE_ADDR')
    return JsonResponse({'origin_ip': client_ip})
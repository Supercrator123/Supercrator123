from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        url = request.GET.get('https://www.bible.com/bible/111/GEN.INTRO1.NIV')
        if url:
            try:
                response = requests.get(url)
                # Optionally process the response here
                return JsonResponse(response.json())  # or return response.content for non-JSON data
            except requests.RequestException as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'URL parameter missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are supported'}, status=405)

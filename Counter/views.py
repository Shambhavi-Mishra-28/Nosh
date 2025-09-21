from django.shortcuts import render

# DGYJoI/uemZUK85G8iWv7w==PYmFA3zF3ZJLtcWf
# Create your views here.
def home(request):
    import json
    import requests

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers= {'X-Api-Key': 'DGYJoI/uemZUK85G8iWv7w==PYmFA3zF3ZJLtcWf'})

        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Oops, something went wrong"
            print(e)
        
        return render(request, 'home.html', {'api': api})
        
    else :
        return render(request, 'home.html', {'query': 'Enter a valid query'})



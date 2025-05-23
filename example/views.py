# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Python and Django hosted at Vercel</h1>
            <p>The current time is { now }.</p>
            <p>Note: The Administration part of this Demo is NOT configurated for this Starter</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
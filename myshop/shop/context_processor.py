from datetime import datetime

def time(request):
    return {'time': datetime.now()}
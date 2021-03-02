from datetime import datetime

def time(request):
    return {'time': datetime.now().strftime("%d/%m/%Y  %H:%M:%S")}
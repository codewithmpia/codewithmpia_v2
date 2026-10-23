from asok import Request

def render(request: Request):
    return request.html('page.html')

from django.shortcuts import render

from serihu.models import Serihu


def index(request):
    """topページを表示する

    SerihuDBからランダムで1つserihuを取得し、serihu/index.htmlにレンダリングする。

    Arguments
    ---------
    request: django.http.request.HttpRequest
        リクエストの内容

    Returns
    -------
    response: django.http.response.HttpResponse
        レスポンスの内容
    """
    serihu = Serihu.objects.random()
    context = {'serihu': serihu}
    return render(request, 'serihu/index.html', context=context)


if __name__ == '__main__':
    import time
    print(time.timezone)

from django.http import JsonResponse

from genres.models import Genre


def genre_view(request):
    genres = Genre.objects.all()
    data = [{"id": genre.id, "name": genre.name} for genre in genres]
    print(data)
    return JsonResponse(data, safe=False)

    # resp = JsonResponse(list(genres.values()), safe=False)
    # print(resp.content)
    # return resp

    # return JsonResponse({"genres": list(genres.values())})

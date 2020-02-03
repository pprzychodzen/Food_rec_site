from django.http import HttpResponse
from django.shortcuts import render

from .models import Tutorial, TutorialCategory, TutorialSeries


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest(
                "tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request,
                      "main/category.html",
                      {"part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(
            tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request=request,
                      template_name='main/tutorial.html',
                      context={"tutorial": this_tutorial,
                               "sidebar": tutorials_from_series,
                               "this_tut_idx": this_tutorial_idx})

    return HttpResponse(f"{single_slug} does not correspond to anything. yolo.")


def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": TutorialCategory.objects.all})

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "This is january page.",
    "february": "This is february page." ,
    "march": "This is march page." ,
    "april": "This is april page." ,
    "may": "This is may page." ,
    "june": "This is june page." ,
    "july": "This is july page." ,
    "august": "This is august page." ,
    "september": "This is september page." ,
    "october": "This is october page." ,
    "november": "This is november page." ,
    "december": None 
}
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number (request, month):
    try:
        challenge_list = list(monthly_challenges.keys())
        month_direct = challenge_list [month - 1]
        redirect_path = reverse("monthly_challenge", args=[month_direct])
        return HttpResponseRedirect (redirect_path)
    except:
        return HttpResponse ("This month is not supported")

def monthly_challenge (request, month):
    try:
        challenge_text = monthly_challenges.get(month)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
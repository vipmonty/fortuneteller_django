from django.shortcuts import render
import random
# Create your views here.

fortuneList = [
    'Struggles are on the horizon, but you were build for it.',
    'Great things are coming, if you hustle hard.',
    'Your cup may runnth over, but you WILL persist.',
    'The story will be as beautifull beyond what you can fathom.',
    'You are amist the grand journey, enjoy it.'
]


def fortune(request):

    fortunes = random.choice(fortuneList)
    context = {
        "fortunes": fortunes
    }

    return render(request, "randomfortune/fortune.html", context)

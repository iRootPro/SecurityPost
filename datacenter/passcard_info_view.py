from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import is_visit_long
from datacenter.models import format_duration

def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    visits  = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        entered_at = visit.entered_at
        leaved_at = visit.leaved_at
        duration = leaved_at - entered_at
        flag = is_visit_long(duration)
        this_passcard_visits.append(
            {
                "entered_at": entered_at,
                "duration": format_duration(duration),
                "is_strange": flag
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.models import get_duration
from datacenter.models import format_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        who_entered = visit.passcard.owner_name
        entered_at = visit.entered_at
        duration = format_duration(get_duration(entered_at))
        non_closed_visits.append(
            {
                "who_entered": who_entered,
                "entered_at": entered_at,
                "duration": duration
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
        }
    return render(request, 'storage_information.html', context)

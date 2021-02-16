from celery import shared_task, current_app
from bs4 import BeautifulSoup as bs4
from events.models import Event, SourceArchive

import urllib.request


@shared_task(bind=True)
def download_sources(self):

    sources = [{
        "name": "Majority Leader",
        "url": "https://www.majorityleader.gov/calendar/ical",
        "type": "ical"
    }, {
        "name": "OPM Holidays",
        "url": "https://www.opm.gov/about-us/open-government/Data/Apps/Holidays/ical.aspx",
        "type": "ical"
    }, {
        "name": "Senate Floor Schedule",
        "url": "https://www.senate.gov/legislative/schedule/floor_schedule.xml",
        "type": "xml_senate_floor"
    }]

    for source in sources:
        download_source(source)

    return


@shared_task(bind=True)
def download_source(source):
    currentSourceArchive = SourceArchive.objects.create(
        source=source.name, url=source.url, type=source.type, status=SourceArchive.DOWNLOADING)

    try:
        with urllib.request.urlopen(source.url) as f:
            currentSourceArchive.content = f.read().decode('utf-8')
        currentSourceArchive.status=SourceArchive.PROCESSING
        currentSourceArchive.save(update_fields=['content', 'status'])
    except Exception as e:
        currentSourceArchive.status=SourceArchive.FAILED
        currentSourceArchive.save(update_fields=['status'])

    return



@shared_task(bind=True)
def process_sources(self):

    # for each content type found in source download archive

    # delete all existing entries for source.
    # We should consider synchronizing events if we start storing additional metadata in our DB
    # Event.objects.filter(source=source.name).delete()

    # call parser for each content and add events to DB

    return

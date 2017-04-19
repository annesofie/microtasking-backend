import csv
from survey_results.models import Taskresult


def dump(qs, outfile_path):
    """
    Takes in a Django queryset and spits out a CSV file.

    Usage::

        >> from utils import dump2csv
        >> from dummy_app.models import *
        >> qs = DummyModel.objects.all()
        >> dump2csv.dump(qs, './data/dump.csv')

    Based on a snippet by zbyte64::

        http://www.djangosnippets.org/snippets/790/

    """
    model = qs.model
    writer = csv.writer(open(outfile_path, 'w'))

    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            row.append(val)
        writer.writerow(row)


def getResultsfromExperienced():
    result = Taskresult.objects.filter(participant__experienced=True)
    dump(result, 'experiencedResult.csv')


def getResultsfromNonExperienced():
    result = Taskresult.objects.filter(participant__experienced=False)
    dump(result, 'nonExperiencedResult.csv')


def getResultsfromAll():
    result = Taskresult.objects.all()
    dump(result, 'allParticipantsResult.csv')


def getResultsTaskWithOneElement():
    result = Taskresult.objects.filter(task__num_of_elements=1)
    dump(result, 'oneElementTaskResult.csv')


def getResultsTaskWithThreeElements():
    result = Taskresult.objects.filter(task__num_of_elements=3)
    dump(result, 'threeElementTaskResult.csv')


def getResultsTaskWithSixElements():
    result = Taskresult.objects.filter(task__num_of_elements=6)
    dump(result, 'sixElementTaskResult.csv')
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


# --- ALL

def getResultsfromAll():
    result = Taskresult.objects.all()
    dump(result, 'allParticipantsResult.csv')


def getResultsfromAllExcludeTask4():
    result = Taskresult.objects.exclude(task_id=4)
    dump(result, 'allParticipantsResultExcludeTask4.csv')


# --- Experienced

def getResultsfromExperienced():
    result = Taskresult.objects.filter(participant__experienced=True)
    dump(result, 'experiencedResult.csv')


def getResultsfromExperiencedExcludeTask4():
    result = Taskresult.objects.filter(participant__experienced=True).exclude(task_id=4)
    dump(result, 'experiencedResultExcludeTask4.csv')


def getResultsfromNonExperienced():
    result = Taskresult.objects.filter(participant__experienced=False)
    dump(result, 'nonExperiencedResult.csv')


def getResultsfromNonExperiencedExcludeTask4():
    result = Taskresult.objects.filter(participant__experienced=False).exclude(task_id=4)
    dump(result, 'nonExperiencedResultExcludeTask4.csv')


# --- Task Results

def getResultsTaskWithOneElement():
    result = Taskresult.objects.filter(task__num_of_elements=1)
    dump(result, 'oneElementTaskResult.csv')


def getResultsTaskWithThreeElements():
    result = Taskresult.objects.filter(task__num_of_elements=3)
    dump(result, 'threeElementTaskResult.csv')


def getResultsTaskWithSixElements():
    result = Taskresult.objects.filter(task__num_of_elements=6)
    dump(result, 'sixElementTaskResult.csv')


# --- GENDER

def getAllMaleResults():
    result = Taskresult.objects.filter(participant__gender='Male')
    dump(result, 'allMaleTaskResults.csv')


def getAllMaleResultsExcludeTask4():
    result = Taskresult.objects.filter(participant__gender='Male').exclude(task_id=4)
    dump(result, 'allMaleTaskResultsExcludeTask4.csv')


def getAllFemaleResults():
    result = Taskresult.objects.filter(participant__gender='Female')
    dump(result, 'allFemaleTaskResults.csv')


def getAllFemaleResultsExcludeTask4():
    result = Taskresult.objects.filter(participant__gender='Female').exclude(task_id=4)
    dump(result, 'allFemaleTaskResultsExcludeTask4.csv')

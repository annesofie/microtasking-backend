import csv

from copy import copy
from pyparsing import basestring
from survey_results.models import Taskresult, Tasksurvey
from base.models import Participant


def dump_taskresult(qs, outfile_path, custom_fields=None):
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
    fields = list(model._meta.get_fields())
    for field in fields:
        print(field)
        headers.append(field.name)
    if custom_fields:
        for field in custom_fields:
            print(field)
            headers.append(field)
    # headers.append('participant_age')
    # headers.append('task_id')
    writer.writerow(headers)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if isinstance(val, basestring):
                val = val.encode('iso-8859-1')
            row.append(val)
        writer.writerow(row)


# --- ALL

def getResultsfromAll():
    result = Taskresult.objects.all()
    dump_taskresult(result, 'allParticipantsResult.csv')


def getResultsfromAllExcludeTask4():
    result = Taskresult.objects.exclude(task_id=4)
    dump_taskresult(result, 'allParticipantsResultExcludeTask4.csv')


def getResultsfromAllExcludeTask4ExcludeParticipant(participantid, participantid2):
    result = Taskresult.objects.exclude(task_id=4).exclude(participant_id=participantid).exclude(
        participant_id=participantid2).exclude(participant_id=117)
    dump_taskresult(result, 'allParticipantsResultExcludeTask4.csv')


# --- Experienced

def getResultsfromExperienced():
    result = Taskresult.objects.filter(participant__experienced=True)
    dump_taskresult(result, 'experiencedResult.csv')


def getResultsfromTaskIdExperienced(taskid):
    result = Taskresult.objects.filter(participant__experienced=True).filter(task_id=taskid)
    dump_taskresult(result, 'experiencedResult.csv')


def getResultsfromExperiencedExcludeTask4():
    result = Taskresult.objects.filter(participant__experienced=True).exclude(task_id=4)
    dump_taskresult(result, 'experiencedResultExcludeTask4.csv')


def getResultsfromNonExperienced():
    result = Taskresult.objects.filter(participant__experienced=False)
    dump_taskresult(result, 'nonExperiencedResult.csv')


def getResultsfromTaskIdNonExperienced(taskid):
    result = Taskresult.objects.filter(participant__experienced=False).filter(task_id=taskid)
    dump_taskresult(result, 'nonExperiencedResult.csv')


def getResultsfromNonExperiencedExcludeTask4():
    result = Taskresult.objects.filter(participant__experienced=False).exclude(task_id=4)
    dump_taskresult(result, 'nonExperiencedResultExcludeTask4.csv')


# --- Task Results

def getResultsTaskWithOneElement():
    result = Taskresult.objects.filter(task__num_of_elements=1)
    dump_taskresult(result, 'oneElementTaskResult.csv')


def getResultsTaskWithThreeElements():
    result = Taskresult.objects.filter(task__num_of_elements=3)
    dump_taskresult(result, 'threeElementTaskResult.csv')


def getResultsTaskWithSixElements():
    result = Taskresult.objects.filter(task__num_of_elements=6)
    dump_taskresult(result, 'sixElementTaskResult.csv')


# --- GENDER

def getAllMaleResults():
    result = Taskresult.objects.filter(participant__gender='Male')
    dump_taskresult(result, 'allMaleTaskResults.csv')


def getAllMaleResultsExcludeTask4():
    result = Taskresult.objects.filter(participant__gender='Male').exclude(task_id=4)
    dump_taskresult(result, 'allMaleTaskResultsExcludeTask4.csv')


def getAllFemaleResults():
    result = Taskresult.objects.filter(participant__gender='Female')
    dump_taskresult(result, 'allFemaleTaskResults.csv')


def getAllFemaleResultsExcludeTask4():
    result = Taskresult.objects.filter(participant__gender='Female').exclude(task_id=4)
    dump_taskresult(result, 'allFemaleTaskResultsExcludeTask4.csv')


# --- AGE SORTED
def get_all_participant_age_ordered():
    taskresult = Taskresult.objects.all().order_by('participant__age', 'participant_id')
    dump_taskresult(taskresult, 'allParticipants_age_sorted.csv')


def get_all_participant_age_ordered_exclude_task4():
    taskresult = Taskresult.objects.exclude(task_id=4).order_by('participant__age', 'participant_id')
    dump_taskresult(taskresult, 'allParticipants_age_sorted_excludetask4.csv')


def get_all_participant_age_ordered_filter_taskid(taskid):
    taskresult = Taskresult.objects.filter(task_id=taskid).order_by('participant__age', 'participant_id')
    dump_taskresult(taskresult, 'allParticipants_age_sorted_taskid_filtered.csv')


# --- AGE and Task sorted
def get_all_participant_age_task_ordered_exclude_task4():
    fields = ['participant_age', 'task_id']
    taskresult = Taskresult.objects.exclude(task_id=4).order_by('participant__age', 'task_id', 'participant_id')
    dump_taskresult(taskresult, 'allParticipants_age_task_sorted_excludetask4.csv', fields)


# --- Task survey
def getTasksurveyResultAll():
    fields = ['participant_experienced', 'task_id']
    result = Tasksurvey.objects.order_by('task_id')
    dump_taskresult(result, 'taskSurveyResultAll.csv', fields)


# --- Totaltime

def getAll():
    getAllFemaleResults()
    getAllMaleResults()
    getResultsTaskWithOneElement()
    getResultsTaskWithThreeElements()
    getResultsTaskWithSixElements()
    getResultsfromNonExperienced()
    getResultsfromExperienced()
    getResultsfromAll()
    getTasksurveyResultAll()


def getAllExcludeTask4():
    getAllFemaleResultsExcludeTask4()
    getAllMaleResultsExcludeTask4()
    getResultsTaskWithOneElement()
    getResultsTaskWithThreeElements()
    getResultsTaskWithSixElements()
    getResultsfromNonExperiencedExcludeTask4()
    getResultsfromExperiencedExcludeTask4()
    getResultsfromAllExcludeTask4()

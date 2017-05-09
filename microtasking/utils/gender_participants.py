
from .dump import dump_taskresult
from survey_results.models import Taskresult, Tasksurvey


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

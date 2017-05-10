from .dump import dump_taskresult
from survey_results.models import Taskresult, Tasksurvey


# --- Experienced

def getResultsfromExperiencedOrderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=True).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'experiencedResult_orderby_' + field + '.csv', fields)


def getResultsfromTaskIdExperienced(taskid, field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=True).filter(task_id=taskid).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'experiencedResult_task'+taskid+'_orderby_'+field+'.csv', fields)


def getResultsfromExperiencedExcludeTask4():
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=True).exclude(task_id=4).filter(totaltime__lte=2000)
    dump_taskresult(result, 'experiencedResultExcludeTask4.csv', fields)


def getResultsfromExperiencedExcludeTask4Orderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=True).exclude(task_id=4).filter(
        totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'experiencedResultExcludeTask4_orderby_' + field + '.csv', fields)


def getResultsfromNonExperiencedOrderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=False).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'inExperiencedResult_orderby_' + field + '.csv', fields)


def getResultsfromTaskIdNonExperienced(taskid, field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=False).filter(task_id=taskid).filter(
        totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'inExperiencedResult_task'+taskid+'_orderby_'+field+'.csv', fields)


def getResultsfromNonExperiencedExcludeTask4OrderBy(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(participant__experienced=False).exclude(task_id=4).filter(
        totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'inExperiencedResultExcludeTask4_orderby_' + field + '.csv', fields)

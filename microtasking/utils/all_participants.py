
from .dump import dump_taskresult
from survey_results.models import Taskresult, Tasksurvey



# --- ALL

def getResultsfromAllOrderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.all().filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'all_orderby_'+ field + '.csv', fields)


def getResultsfromAllExcludeTask4():
    result = Taskresult.objects.exclude(task_id=4).filter(totaltime__lte=2000)
    dump_taskresult(result, 'allExcludeTask4.csv')


def getResultsfromAllExcludeTask4_Orderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.exclude(task_id=4).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'allExcludeTask4_Orderby_' + field + '.csv', fields)


def getResultsfromAllExcludeTask4_Filtertotaltime_Orderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.exclude(task_id=4).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'allExcludeTask4totaltimebiggerthan2000orderby' + field + '.csv', fields)


# -- Task Survey

def get_tasksurvey_participants_was_interupted_orderby(field):
    fields = ['task_id', 'participant_age', 'participant_experienced', 'taskresult_totaltime',
              'taskresult_totalcorrect']
    result = Tasksurvey.objects.exclude(interupted=False).exclude(task_id=4).order_by(field)
    dump_taskresult(result, 'all_wasinterupted_exclude4_orderby_' + field + '.csv', fields)


def get_tasksurvey_participants_was_not_interupted_orderby(field):
    fields = ['task_id', 'participant_age', 'participant_experienced', 'taskresult_totaltime',
              'taskresult_totalcorrect']
    result = Tasksurvey.objects.exclude(interupted=True).exclude(task_id=4).order_by(field)
    dump_taskresult(result, 'all_was_not_interupted_exclude4_orderby_' + field + '.csv', fields)


# --- Task Results

def getResultsTaskWithOneElement():
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(task__num_of_elements=1).filter(totaltime__lte=2000)
    dump_taskresult(result, 'oneElementTaskResult_filtertotaltime.csv')


def getResultsTaskWithOneElementOrderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(task__num_of_elements=1).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'oneElementTaskResult_filtertotaltime_' + field + '.csv')


def getResultsTaskWithThreeElements():
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(task__num_of_elements=3).filter(totaltime__lte=2000)
    dump_taskresult(result, 'threeElementTaskResult_filtertotaltime.csv')


def getResultsTaskWithThreeElementsOrderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(task__num_of_elements=3).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'threeElementTaskResult_filtertotaltime_' + field + '.csv')


def getResultsTaskWithSixElements():
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(task__num_of_elements=6).filter(totaltime__lte=2000)
    dump_taskresult(result, 'sixElementTaskResult_filtertotaltime.csv')


def getResultsTaskWithSixElementsOrderby(field):
    fields = ['participant_age', 'task_id']
    result = Taskresult.objects.filter(task__num_of_elements=6).filter(totaltime__lte=2000).order_by(field)
    dump_taskresult(result, 'sixElementTaskResult_filtertotaltime_' + field + '.csv')

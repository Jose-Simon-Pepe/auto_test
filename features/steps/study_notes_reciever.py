from studynotesreciever.reciever import StudyNoteReciever
from features.helpers.notes_factories import RightNotesFactory
from features.helpers.questionmakertrue import QuestionsMaker


@given(u'student has tagged non empty study notes')
def step_impl(context):
    context.notes = RightNotesFactory.get

@when(u'student put it into system')
def step_impl(context):
    StudyNoteReciever().recieve_notes(context.notes)


@then(u'system should enable student to make questions about')
def step_impl(context):
    assert QuestionsMaker().make_questions()


#@given(u'study note has no tag')
#def step_impl(context):
#    pass


#@then(u'system should not keep note in system')
#def step_impl(context):
#    pass


#@then(u'system should tell user that note has no identifiable tag')
#def step_impl(context):
#    pass


#@given(u'study note has no content')
#def step_impl(context):
#    pass


#@then(u'system should tell user that note has no content')
#def step_impl(context):
#    pass


#@given(u'study note is not a text file')
#def step_impl(context):
#    pass


#@then(u'system should tell user that note is not text file')
#def step_impl(context):
 #   pass

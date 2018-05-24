from django.urls import include, path

from .views import classroom, students, professors

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

    path('professors/', include(([
        path('', professors.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', professors.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', professors.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', professors.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', professors.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', professors.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', professors.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', professors.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='professors')),
]

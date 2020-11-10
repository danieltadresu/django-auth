from django.urls import path

from polls.views import (
    getIndex,
    getLogIn,
    getLogOut,
    postLogIn,
    getSignUp,
    postSignUp,
    getDummyUrl
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('login/', getLogIn, name='getLogIn'),
    path('logout/', getLogOut, name='getLogIn'),
    path('login/auth/', postLogIn, name='postLogIn'),
    path('signup/', getSignUp, name='getSignUp'),
    path('signup/auth/', postSignUp, name='postSignUp'),
    path('dummy/', getDummyUrl, name='getDummyUrl')
]

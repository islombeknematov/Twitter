from django.urls import path
from .views import PostModelListView, PostModelDetailView, \
    PostModelUpdateView, PostModelDeleteView, CommentModelDeleteView, UserProfileModelView, ProfileModelUpdateView

app_name = 'social'

urlpatterns = [
    path('', PostModelListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostModelDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>/', PostModelUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostModelDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentModelDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', UserProfileModelView.as_view(), name='user-profile'),
    path('profile/update/<int:pk>/', ProfileModelUpdateView.as_view(), name='update-profile'),

]
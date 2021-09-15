from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Post, Topic
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required

# -----COMMENT SHORTCUT CTRL+K+C


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


@login_required  # order matters where the @login require piece goes
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # come back later to implement user funtionality

    if request.method == 'POST':  # check IF user is submitting data to the server
        # creates an example of a form to pass the POST data through
        form = NewTopicForm(request.POST)
        if form.is_valid():  # checks if data is valid to then save to DB
            # saves  data to DB and also returns instance of the Model 'Topic' to be saved to 'topic' variable
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            # come back later to implement redirect to topic page created from
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board_pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})

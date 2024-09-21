from django.shortcuts import render

posts = [
  {
    'author': 'CoreyMS',
    'title': 'blog post 1',
    'content': 'first post content',
    'date_posted': 'Augest, 27 2018'
  },
  {
    'author': 'Jane Doe',
    'title': 'blog post 2',
    'content': 'first post content',
    'date_posted': 'Augest, 27 2018'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html',context)


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
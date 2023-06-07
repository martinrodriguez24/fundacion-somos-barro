from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import User, News, Comment
"""
[-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--]
[       Views, sections,                           
[-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--]
"""

def home(request):
    return render(request, 'pages/home.html',
                            {'session': session(request)
                            })

def about(request):
    return render(request, 'pages/about.html',
                            {'session': session(request)
                            })

def blog(request):
    news = News.objects.all()
    if session(request) != False:

        return render(request, 'blog/blog.html',
                                {'news':news,
                                'session': session(request),
                                'email': session(request)[0],
                                'username': session(request)[1]
                                
                                })
    else:
        return render(request, 'blog/blog.html',
                                {'news':news,
                                'session': session(request)})

def video(request):
    return render(request, 'pages/video.html')

def blogCategory(request, category):
    news = News.objects.filter(category=category)
    if session(request) != False:
        return render(request, 'blog/blog.html',
                                {'news':news,
                                'session': session(request),
                                'email': session(request)[0],
                                'username': session(request)[1]
                                })
    else:
        return render(request, 'blog/blog.html',
                                {'news':news,
                                'session': session(request)})

def newsDetail(request, id_news):  
    try: 
        news = News.objects.get(id=id_news)
        comment = news.comments.filter(news_id=id_news)
        if request.method == 'POST':
            
                
            Comment(content=request.POST['comment'],
                    email=session(request)[0],
                    name=session(request)[1],
                    news=news).save()
            return render(request, 'blog/completeNews.html',
                                    {'news': news,
                                    'comment':comment,
                                    'session': session(request)})
               
        return render(request, 'blog/completeNews.html',
                                    {'news': news,
                                    'comment':comment,
                                    'session': session(request)})
    except:
        return redirect('handler404')

"""
[-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--]
[       Login, redirects                          
[-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--]
"""

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:
                User(username=request.POST['username'],
                     email=request.POST['email'],
                     password=request.POST['password1']).save()
                return redirect('signin')

            except IntegrityError:
                return render(request, 'pages/signup.html', 
                                        {'error': 'El usuario ya esta registrado, intenta con otro'})
        return render(request, 'pages/signup.html', 
                                {'error': 'Las contraseñas no coinciden'})
    else:
        return render(request, 'pages/signup.html')

def signin(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(
                email=request.POST['email'],
                password=request.POST['password'])
            request.session['email'] = user.email
            request.session['username'] = user.username
            return redirect('blog')

        except User.DoesNotExist:
            return render(request, 'pages/signin.html', 
                                    {'error': 'Usuario o contraseña incorrectos, intenta nuevamente'})
    else:
        return render(request, 'pages/signin.html')

def signout(request):
    del request.session['email']
    return redirect('home')

def session(request):
    try:
        return [request.session['email'],
                request.session['username']]
    except:
        return False

def handler404(request):
    return render(request, 'pages/404.html')


from django.shortcuts import render
from  datetime import date
from .models import post,Author
# Create your views here.
all_posts = [
    {
        
        "slug" :"in_the_mountainous" ,
        "image" : "mountains.jpg",
        "title" : "mountain hiking",
        "text" : "Mountain hiking embodies what hiking is all about: breathtaking views, fresh air, and a good workout. Here are the insider tips to be safe and have fun.",
        "date" : date(2021,11,29)
    }
,
    {
        "slug" :"hard-coding",
        "image" :"code.jpg",
        "title" :"coding evil",
        "text" : """
         a constant is hard coded and
        remains the same throughout the execution of the program. (2) Programming code that solves a problem but offers less flexibility for future changes.
        """,
        "date" : date(2021,11,25)
    }

]


def starting_page(request):
    latest_posts = post.objects.all().order_by("-date",'title')[:5]
    return render(request,'blog/index.html',{
    "post" : latest_posts})

def posts(request):
    post1 = post.objects.all().order_by("title",)[:5]
    return render(request,"blog/all-posts.html",
        {"posts" :post1})

def full_post(request,slug):
    identified =post.objects.get(slug=slug)
    try:
        return render(request,"blog/post_detail.html",{
       "match": identified
})
    except ValueError() :
        return  render(request,"404.html")

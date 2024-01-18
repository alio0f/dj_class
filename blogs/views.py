from django.db.models import Avg, Max, Min
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import Http404
from blogs.models import product

# Create your views here.
all_post=[
    {'slug':'python-programing',
     'title':'python.py',
     'author':'isavandi',
     'image':'python.png',
     'date':date(1402,1,20),
     'short_description':'python is open source and high level languages',
     'content': 'python is a good lang to learn and earn money'
    },

    {
     'slug':'c-programing',
     'title':'c#',
     'author':'tehrani',
     'image':'c#.png',
     'date':date(1401,9,25),
     'short_description':'c# use by developer',
     'content':'c# is another lang that is very good to use to make money'

    },
    {
     'slug':'php-programing',
     'title':'php',
     'author':'ahmadi',
     'image':'download.jpg',
     'date':date(1399,5,7),
     'short_description':'php is website',
     'content': 'php is a very useful lang in the world'

    }
]
def get_date(post):
    return post['date']


def index(request):
    # d = list(all_post)
    # context = {'a':d}
    # return render(request,'blogs/index.html',context)
    post_sorterd = sorted(all_post,key=get_date)
    leatests = post_sorterd[-2:]
    return render(request,'blogs/index.html',{'latest_posts':leatests})

def post(request):
    return render(request,'blogs/all_post.html',{'all_post':all_post})

def single_post(request,slug):
    post=next(post for post in all_post if post['slug']==slug)
    return render(request, 'blogs/post_details.html', {'post':post})



def list_product(request):
    all_products = product.objects.all().order_by('-price')
    num = all_products.count()
    info = all_products.aggregate(Avg('price'), Max('price'), Min('price'))

    return render(request,'blogs/product_list.html',context={'all_products':all_products,
                                                             'numbers':num,
                                                             'info':info})






def details_product(request,slug):

    pro = get_object_or_404(product,slug=slug)

    return render(request,'blogs/product_details.html',{'pro':pro})




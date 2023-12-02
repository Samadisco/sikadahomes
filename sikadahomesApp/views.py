from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'index.html')

def page_404 (request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def account(request):
    return render(request, 'account.html')

def add_listing(request):
    return render(request, 'add-listing.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog_grid(request):
    return render(request, 'blog-grid.html')

def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html')

def blog_right_sidebar(request):
    return render(request, 'blog-right-sidebar.html')

def blog(request):
    return render(request, 'blog.html')


def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def history(request):
    return render(request, 'history.html')

def locations(request):
    return render(request, 'locations.html')

def login(request):
    return render(request, 'login.html')

def order_tracking(request):
    return render(request, 'order-tracking.html')

def portfolio_2(request):
    return render(request, 'portfolio-2.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def product_details(request):
    return render(request, 'product-details.html')

def register(request):
    return render(request, 'register.html')

def service_details(request):
    return render(request, 'service-details.html')

def service(request):
    return render(request, 'service.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def shop_left_sidebar(request):
    return render(request, 'shop-left-sidebar.html')

def shop_list(request):
    return render(request, 'shop-list.html')

def shop_right_sidebar(request):
    return render(request, 'shop-right-sidebar.html')

def shop(request):
    return render(request, 'shop.html')

def team_details(request):
    return render(request, 'team-details.html')

def team(request):
    return render(request, 'team.html')

def wishlist(request):
    return render(request, 'wishlist.html')























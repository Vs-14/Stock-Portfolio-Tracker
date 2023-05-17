"""StockPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import home
from faq.views import faq
from stockTracker.views import tracker
from stockTrackerSymbol.views import symbol
from auth_app.views import register_view,login_view,logout_view
from portfolioPage.views import portfolio_home
from portfolioStockTracker.views import portfolio_stock_finder
from portfolioSymbol.views import portfolio_symbol
from portfolioPurchase.views import DB_entry
from CheckPortfolio.views import checkPortfolio
from sellPortfolio.views import sell,sold

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('FAQ', faq, name='faq'),
    path('StockTracker', tracker, name='StockTracker'),
    path('StockTracker/Data', symbol, name='StockTracker/Data'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('portfolio', portfolio_home, name='portfolio'),
    path('portfolio/StockTracker', portfolio_stock_finder, name='portfolio/StockTracker'),
    path('portfolio/Data', portfolio_symbol, name='portfolio/Data'),
    path('portfolio/Puchase', DB_entry, name='DB_entry'),
    path('portfolio/CheckPortfolio', checkPortfolio, name='checkPortfolio'),
    path('portfolio/CheckPortfolio/Sell', sell, name='sell'),
    path('portfolio/CheckPortfolio/Sold', sold, name='sold'),
]

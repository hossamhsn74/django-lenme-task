from django.urls import path
from .api import views


urlpatterns = [
    path('borrowers/', views.BorrowerListView.as_view(), name='borrowersList'),
    path('borrower/create/', views.BorrowerCreateView.as_view()),
    path('borrower/<int:pk>/', views.BorrowerDetailView.as_view()),
    path('investors/', views.InvestorListView.as_view(), name='investorsList'),
    path('investor/create/', views.InvestorCreateView.as_view()),
    path('investor/<int:pk>/', views.InvestorDetailView.as_view()),
    path('loans/', views.LoanListView.as_view(), name='loansList'),
    path('loan/create/', views.LoanCreateView.as_view()),
    path('loan/<int:pk>/', views.LoanDetailView.as_view()),
    path('investoraccounts/', views.InvestorAccountListView.as_view(),
         name='investorAccountList'),
    path('investoraccount/create/', views.InvestorCreateView.as_view()),
    path('investoraccount/<int:pk>/', views.InvestorDetailView.as_view()),
    path('requests/', views.RequestListView.as_view(), name='requestsList'),
    path('request/create/', views.RequestCreateView.as_view()),
    path('request/<int:pk>/', views.RequestDetailView.as_view()),
    path('offers/', views.OfferListView.as_view(), name='offersList'),
    path('offer/create/', views.OfferCreateView.as_view()),
    path('offer/<int:pk>/', views.OfferDetailView.as_view()),


]

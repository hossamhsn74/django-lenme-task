from django.contrib import admin
from lenme.models import Borrower, Loan, Offer, Request, InvestorAccount, Investor, Payment


admin.site.register(Borrower)
admin.site.register(Loan)
admin.site.register(Offer)
admin.site.register(Request)
admin.site.register(Investor)
admin.site.register(InvestorAccount)
admin.site.register(Payment)

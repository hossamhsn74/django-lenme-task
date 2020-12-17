from django.contrib import admin
from lenme.models import Borrower, Loan, LoanOffer, LoanRequest, Investor, Investor_Payment, Payment, BorrowerOffer, Borrower_Investor_Loan



admin.site.register(Borrower)
admin.site.register(Loan)
admin.site.register(LoanOffer)
admin.site.register(LoanRequest)
admin.site.register(Investor)
admin.site.register(Investor_Payment)
admin.site.register(Payment)
admin.site.register(Borrower_Investor_Loan)
admin.site.register(BorrowerOffer)
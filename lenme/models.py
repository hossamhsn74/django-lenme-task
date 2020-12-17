from django.db import models


class Borrower(models.Model):
    name = models.CharField(max_length=200)


class LoanRequest(models.Model):
    requester = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.IntegerField()
    period = models.IntegerField()


class Investor(models.Model):
    name = models.CharField(max_length=200)
    balance = models.IntegerField()


class LoanOffer(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    interestRate = models.IntegerField()


class BorrowerOffer(models.Model):
    borrowerId = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    offerId = models.ForeignKey(LoanOffer, on_delete=models.CASCADE)


class Loan(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(
        choices=[("Funded", "Funded"), ("Completed", "Completed")], max_length=200)


class Payment(models.Model):
    loanId = models.ForeignKey(Loan, on_delete=models.CASCADE)


class Borrower_Investor_Loan(models.Model):
    borrowerId = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    investorId = models.ForeignKey(Investor, on_delete=models.CASCADE)
    loanId = models.ForeignKey(Loan, on_delete=models.CASCADE)


class Investor_Payment(models.Model):
    investorId = models.ForeignKey(Investor, on_delete=models.CASCADE)
    paymentId = models.ForeignKey(Loan, on_delete=models.CASCADE)

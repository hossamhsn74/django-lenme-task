from django.db import models


class Investor(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName


class InvestorAccount(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    balance = models.IntegerField()


class Borrower(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName


class Request(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loanAmount = models.IntegerField()
    loanPeriod = models.IntegerField()


class Offer(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    annualInterestRate = models.IntegerField()


class Loan(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    status = models.CharField(
        choices=[("Funded", "Funded"), ("Completed", "Completed")], max_length=200)


class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    releaseDate = models.DateField()

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Borrower, Investor, Offer, Request
from .api.serializers import BorrowerSerializer, InvestorSerializer, OfferSerializer, RequestSerializer


client = Client()


class GetAllBorrowersTest(TestCase):
    """ Test module for GET all Borrowers API """

    def setUp(self):
        Borrower.objects.create(
            firstName='admin1', lastName='manager')
        Borrower.objects.create(
            firstName='admin2', lastName='manager')

    def test_get_all_borrowers(self):
        # get API response
        response = client.get(reverse('borrowersList'))
        # get data from db
        borrowers = Borrower.objects.all()
        serializer = BorrowerSerializer(borrowers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleBorrowerTest(TestCase):
    """ Test module for GET single borrower API """

    def setUp(self):
        self.admin1 = Borrower.objects.create(
            firstName='admin3', lastName='manager')
        self.admin2 = Borrower.objects.create(
            firstName='admin4', lastName='manager')

    def test_get_valid_single_borrower(self):
        response = client.get(
            reverse('borrowerDetails', kwargs={'pk': self.admin1.pk}))
        borrower = Borrower.objects.get(pk=self.admin1.pk)
        serializer = BorrowerSerializer(borrower)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_borrower(self):
        response = client.get(
            reverse('borrowerDetails', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetAllInvestorsTest(TestCase):
    """ Test module for GET all Investors API """

    def setUp(self):
        Investor.objects.create(
            firstName='user1', lastName='test')
        Investor.objects.create(
            firstName='user2', lastName='test')

    def test_get_all_investors(self):
        # get API response
        response = client.get(reverse('investorsList'))
        # get data from db
        investors = Investor.objects.all()
        serializer = InvestorSerializer(investors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleInvestorTest(TestCase):
    """ Test module for GET single Investor API """

    def setUp(self):
        self.user3 = Investor.objects.create(
            firstName='user3', lastName='tester')
        self.user4 = Investor.objects.create(
            firstName='user4', lastName='tester')

    def test_get_valid_single_investor(self):
        response = client.get(
            reverse('investorDetails', kwargs={'pk': self.user3.pk}))
        investor = Investor.objects.get(pk=self.user3.pk)
        serializer = InvestorSerializer(investor)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_investor(self):
        response = client.get(
            reverse('investorDetails', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

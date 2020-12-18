from rest_framework import permissions, authentication
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Borrower, Loan, Offer, Request, InvestorAccount, Investor, Payment
from . import serializers


class BorrowerListView(generics.ListAPIView):
    """
    View to list all borrowers in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Borrower.objects.all()
    serializer_class = serializers.BorrowerSerializer


class BorrowerCreateView(generics.CreateAPIView):
    """
    View to add a new borrower.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Borrower.objects.all()
    serializer_class = serializers.BorrowerSerializer

    def create(self, request, *args, **kwargs):
        super(BorrowerCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added as new Borrower",
                    "result": request.data}
        return Response(response)


class BorrowerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Borrower.objects.all()
    serializer_class = serializers.BorrowerSerializer

    def retrieve(self, request, *args, **kwargs):
        super(BorrowerDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "data": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(BorrowerDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "data": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(BorrowerDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class LoanListView(generics.ListAPIView):
    """
    View to list all loans in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Loan.objects.all()
    serializer_class = serializers.LoanSerializer


class LoanCreateView(generics.CreateAPIView):
    """
    View to add a new loan.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Loan.objects.all()
    serializer_class = serializers.LoanSerializer

    def create(self, request, *args, **kwargs):
        super(LoanCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added new loan",
                    "result": request.data}
        return Response(response)


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Loan.objects.all()
    serializer_class = serializers.LoanSerializer

    def retrieve(self, request, *args, **kwargs):
        super(LoanDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(LoanDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(LoanDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class OfferListView(generics.ListAPIView):
    """
    View to list all offers in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Offer.objects.all()
    serializer_class = serializers.OfferSerializer


class OfferCreateView(generics.CreateAPIView):
    """
    View to add a new offer.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Offer.objects.all()
    serializer_class = serializers.OfferSerializer

    def create(self, request, *args, **kwargs):
        super(OfferCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added new offer",
                    "result": request.data}
        return Response(response)


class OfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Offer.objects.all()
    serializer_class = serializers.OfferSerializer

    def retrieve(self, request, *args, **kwargs):
        super(OfferDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(OfferDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(OfferDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class RequestListView(generics.ListAPIView):
    """
    View to list all loan requests in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Request.objects.all()
    serializer_class = serializers.RequestSerializer


class RequestCreateView(generics.CreateAPIView):
    """
    View to add a new loan request.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Request.objects.all()
    serializer_class = serializers.RequestSerializer

    def create(self, request, *args, **kwargs):
        super(RequestCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added as new loan Request",
                    "result": request.data}
        return Response(response)


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Request.objects.all()
    serializer_class = serializers.RequestSerializer

    def retrieve(self, request, *args, **kwargs):
        super(RequestDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(RequestDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(RequestDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class InvestorListView(generics.ListAPIView):
    """
    View to list all Investors in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Investor.objects.all()
    serializer_class = serializers.InvestorSerializer


class InvestorCreateView(generics.CreateAPIView):
    """
    View to add a new investor.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Investor.objects.all()
    serializer_class = serializers.InvestorSerializer

    def create(self, request, *args, **kwargs):
        super(InvestorCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added as new investor",
                    "result": request.data}
        return Response(response)


class InvestorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Investor.objects.all()
    serializer_class = serializers.InvestorSerializer

    def retrieve(self, request, *args, **kwargs):
        super(InvestorDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "data": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(InvestorDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "data": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(InvestorDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class InvestorAccountListView(generics.ListAPIView):
    """
    View to list all ivestors account details in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = InvestorAccount.objects.all()
    serializer_class = serializers.InvestorAccountSerializer


class InvestorAccountCreateView(generics.CreateAPIView):
    """
    View to add a new Investor account details.
    """
    permission_classes = [permissions.AllowAny]
    queryset = InvestorAccount.objects.all()
    serializer_class = serializers.InvestorAccountSerializer

    def create(self, request, *args, **kwargs):
        super(InvestorAccountCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added new account details",
                    "result": request.data}
        return Response(response)


class InvestorAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = InvestorAccount.objects.all()
    serializer_class = serializers.InvestorAccountSerializer

    def retrieve(self, request, *args, **kwargs):
        super(InvestorAccountDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(InvestorAccountDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(InvestorAccountDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class PaymentsListView(generics.ListAPIView):
    """
    View to list all loan payments in the system.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    """
    View to add a new payment details.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def create(self, request, *args, **kwargs):
        super(PaymentCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added as new payment details",
                    "result": request.data}
        return Response(response)


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PaymentDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PaymentDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(PaymentDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)

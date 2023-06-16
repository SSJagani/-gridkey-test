
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, DayHoldings
from .serializers import TransactionSerializer, DayHoldingsSerializer


# Create your views here.
class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class DayHoldingsView(APIView):
    def get(self, request):
        day_holding_qry = DayHoldings.objects.last()
        print(day_holding_qry.total_cost_price)
        data = {
            'average_buy_price': day_holding_qry.total_cost_price,
            'balance_quantity': day_holding_qry.balance_qty
        }

        message = {
            'status': True,
            'message': 'successfully get data.',
            'data': data,
        }

        return Response(message, status=status.HTTP_200_OK)

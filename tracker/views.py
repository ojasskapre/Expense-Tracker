from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Expenses
from .forms import AddDetailForm
from django.core.mail import send_mail


def home(request):
    expense = Expenses.objects.all()
    return render(request, 'home.html', {'expenses': expense})


def expense_detail(request, name):
    try:
        total_amount = 0
        expense = Expenses.objects.all().filter(name=name)
        for exp in expense:
            total_amount = total_amount + exp.amount
            print(total_amount)
    except Expenses.DoesNotExist:
        raise Http404('Details not found')
    return render(request, 'expense_detail.html', {'expenses': expense, 'amount': total_amount })


def add_detail(request):
    if request.method == 'POST':
        form = AddDetailForm(request.POST)
        if form.is_valid():
            expense = Expenses()
            expense.name = form.cleaned_data['name']
            expense.payment_method = form.cleaned_data['payment_method']
            expense.amount = form.cleaned_data['amount']
            expense.spent_on = form.cleaned_data['spent_on']
            expense.date = form.cleaned_data['date']
            expense.save()
            return HttpResponseRedirect('/')
    else:
        form = AddDetailForm()
        return render(request, 'add_detail.html', {'forms': form })


def delete_detail(request, id):
    Expenses.objects.get(id=id).delete()
    return HttpResponseRedirect('/')

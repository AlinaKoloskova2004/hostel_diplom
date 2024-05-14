from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.http.response import FileResponse
from .models import Product, Contractor, Token
from utils import model_to_xls
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd


class Login(LoginView):
    template_name = 'main/login.html'

    def get_success_url(self):
        user = self.request.user
        token = self.request.POST['user_token']
        Token.objects.update_or_create(user=user, defaults={'token': token})
        return super(Login, self).get_success_url()


class Logout(LogoutView):
    next_page = reverse_lazy('main:index')


@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html', context={})


@login_required(login_url='login')
def products(request):
    return render(request, 'main/products.html', context={})


@login_required(login_url='login')
def contractors(request):
    return render(request, 'main/contractors.html', context={})


@login_required(login_url='login')
def documents(request):
    return render(request, 'main/documents.html', context={})


@login_required(login_url='login')
def operations(request):
    return render(request, 'main/operations.html', context={})


@login_required(login_url='login')
def storage_items(request):
    return render(request, 'main/storage_items.html', context={})


@login_required(login_url='login')
def products_to_xls(request):
    column_descriptions = [
        {'machine_name': 'id', 'display_name': 'Номер'},
        {'machine_name': 'title', 'display_name': 'Наименование', 'width': 80},
        {'machine_name': 'description', 'display_name': 'Описание', 'width': 30},
        {'machine_name': 'price', 'display_name': 'Цена'},
        {'machine_name': 'dt_created', 'display_name': 'Дата создания', 'width': 30},
        {'machine_name': 'dt_updated', 'display_name': 'Дата изменения', 'width': 30},
    ]
    
    products = Product.objects.all()
    for product in products:
        product.dt_created = product.dt_created.replace(tzinfo=None)
        product.dt_updated = product.dt_updated.replace(tzinfo=None)
    
    df = pd.DataFrame(list(products.values()))
    # Remove timezone information
    df['dt_created'] = df['dt_created'].dt.tz_localize(None)
    df['dt_updated'] = df['dt_updated'].dt.tz_localize(None)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'
    
    wb = Workbook()
    ws = wb.active
    ws.append([x['display_name'] for x in column_descriptions])
    
    for row in dataframe_to_rows(df, index=False, header=False):
        ws.append(row)
        
    wb.save(response)
    
    return response
   


@login_required(login_url='login')
def contractors_to_xls(request):
    column_descriptions = [
        {'machine_name': 'id', 'display_name': 'Номер'},
        {'machine_name': 'title', 'display_name': 'Наименование', 'width': 80},
        {'machine_name': 'category', 'display_name': 'Категория', 'width': 30,
         'subs': dict(Contractor.CONTRACTOR_CATEGORY)},
        {'machine_name': 'dt_created', 'display_name': 'Дата создания', 'width': 30},
        {'machine_name': 'dt_updated', 'display_name': 'Дата изменения', 'width': 30},
    ]
    
    contractors = Contractor.objects.all()
    for contractor in contractors:
        contractor.dt_created = contractor.dt_created.replace(tzinfo=None)
        contractor.dt_updated = contractor.dt_updated.replace(tzinfo=None)
    
    df = pd.DataFrame(list(contractors.values()))
    # Remove timezone information
    df['dt_created'] = df['dt_created'].dt.tz_localize(None)
    df['dt_updated'] = df['dt_updated'].dt.tz_localize(None)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=contractors.xlsx'
    
    wb = Workbook()
    ws = wb.active
    ws.append([x['display_name'] for x in column_descriptions])
    
    for row in dataframe_to_rows(df, index=False, header=False):
        ws.append(row)
        
    wb.save(response)
    
    return response

@login_required(login_url='login')
def remove_marked_objects(request):
    return render(request, 'main/remove_marked_objects.html', context={})


@login_required(login_url='login')
def import_products(request):
    return render(request, 'main/import_products.html', context={})


@login_required(login_url='login')
def consolidated_report(request):
    return render(request, 'main/consolidated_report.html', context={})


@login_required(login_url='login')
def motion_report(request):
    report_type = request.GET['report_type']
    return render(request, 'main/motion_report.html', context={'report_type': report_type})

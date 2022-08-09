from cProfile import label
from email import message
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .decorators import allowed_user, admin_only
from django.views.generic import ListView
import datetime
from dateutil.relativedelta import relativedelta
import os
from django.contrib import messages
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Building, Report, Account, ReportType
import json


def loginUser(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                     auth_login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                     return redirect('home')
                else:
                     context = {'msg': 'Invalid Username or Password'}
                     return render(request, 'registration/login.html',context)
        return render(request, 'registration/login.html')
        


@login_required
def home(request):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'scitu-admin':
            return redirect('admin_home')
        
        if group == 'scitu-chief':
            return redirect('chief_home')
        
        if group == 'scitu-staff':
            return redirect('staff_home')

        
def logoutUser(request):
        logout(request)
        return redirect('home')


def dashboard(request):
        i = 0
        status = ['start','received','pending','success']
        labels = []
        labels2 = []
        data1 = [] 
        data2 = []
        data3 = []
        data4 = []
        data5 = [] 
        data6 = []
        data7 = []
        data8 = []
        startper=0
        successper=0
        pendingper=0
        receivedper=0
        type = ReportType.objects.all()
        building = Building.objects.all()
        startdate = request.GET.get('start_date')
        enddate = request.GET.get('end_date')
        report = Report.objects.filter(timestamp__range=[startdate, enddate])
        perbuilding = []
                                
        countReport = report.count()
        start = report.filter(statusReport='start').count()
        if start : startper = round(start/countReport*100,2)

        received = report.filter(statusReport='received').count()
        if received : receivedper = round(received/countReport*100,2)
        
        pending = report.filter(statusReport='pending').count()
        if pending : pendingper = round(pending/countReport*100,2)

        success = report.filter(statusReport='success').count()
        if success : successper = round(success/countReport*100,2)

        for b in building:
                labels.append(b.shortname)
                data1.append(report.filter(statusReport=status[0]).filter(building=b).count())
                data2.append(report.filter(statusReport=status[1]).filter(building=b).count())
                data3.append(report.filter(statusReport=status[2]).filter(building=b).count())
                data4.append(report.filter(statusReport=status[3]).filter(building=b).count())
                if report.filter(building=b).count():
                        perbuilding.append(round(report.filter(building=b).count()/countReport*100,2))

        for t in type:
                labels2.append(t.labels)
                data5.append(report.filter(statusReport=status[0]).filter(type=t).count())
                data6.append(report.filter(statusReport=status[1]).filter(type=t).count())
                data7.append(report.filter(statusReport=status[2]).filter(type=t).count())
                data8.append(report.filter(statusReport=status[3]).filter(type=t).count())

        context = {
                'start': start,
                'startper': startper,
                'received': received,
                'receivedper': receivedper,
                'pending': pending,
                'pendingper': pendingper,
                'success': success,
                'successper': successper,
                'data1': data1,
                'data2': data2,
                'data3': data3,
                'data4': data4,
                'labels':labels,
                'labels2': labels2,
                'data5': data5,
                'data6': data6,
                'data7': data7,
                'data8': data8,
                'perbuilding': perbuilding,
                'countReport':countReport,
                'startdate': startdate,
                'enddate': enddate,
        }
        return render(request, 'dashboard/dashboard.html',context)

def reportbystatus(request):
        labels = []
        data = []
        dataper = []
        startper=0
        successper=0
        pendingper=0
        receivedper=0
        startdate = request.GET.get('start_date')
        enddate = request.GET.get('end_date')
        report = Report.objects.filter(timestamp__range=[startdate, enddate])
        type = ReportType.objects.all()
        countReport = report.count()
        for y in type:
                labels.append(y.labels)
                data.append(report.filter(type=y).count())
                if report.filter(type=y).count() > 0 :
                        datachart=round(report.filter(type=y).count()/countReport*100,2)
                        dataper.append(datachart)
                else : 
                        datachart = 0
                        dataper.append(datachart)

        countStart = report.filter(statusReport='start').count()
        if countStart : startper = round(countStart/countReport*100,2)
        
        countSuccess = report.filter(statusReport='success').count()
        if countSuccess : successper = round(countSuccess/countReport*100,2)
        
        countPending = report.filter(statusReport='pending').count()
        if countPending : pendingper = round(countPending/countReport*100,2)

        countReceived = report.filter(statusReport='received').count()
        if countReceived : receivedper = round(countReceived/countReport*100,2)

        context = {
                'report':report, 
                'labels': labels,
                'data': data,
                'countReport': countReport,
                'countStart': countStart,
                'countSuccess': countSuccess,
                'countPending': countPending,
                'countReceived': countReceived,
                'dataper':dataper,
                'startper': startper,
                'successper': successper,
                'pendingper': pendingper,
                'receivedper': receivedper,
                }
        return render(request, 'summary_report/bystatus.html',context)

def success(request):
        labels = []
        success = []
        successper = []
        startdate = request.GET.get('start_date')
        enddate = request.GET.get('end_date')
        report = Report.objects.filter(timestamp__range=[startdate, enddate])
        type = ReportType.objects.all()
        countReport = report.count()
        countStart = report.filter(statusReport='success').count()
        countSuccess = report.filter(statusReport='success').count()
        countPending = report.filter(statusReport='pending').count()
        countReceived = report.filter(statusReport='received').count()
        
        for y in type:
                labels.append(y.labels)
                if report.filter(type=y).filter(statusReport='success').count() > 0 :
                        datachart=round(report.filter(type=y).filter(statusReport='success').count()/countSuccess*100,2)
                        successper.append(datachart)
                else : 
                        datachart = 0
                        successper.append(datachart)
                success.append(report.filter(type=y).filter(statusReport='success').count())

        context = {
                'report':report.filter(statusReport='success'), 
                'labels': labels,
                'success': success,
                'successper': successper,
                'countReport': countReport,
                'countStart': countStart,
                'countSuccess': countSuccess,
                'countPending': countPending,
                'countReceived': countReceived,
                }
        return render(request, 'summary_report/success.html',context)

def start(request):
        labels = []
        startper = []
        start = [] 
        startdate = request.GET.get('start_date')
        enddate = request.GET.get('end_date')
        report = Report.objects.filter(timestamp__range=[startdate, enddate])
        type = ReportType.objects.all()
        countReport = report.count()
        countStart = report.filter(statusReport='start').count()
        countSuccess = report.filter(statusReport='success').count()
        countPending = report.filter(statusReport='pending').count()
        countReceived = report.filter(statusReport='received').count()

        for y in type:
                labels.append(y.labels)
                if report.filter(type=y).filter(statusReport='start').count() > 0 :
                        datachart=round(report.filter(type=y).filter(statusReport='start').count()/countStart*100,2)
                        startper.append(datachart)
                else : 
                        datachart = 0
                        startper.append(datachart)
                start.append(report.filter(type=y).filter(statusReport='start').count())
        
        context = {
                'report':report.filter(statusReport='start'), 
                'labels': labels,
                'start': start,
                'startper': startper,
                'countReport': countReport,
                'countStart': countStart,
                'countSuccess': countSuccess,
                'countPending': countPending,
                'countReceived': countReceived,
                }
        return render(request, 'summary_report/start.html',context)

def pending(request):
        labels = []
        pendingper = []
        pending = [] 
        startdate = request.GET.get('start_date')
        enddate = request.GET.get('end_date')
        report = Report.objects.filter(timestamp__range=[startdate, enddate])
        type = ReportType.objects.all()
        countReport = report.count()
        countStart = report.filter(statusReport='start').count()
        countSuccess = report.filter(statusReport='success').count()
        countPending = report.filter(statusReport='pending').count()
        countReceived = report.filter(statusReport='received').count()

        for y in type:
                labels.append(y.labels)
                if report.filter(type=y).filter(statusReport='pending').count() > 0 :
                        datachart=round(report.filter(type=y).filter(statusReport='pending').count()/countPending*100,2)
                        pendingper.append(datachart)
                else : 
                        datachart = 0
                        pendingper.append(datachart)
                pending.append(report.filter(type=y).filter(statusReport='pending').count())
        
        context = {
                'report':report.filter(statusReport='pending'), 
                'labels': labels,
                'pending': pending,
                'pendingper': pendingper,
                'countReport': countReport,
                'countStart': countStart,
                'countSuccess': countSuccess,
                'countPending': countPending,
                'countReceived': countReceived,
                }
        return render(request, 'summary_report/pending.html',context)

def received(request):
        labels = []
        receivedper = []
        received = []
        startdate = request.GET.get('start_date')
        enddate = request.GET.get('end_date')
        report = Report.objects.filter(timestamp__range=[startdate, enddate])
        type = ReportType.objects.all()
        countReport = report.count()
        countStart = report.filter(statusReport='start').count()
        countSuccess = report.filter(statusReport='success').count()
        countPending = report.filter(statusReport='pending').count()
        countReceived = report.filter(statusReport='received').count()

        for y in type:
                labels.append(y.labels)
                if report.filter(type=y).filter(statusReport='received').count() > 0 :
                        datachart=round(report.filter(type=y).filter(statusReport='received').count()/countReceived*100,2)
                        receivedper.append(datachart)
                else : 
                        datachart = 0
                        receivedper.append(datachart)
                received.append(report.filter(type=y).filter(statusReport='received').count())
        
        context = {
                'report':report.filter(statusReport='received'), 
                'labels': labels,
                'received': received,
                'receivedper': receivedper,
                'countReport': countReport,
                'countStart': countStart,
                'countSuccess': countSuccess,
                'countPending': countPending,
                'countReceived': countReceived,
                }
        return render(request, 'summary_report/received.html',context)

def reportbylocation(request):
        report = Report.objects.all()

        context = {
                'report':report, 
                'countLc2':report.filter(building=2).count(),
                'countLc3':report.filter(building=3).count(),
                'countLc4':report.filter(building=4).count(),
                'countLc5':report.filter(building=5).count(),
                }
        return render(request, 'summary_report/bylocation.html',context)

def location(request,building_id):
        labels = []
        data1 = [] 
        report = Report.objects.filter(building=building_id)
        countReport = report.count()
        type = ReportType.objects.all()
        built = Building.objects.get(pk=building_id)

        for t in type:
                labels.append(t.labels)
                data1.append((round(report.filter(type=t).count()/countReport*100,2)))

        context = {
                'pk': building_id,
                'built':built,
                'report': report,
                'start': report.filter(statusReport='start').count(),
                'success': report.filter(statusReport='success').count(),
                'pending': report.filter(statusReport='pending').count(),
                'received': report.filter(statusReport='received').count(),
                'data1': data1,
                'labels': labels,
                'countReport': countReport,
                
        }
        return render(request, 'summary_report/location-details.html',context)

def locationtype(request,building_id,type_id):
        labels = []
        data1 = [] 
        pk=building_id
        report = Report.objects.filter(building=pk)
        countReport = report.count()
        type = ReportType.objects.all()
        typeid = type.get(pk=type_id)
        countType = report.filter(type=type_id)

        for t in type:
                labels.append(t.labels)
                data1.append((round(report.filter(type=t).count()/countReport*100,2)))

        context = {
                'pk': pk,
                'typeid': typeid,
                'report': report,
                'start': report.filter(statusReport='start').count(),
                'success': report.filter(statusReport='success').count(),
                'pending': report.filter(statusReport='pending').count(),
                'received': report.filter(statusReport='received').count(),
                'starttype':  countType.filter(statusReport='start').count(),
                'successtype': countType.filter(statusReport='success').count(),
                'pendingtype': countType.filter(statusReport='pending').count(),
                'receivedtype': countType.filter(statusReport='received').count(),
                'data1': data1,
                'labels': labels,
                'countReport': countReport,
                
        }
        return render(request, 'summary_report/location-details-type.html',context)       


def ITstaff(request):
        labels = []
        datatotal = []
        datareceived = []
        datapending = []
        datasuccess = []
        max=0
        report = Report.objects.all()
        account = Account.objects.filter(role='It')
        for a in account:
                labels.append(a.firstname)
                datatotal.append(report.filter(takecareBy=a.pk).count())
                max = max + report.filter(takecareBy=a.pk).count()
                datareceived.append(report.filter(takecareBy=a.pk).filter(statusReport='received').count())
                datapending.append(report.filter(takecareBy=a.pk).filter(statusReport='pending').count())
                datasuccess.append(report.filter(takecareBy=a.pk).filter(statusReport='success').count())

        context = {
                'account': account,
                'labels': labels,
                'datatotal': datatotal,
                'datareceived': datareceived,
                'datapending': datapending,
                'datasuccess': datasuccess,
                'max': max
                }
        return render(request, 'officer/ITstaff.html',context)

def maintenance(request):
        labels = []
        datatotal = []
        datareceived = []
        datapending = []
        datasuccess = []
        max=0
        report = Report.objects.all()
        account = Account.objects.filter(role='Mt')
        for a in account:
                labels.append(a.firstname)
                datatotal.append(report.filter(takecareBy=a.pk).count())
                max = max + report.filter(takecareBy=a.pk).count()
                datareceived.append(report.filter(takecareBy=a.pk).filter(statusReport='received').count())
                datapending.append(report.filter(takecareBy=a.pk).filter(statusReport='pending').count())
                datasuccess.append(report.filter(takecareBy=a.pk).filter(statusReport='success').count())

        context = {
                'account': account,
                'labels': labels,
                'datatotal': datatotal,
                'datareceived': datareceived,
                'datapending': datapending,
                'datasuccess': datasuccess,
                'max': max
                }
        return render(request, 'officer/maintenance.html',context)

def supervisor(request):
        labels = []
        datatotal = []
        datareceived = []
        datapending = []
        datasuccess = []
        max=0
        report = Report.objects.all()
        account = Account.objects.filter(role='Sv')
        for a in account:
                labels.append(a.firstname)
                datatotal.append(report.filter(takecareBy=a.pk).count())
                max = max + report.filter(takecareBy=a.pk).count()
                datareceived.append(report.filter(takecareBy=a.pk).filter(statusReport='received').count())
                datapending.append(report.filter(takecareBy=a.pk).filter(statusReport='pending').count())
                datasuccess.append(report.filter(takecareBy=a.pk).filter(statusReport='success').count())
        context = {
                'account': account,
                'labels': labels,
                'datatotal': datatotal,
                'datareceived': datareceived,
                'datapending': datapending,
                'datasuccess': datasuccess,
                'max': max
                }
        return render(request, 'officer/supervisor.html',context)

def roomcaretaker(request):
        labels = []
        datatotal = []
        datareceived = []
        datapending = []
        datasuccess = []
        max=0
        report = Report.objects.all()
        account = Account.objects.filter(role='Rc')
        for a in account:
                labels.append(a.firstname)
                datatotal.append(report.filter(takecareBy=a.pk).count())
                max = max + report.filter(takecareBy=a.pk).count()
                datareceived.append(report.filter(takecareBy=a.pk).filter(statusReport='received').count())
                datapending.append(report.filter(takecareBy=a.pk).filter(statusReport='pending').count())
                datasuccess.append(report.filter(takecareBy=a.pk).filter(statusReport='success').count())

        context = {
                'account': account,
                'labels': labels,
                'datatotal': datatotal,
                'datareceived': datareceived,
                'datapending': datapending,
                'datasuccess': datasuccess,
                'max': max
                }
        return render(request, 'officer/roomcaretaker.html',context)

def detailofficer(request,pk):
        total_seconds = 0
        timesuccess=[]
        daymin=0
        hourmin=0
        mimin=0
        daymax=0
        hourmax=0
        mimax=0
        day=0
        hour=0
        mi=0
        maximum = 0
        minimum = 0
        account = Account.objects.get(pk=pk)
        report = Report.objects.filter(takecareBy=account)
        reportevent = serializers.serialize("json", report)
        total_report = Report.objects.filter(takecareBy=account).count()
        success_report = Report.objects.filter(takecareBy=account).filter(statusReport='success').count()
        now_report = total_report - success_report

        if total_report != 0:
                for r in report.filter(statusReport='success'):
                        total = r.lastModified - r.timestamp
                        timesuccess.append(total)
                        total_seconds = total_seconds + total.total_seconds()
                        if timesuccess:
                                maximum = max(timesuccess).total_seconds()
                                minimum = min(timesuccess).total_seconds()
                        else:
                                maximum = 0
                                minimum = 0
                daymax = int(maximum / (3600*24))
                hourmax = int(maximum / 3600)
                mimax = int(maximum % 3600 / 60)
                daymin = int(minimum/ (3600*24))
                hourmin = int(minimum / 3600)
                mimin = int(minimum % 3600 / 60)
                avg = total_seconds/total_report
                day = int(avg / (3600*24))
                hour = int(avg / 3600)
                mi = int(avg % 3600 / 60)

        daydate = []
        monthdate = []
        current = 6
        while current <= 6:
                datecal = (datetime.datetime.today() - datetime.timedelta(current)).strftime("%Y-%m-%d")
                daydate.append(datecal)
                print(report.filter(statusReport='success').filter(lastModified=datecal))
                monthdate.append((datetime.datetime.today() - relativedelta(months=+current)).strftime("%b-%Y"))
                current = current-1
                if current == 0: break
        daydate.append(datetime.datetime.today().strftime("%Y-%m-%d"))
        monthdate.append(datetime.datetime.today().strftime("%b-%Y"))


        context = {
                'account': account,
                'report':report,
                'total_report':total_report,
                'success_report':success_report,
                'now_report':now_report,
                'day': day,
                'hour': hour,
                'mi':mi,
                'daymin': daymin,
                'hourmin': hourmin,
                'mimin': mimin,
                'daymax': daymax,
                'hourmax': hourmax,
                'mimax':mimax,
                'daydate': daydate,
                'monthdate': monthdate,
                'reportevent': reportevent
        }
        return render(request, 'officer/detailofficer.html', context)

def managerview(request):
        account = Account.objects.all()
        
        context = {'account':account}
        return render(request, 'officer/managerview.html',context)

def editProfile(request, pk):
        account = Account.objects.get(pk=pk)

        if request.method == "POST":
                if len(request.FILES) != 0:
                        if len(account.image) > 0:
                            os.remove(account.image.path)
                        account.image = request.FILES['image']
                account.firstname = request.POST.get('firstname')
                account.lastname = request.POST.get('lastname')
                account.email = request.POST.get('email')
                account.save()
                messages.success(request, "Profile Updated Successfully")
                return redirect('detailofficer',pk=pk)

        context = {'account':account}
        return render(request, 'officer/editProfile.html',context)

def boardmanager(request):
        labels = []
        datatotal = []
        datareceived = []
        datapending = []
        datasuccess = []
        report = Report.objects.all()
        account = Account.objects.filter(role='Rc')
        for a in account:
                labels.append(a.firstname)
                datatotal.append(report.filter(takecareBy=a.pk).count())
                datareceived.append(report.filter(takecareBy=a.pk).filter(statusReport='received').count())
                datapending.append(report.filter(takecareBy=a.pk).filter(statusReport='pending').count())
                datasuccess.append(report.filter(takecareBy=a.pk).filter(statusReport='success').count())
  
        context = {
                'account': account,
                'labels': labels,
                'datatotal': datatotal,
                'datareceived': datareceived,
                'datapending': datapending,
                'datasuccess': datasuccess
                }
        return render(request, 'officer/boardmanager.html',context)
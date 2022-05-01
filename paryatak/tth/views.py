
import imp
from turtle import color
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from tth.models import Userreg
import matplotlib.pyplot as plt
import io
import urllib
import base64
import mysql.connector
import numpy as np
from numpy.random import choice as np_choice



def home(request):
    return render(request, 'home.html')


def bus(request):
    if request.method == "POST":
        datas=Bus.Company-Bus.Company
        data = Bus.objects.all().order_by("Company")
        return render(request, 'bus.html', {'entries': data})


def Travel(request):
    return render(request, 'Travel.html')


def Ani(request):
    return render(request, 'Animatedmod.html')


def stats(request):
    return render(request, 'stats.html')


def sample(request):
    if not 'umail' in request.session:
        return redirect('loginpage')
    umail = request.session['umail']
    uname = request.session['uname']
    return render(request, 'travel.html', {'umail': umail}, {'uname': uname})


def seat(request):

    return render(request, 'seat.html')


def Userregestration(request):
    if 'umail' in request.session:
        return redirect('travel')
    if request.method == "POST":
        umail = request.POST.get('umail')
        uname = request.POST.get('uname')
        umailObj = Userreg.objects.all().filter(umail=umail)

        if not umailObj:
            saverecord = Userreg()
            saverecord.uname = request.POST.get('uname')
            saverecord.gender = request.POST.get('gender')
            saverecord.umail = request.POST.get('umail')
            saverecord.pwd = request.POST.get('pwd')
            saverecord.trans = request.POST.get('trans')
            saverecord.save()
            messages.success(request, "  Regestration is succesfull!.....")
            print("  Regestration is succesfull!.....")
            request.session['umail'] = umail
            request.session['uname'] = uname
            return redirect('travel')
        else:
            print("User Already Exists")
            return redirect('loginpage')
    return render(request, 'reg1.html')


def loginpage(request):
    if 'umail' in request.session:
        return redirect('travel')
    if request.method == "POST":
        try:
            print(request.POST['umail'], request.POST['pwd'])
            Userdetails = Userreg.objects.get(
                umail=request.POST['umail'], pwd=request.POST['pwd'])
            print("uname", Userdetails)
            request.session['umail'] = Userdetails.umail
            request.session['uname'] = Userdetails.uname  # requesting details
            return redirect('travel')
        except Userreg.DoesNotExist as e:
            print('Username / Password invalid..!')
            messages.success(request, 'Username / Password invalid..!')
    return render(request, 'reg1.html')
    # if request.method=='POST':
    #     form= userreg(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"Travel.html")
    # else:
    #     form=userreg()
    # return render(request,'reg1.html',{'form':form})


def logout(request):
    if 'umail' in request.session:
        del request.session['umail']
    return redirect('loginpage')


def stat1(request):
    mydb = mysql.connector.connect(host="127.0.0.1",
                                 user="root",
                               password="Rsskarthik@123",
                               database="paryatak")
    mycursor = mydb.cursor()
    mycursor.execute("select gender, trans from newreg")
    result = mycursor.fetchall
    gend = []
    tran = []
    for i in mycursor:
        gend.append(i[0])
        tran.append(i[1])
    bar_plt = plt
    plot = plt
    hist_plot = plt

    bar_plt.hist(tran)
    bar_plt.xlabel("gender")

    bar_plt.ylabel("transport")
    bar_plt.title("traveler's Information")
    bar_plt.rc('axes', edgecolor='white')

    fig = bar_plt.gcf()

    buf = io.BytesIO()
    fig.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri1 = urllib.parse.quote(string)

    # plot.bar(gend, tran)
    # plot.xlabel("gender")
    # plot.ylabel("transport")
    # plot.title("traveler's Rate")
    # fig=plot.gcf()
    # buf=io.BytesIO()
    # fig.savefig(buf,format='png')
    # buf.seek(0)
    # string=base64.b64encode(buf.read())
    # uri2=urllib.parse.quote(string)

    # hist_plot.scatter(gend, tran)
    # hist_plot.xlabel("gender")
    # hist_plot.ylabel("transport")
    # hist_plot.title("traveler's Bio")
    # fig=hist_plot.gcf()
    # buf=io.BytesIO()
    # fig.savefig(buf,format='png')
    # buf.seek(0)
    # string=base64.b64encode(buf.read())
    # uri3=urllib.parse.quote(string)
    context = {
        'data1': uri1,
        'data2': uri1,
        'data3': uri1
  }

    return render(request, 'home.html', context)

    
class Shortdresults(object):

    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
    
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            print (shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone = self.pheromone * self.decay            
        return all_time_shortest_path

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move


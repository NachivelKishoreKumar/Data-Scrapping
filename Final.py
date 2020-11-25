import requests
import csv
import flask
from flask import *
from bs4 import BeautifulSoup
def Vultr():
    arr2=[]
    arr3=["STORAGE","CPU","MEMORY","BANDWIDTH","PRICE /mo"]
    result1=requests.get("https://www.vultr.com/products/cloud-compute/#pricing")
    soup1=BeautifulSoup(result1.content,"html.parser")
    rows =soup1.findAll("div", {"class":"pt__cell"})

    for i in range(1,len(rows)):
        z=rows[i]
        for cell in z.findAll('strong'):
            w=cell.text
            arr2.append(w)

    with open('vultr.csv','w') as f:
        thewriter=csv.writer(f)
        thewriter.writerow(arr3)
        for p in range(0,50,5):
            thewriter.writerow(arr2[p:p+5])
    return arr2

def Linode():
    arr=[]
    arr1=[]
    arr2=['RAM', 'CPU', 'Storage', 'Transfer', 'Network In', 'Network Out', 'Price']
    arr3=['RAM', 'CPU', 'Storage', 'GPU Cards', 'Transfer', 'Network In', 'Network Out', 'Price']
    result=requests.get("https://www.linode.com/pricing/")
    soup=BeautifulSoup(result.content,"html.parser")
    table_body=soup.findAll('tbody')
    tb1=soup.find('thead')

    for i in range(1):
        for w in tb1.findAll('th'):
            d=w.text
            arr.append(d)
    for i in range(0,len(table_body)):
        z=table_body[i]
        for row1 in z.findAll('th'):
            t=row1.text
            arr1.append(t)
        for row in z.findAll('td'):
            x=row.text
            arr.append(x)

    for j,i in zip(range(0,21),range(7,161,7)):
        arr.insert(i,arr1[j])

    for j,i in zip(range(21,25),range(154,182,8)):
        arr.insert(i, arr1[j])
#print(arr)
    with open('linode.csv','w') as f:
            thewriter=csv.writer(f)
            thewriter.writerow(arr2)
            for p in range(7,154,7):
                thewriter.writerow(arr[p:p+7])

    with open('linode.csv', 'a') as f:
        thewriterr = csv.writer(f)
        thewriterr.writerow(arr3)
        for p in range(154,182,8):
            thewriterr.writerow(arr[p:p + 8])

    for i in range(157,179,7):
        arr.pop(i)
#print(arr)
    return arr

def Buyvm():
    arr5=[]
    arr6=["CORE","CPU USAGE","MEMORY","STORAGE","BANDWIDTH","PROTOCOL VERSION","PRICE"]
    arr7=["CORE","MEMORY","STORAGE","BANDWIDTH","PRICE"]
    result=requests.get("https://buyvm.net/kvm-dedicated-server-slices/")
    soup=BeautifulSoup(result.content,"html.parser")
    table_body=soup.findAll('table',{"class":"plantable"})
    tb1=soup.findAll('div',{"class":"plan-description"})
    for i in range(0,len(tb1)):
        z=tb1[i]
        for row1 in z.findAll('li'):
            u=row1.text
            arr5.append(u)
    p=table_body[0]
    for row in p.findAll('td'):
       p=row.text
       arr5.append(p)
    with open('buyvm.csv','w') as f:
        thewriter=csv.writer(f)
        thewriter.writerow(arr6)
        for p in range(0,28,7):
            thewriter.writerow(arr5[p:p+7])

    with open('buyvm.csv','a') as g:
        thewriter1 = csv.writer(g)
        thewriter1.writerow(arr7)
        for n in range(28,64,6):
            thewriter1.writerow(arr5[n:n+5])

    return arr5

def Hetzner():
    arr = []
    arr1 = []
    arr2 = ["CPU", "", "RAM", "", "DISKSPACE", "", "TRAFFIC", "", "PRICE"]
    result = requests.get("https://www.hetzner.com/cloud")
    soup = BeautifulSoup(result.content, "html.parser")
    rows = soup.findAll("div", {"class": "pricing-section"})

    for i in range(0,len(rows)):
        z = rows[i]
        for cell in z.findAll("span"):
            p = cell.text
            arr.append(p)
    table_body = soup.findAll('table', {"class": "price-table"})
    for i in range(0, 15):
        z = table_body[i]
        for row in z.findAll('td'):
            k = row.text
            arr1.append(k)

    for i, j in zip(range(0, 15), range(8, 165, 11)):
        arr1.insert(j, arr[i])

    with open('hetzner.csv', 'w') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(arr2)
        for p in range(0, 165, 11):
            thewriter.writerow(arr1[p:p + 9])
    return arr1

def upcld():
    arr1 = ['MEMORY', 'CPU', 'STORAGE', 'TRANSFER', 'PRICE/mo']
    arr4 = []
    result2 = requests.get("https://upcloud.com/pricing/")
    soup2 = BeautifulSoup(result2.content, "html.parser")
    rows1 = soup2.findAll("div", {"class": "block"})
    for i in range(0,len(rows1)):
        z = rows1[i]
        for cell1 in z.findAll("h3"):
            o = cell1.text
            arr4.append(o)

    with open('upcld.csv', 'w') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(arr1)
        for p in range(0, 50, 5):
            thewriter.writerow(arr4[p:p + 5])

    return arr4

app = Flask(__name__)

@app.route('/device')
def deviceSelect():
    return render_template("fin.html")

@app.route('/device/Pricing',methods=['GET','POST'])
def Pricing():
    Cloud = request.form["Cloud"]
    if Cloud=="vultr":
        a=Vultr()
        return render_template("vultr.html", len=len(a), a=a)
    if Cloud=="linode":
        a=Linode()
        return render_template("linode.html", len=len(a), a=a)
    if Cloud=="buyvm":
        a=Buyvm()
        return render_template("buyvm.html", len=len(a), a=a)
    if Cloud=="hetzner":
        a=Hetzner()
        return render_template("hetzner.html", len=len(a), a=a)
    if Cloud=="upcloud":
        a=upcld()
        return render_template("upcld.html", len=len(a), a=a)

@app.route('/devices')
def devicesSelect():
    return render_template("fin_result.html")

@app.route('/devices/Calc',methods=['GET','POST'])
def Calc():
    Cloud = request.form["Cloud"]
    price=[]
    if Cloud=="vultr":
        a=Vultr()
        Storage = request.form["storage"]
        CPU = request.form["CPU"]
        value = str(Storage) + " GB"
        value1 = str(CPU) + " CPU"

        for x, y in zip(range(0, 50), range(1, 50)):
            if (a[x] == value and a[y] == value1):
                price.append(a[x + 4])

        return render_template("result.html", len=len(price), price=price)
    if Cloud == "linode":
        a=Linode()
        Storage = request.form["storage"]
        CPU = request.form["CPU"]
        value = str(Storage) + " GB SSD"
        if CPU == 1:
            value1 = str(CPU) + " Core"
        else:
            value1 = str(CPU) + " Cores"
        for x, y in zip(range(8, 182), range(9, 182)):
            if (a[x] == value1 and a[y] == value):
                price.append(a[x + 5])
        return render_template("result.html", len=len(price), price=price)
    if Cloud=="buyvm":
        a=Buyvm()
        Storage = request.form["storage"]
        CPU = request.form["CPU"]

        if CPU == 1:
            value1 = str(CPU) + " Core "
        else:
            value1 = str(CPU) + " Cores"

        if int(Storage) >= 160:
            value = str(Storage) + " GB SSD"
            for x, y in zip(range(32, 73), range(35, 73)):
                if (a[x] == value1 and a[y] == value):
                    price.append(a[y + 2])
            return render_template("result.html", len=len(price), price=price)

        if int(Storage) < 81:
            value = str(Storage) + " GB SSD Storage"
            for x, y in zip(range(0, 32), range(4, 32)):
                if (a[x] == value1 and a[y] == value):
                    price.append(print(a[y + 3]))
            return render_template("result.html", len=len(price), price=price)
    if Cloud=="hetzner":
        a=Hetzner()
        Storage = request.form["storage"]
        CPU = request.form["CPU"]
        value = str(Storage) + " GB"
        for x, y in zip(range(0, 165), range(4, 165)):
            if (a[x] == CPU and a[y] == value):
                price.append(a[x + 8])
        return render_template("result.html", len=len(price), price=price)
    if Cloud=="upcloud":
        a=upcld()
        Storage = request.form["storage"]
        CPU = request.form["CPU"]

        value = str(Storage) + " GB"
        for x, y in zip(range(1, 50), range(2, 50)):
            if (a[x] == CPU and a[y] == value):
                price.append(a[x + 3])
        return render_template("result.html", len=len(price), price=price)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

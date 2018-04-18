from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

def init(request):
    request.session['amount'] = 0 ## total spent
    request.session['total'] = 0 ## total items bought
    request.session['temp'] = 0 ## purchase amount for item checked out
    return redirect('/amadon')

def index(request):
    return render(request, 'first_app/index.html')

def process(request):
  if request.POST['id'] == "tshirt":
    request.session['total'] += int(request.POST['quantity'])
    tempamount = int(request.POST['quantity']) * 19.99
    request.session['temp'] = tempamount
    request.session['amount'] += tempamount
    return redirect('/amadon/checkout')
  
  if request.POST['id'] == "sweater":
    request.session['total'] += int(request.POST['quantity'])
    tempamount = int(request.POST['quantity']) * 29.99
    request.session['temp'] = tempamount
    request.session['amount'] += tempamount
    return redirect('/amadon/checkout')
  
  if request.POST['id'] == "cup":
    request.session['total'] += int(request.POST['quantity'])
    tempamount = int(request.POST['quantity']) * 4.99
    request.session['temp'] = tempamount
    request.session['amount'] += tempamount
    return redirect('/amadon/checkout')
  
  if request.POST['id'] == "book":
    request.session['total'] += int(request.POST['quantity'])
    tempamount = int(request.POST['quantity']) * 49.99
    request.session['temp'] = tempamount
    request.session['amount'] += tempamount
    return redirect('/amadon/checkout')

def checkout(request):
  return render(request, 'first_app/checkout.html')


  # if request.method == "POST":
  #   print(request.POST['id'])
  #   print(request.POST['quantity'])
  #   if request.POST['id'] == 1:
  #     quantity = int(request.POST['quantity'])
  #     total = quantity * 19.99
  #     request.session['charge'] = total
  #   elif request.POST['id'] == 2:
  #     quantity = int(request.POST['quantity'])
  #     total = quantity * 29.99
  #     request.session['charge'] = total
  #   elif request.POST['id'] == 3:
  #     quantity = int(request.POST['quantity'])
  #     total = quantity * 4.99
  #     request.session['charge'] = total
  #   elif request.POST['id'] == 4:
  #     quantity = int(request.POST['quantity'])
  #     total = quantity * 49.99
  #     request.session['charge'] = total

  #   if not 'itemcount' in request.session:
  #     request.session['itemcount'] = 0
  #   count = request.session['itemcount']
  #   count = count + quantity
  #   request.session['itemcount'] = 0

  #   if not 'totalspent' in request.session:
  #     request.session['totalspent'] = 0
  #   totalspent = request.session['totalspent']
  #   totalspent += total
  #   request.session['totalspent'] = totalspent

  #   return redirect('/checkout')
  # else:
  #   return redirect('/')
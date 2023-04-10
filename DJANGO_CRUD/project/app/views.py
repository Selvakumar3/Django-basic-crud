from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Details

# HOME page function
def index(request):
    return render(request,'index.html')

# create function for CRUD
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        degree=request.POST['degree']
        address=request.POST['address']
        image=request.POST['image']        # another method;FILES.get()
        obj=Details.objects.create(name=name,age=age,gender=gender,degree=degree,address=address,image=image)
        obj.save()
        return redirect('retrieve')

#  VIEW function for CRUD    
def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})


# EDIT function for CRUD
def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request,'update.html',{'object': object})
 
#update function for CRUD   
def update(request,id):
    obj=Details.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST['name']
        obj.age=request.POST['age']
        obj.gender=request.POST['gender']
        obj.degree=request.POST['degree']
        obj.address=request.POST['address']
        obj.image=request.POST['image']
        obj.save()
        return redirect('retrieve')   

# delete function for CRUD
def delete(request,id):
    object = Details.objects.get(id=id)
    object.delete()
    return redirect('retrieve')



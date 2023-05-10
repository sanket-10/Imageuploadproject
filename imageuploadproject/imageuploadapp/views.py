from django.shortcuts import render,HttpResponse
from imageuploadapp.forms import ImageUploadForm
from imageuploadapp.models import ImageUploadModel

# Create your views here.


def upload_fie(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Image Uploaded Successfully...!</h1>")

    else:
        form = ImageUploadForm()
        images = ImageUploadModel.objects.all()
    return render (request,"index.html",{'form': form,'images':images})


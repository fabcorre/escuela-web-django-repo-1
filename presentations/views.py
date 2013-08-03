#encoding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render







def create_edit_presentation(request,p_id=None):
    if request.method == 'POST':
        form = CreateEditPresentationForm(request.POST)
        if form.is_valid():
            if not p_id:
                p = Presentation(**form.cleaned_data)
                p.save()
                return HttpResponse(status=201)
            else:
                p = Presentation.objects.get(id=p_id)
                p.update(**form.cleaned_data)
                return HttpResponse(status=200)
        return HttpResponse(form.errors, status=400)


    if p_id:
        p = Presentation.objects.get(id=p_id)
        form = CreateEditPresentationForm(instance=p)
    else
        form = CreateEditPresentationForm()

    context = {
        'form': form
    }

    return HttpResponse(form.as_table(), status=200)



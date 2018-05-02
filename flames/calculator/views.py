from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.views.generic import FormView




def flames(request):
    form = forms.Flames(request.POST)
    if form.is_valid():
        form.save()
        your_name = form.cleaned_data['your_name']
        partner_name = form.cleaned_data['partner_name']
        # print(your_name)
        # print(partner_name)
        your_name = [i for i in your_name]
        partner_name = [i for i in partner_name]

        for i in range(len(your_name)):
            for i in your_name:
                if i in partner_name:
                    your_name.remove(i)
                    partner_name.remove(i)
        # print(your_name)
        # print(partner_name)


        count = len(your_name) + len(partner_name)
        flames = ['f','l','a','m','e','s']

        for i in range(5):
            value = (count % len(flames)) - 1
            flames.remove(flames[value])
            if(value>0):
                flames = flames[value:] + flames[:value]
        flames = flames[0]
        f_dict = {
            'f': 'FRIENDSHIP',
            'l': 'LOVE',
            'a': 'AFFECTION',
            'm': 'Marriage',
            'e': 'Enemy',
            's': 'Sister (Siblings)'
        }
        if (your_name != partner_name):
        out = f_dict[flames]
        elif (your_name == partner_name):
            out = " Don't try to FOOL me, You love yourslef the most"
        return render(request,"flames.html",{"flames" : out})
    return render(request,"flames.html",{'Form':form})



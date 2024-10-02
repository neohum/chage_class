import pandas as pd
import sqlite3
import os, io, random, string

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import InfoModel
from django.views import View
import asyncio


#schoolnames
schoolnames = ''.join(random.choices(string.ascii_letters, k=12))

# 

class UploadFileForm(forms.Form):
  file = forms.FileField()
 
  
# Create your views here.
def home(request):
  
  return render(request, 'change_classes/home.html')
  

async def upload(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        #kappa 
        
        kappa = request.FILES['file']
        df = pd.read_excel(kappa)
        df['total'] = df['수업태도'] + df['학습능력'] + df['교우관계']
        df = df.sort_values(by=['total', '성별'], ascending=[False, True])
        woman = df[df['성별'] == '여']
        man = df[df['성별'] == '남']
        shuffled_woman = woman.sample(frac=1).reset_index(drop=True)
        shuffled_man = man.sample(frac=1).reset_index(drop=True)
        
        # Shuffle the DataFrame rows
        #shuffled_df = df.sample(frac=1).reset_index(drop=True)
        
        # Get the number of classes from the POST data
        num_classes = 8
        print(request.POST.get(f"newclass: {request.POST.get('newclass')}"))
        # Assign classes randomly
        #shuffled_df['다음 반'] = (shuffled_df.index % num_classes) + 1
        shuffled_woman['다음 반'] =(shuffled_woman.index % num_classes) + 1
        shuffled_man['다음 반'] =(shuffled_man.index % num_classes) + 1
        # Save the new DataFrame
        #new_df = shuffled_df.copy()
        new_df = pd.concat([shuffled_woman, shuffled_man], axis=0)
        
        
        # Save the DataFrame to an Excel file
        output_file_path = f"templates/downloads/{schoolnames}_{kappa.name}"
        new_df.to_excel(output_file_path, engine='openpyxl', index=False)
        
        print(f"Data saved to {output_file_path}")
        
    
    return render(request, 'change_classes/home.html')
  
def index(request):
    if request.method == "POST":
        schoolname = request.POST['schoolname']
        oldgrade = request.POST['oldgrade']
        newgrade = request.POST['newgrade']
        oldclass = request.POST['oldclass']
        newclass = request.POST['newclass']
        redirect('change_classes/home.html', {'schoolname': schoolname, 'oldgrade': oldgrade, 'newgrade': newgrade, 'oldclass': oldclass, 'newclass': newclass})
        
        
      
    return render(request, 'change_classes/index.html')
        
  
def result(request):
    
   
    return render(request, 'change_classes/result.html')
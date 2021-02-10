# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import datetime

# Create your views here.
def index(request):
    context = {

    }
    return render(request, "index.html", context)
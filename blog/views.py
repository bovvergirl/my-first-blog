from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include


def post_list(request):
    return render(request, 'blog/post_list.html', {})
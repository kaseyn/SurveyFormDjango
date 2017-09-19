from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if "count" not in request.session:
		request.session["count"] = 0
	return render(request, "survey/index.html")

def process(request):
	request.session["name"] = request.POST["name"]
	request.session["location"] = request.POST["location"]
	request.session["language"] = request.POST["language"]
	request.session["comment"] = request.POST["comment"]
	request.session["count"] += 1
	return redirect("/result")

def result(request):
	return render(request, "survey/result.html")
from django.shortcuts import render,HttpResponse,redirect
from django.template.loader import render_to_string
from django.http import StreamingHttpResponse
from .models import *
from .forms import UserLogin
from .gemini import *

# Create your views here.
def login(request):
    note=""

    if request.method=="POST":
        print(request.POST)
        form=UserLogin(request.POST)
        if form.is_valid():
            CurrentUser=CustomUser(name=form.cleaned_data["name"],password=form.cleaned_data["password"])
            ExistingUser=CustomUser.objects.filter(name=CurrentUser.name)

            if len(ExistingUser):
                if CurrentUser.password==ExistingUser[0].password:
                    request.session["user"]=ExistingUser[0].id
                    return redirect("/chat/")
                else:
                    note="Wrong Password!"
            else:
                CurrentUser.save()
                request.session["user"]=CurrentUser.id
                return redirect("/chat/")
            
    else:
        form=UserLogin()
    return render(request,"login.html",{"form":form,"note":note})

def chat(request):
    user=CustomUser.objects.filter(id=request.session.get("user"))

    if user:
        user=user[0]
    else:
        return redirect("/login/")
    
    
    if request.method=="POST":
        if  "delete" in request.POST:
            for log in user.chatlog_set.all():
                log.delete()


        elif "submit" in request.POST:
            prompt=request.POST["prompt"]
 
            user.chatlog_set.create(role="user",log=prompt)

            def generatereply(geminiprompt):
                reply=""
                for tokens in askgemini(user.name,geminiprompt):
                    if tokens.text:
                        reply+=tokens.text
                        yield tokens.text

                user.chatlog_set.create(role="model",log=reply)

            
            contextlength=10
            previouslogs=user.chatlog_set.all().order_by("-id")[:contextlength][::-1]
            fullprompt=[{"role":log.role,"parts":[{"text":log.log}]} for log in previouslogs]


            return StreamingHttpResponse(generatereply(fullprompt),content_type="text/plain")



    return render(request,"chat.html",{"logs":user.chatlog_set.all().order_by("id"),"name":user.name})

    




    

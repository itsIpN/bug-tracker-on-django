from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Bugs
from .forms import ProjectForm, BugForm, ProjectUpdateForm, BugUpdateForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    bugs = Bugs.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {'bugs': bugs, 'projects': projects})

@login_required
def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project_index.html', {'projects': projects})

@login_required
def bug_index(request):
    bugs = Bugs.objects.all()
    return render(request, 'bug_index.html', {'bugs': bugs})

@login_required
def bug_filtered(request):
    bugs = Bugs.objects.filter(assigned_to=request.user)
    requser = User.objects.filter(username = request.user)
    return render(request, 'bug_index.html', {'bugs': bugs, 'requser':requser})

@login_required
def project_details(request, project_id):
    bugs = Bugs.objects.filter(project = project_id)
    project = Project.objects.get(id = project_id)
    return render(request, 'project_details.html', {'project': project, 'bugs': bugs})

@login_required
def bug_details(request, bugs_id):
    bugs = Bugs.objects.get(id = bugs_id)
    project = Project.objects.get(id = bugs.project_id)
    unassigned_user = User.objects.exclude(id__in = bugs.assigned_to.all().values_list('id'))
    return render(request, 'bug_details.html', {'bugs' : bugs, 'project': project, 'unassigned_user': unassigned_user})


def register(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

@login_required
def assign_user(request, bugs_id, user_id):
    Bugs.objects.get(id=bugs_id).assigned_to.add(user_id)
    return redirect('bug_details', bugs_id=bugs_id)

@login_required
def unassign_user(request, bugs_id, user_id):
    Bugs.objects.get(id=bugs_id).assigned_to.remove(user_id)
    return redirect('bug_details', bugs_id=bugs_id)

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/projects/' 

class BugCreate(LoginRequiredMixin, CreateView):
    model = Bugs
    form_class = BugForm
   
    def get_form_kwargs(self):
        kwargs = super(BugCreate, self).get_form_kwargs()
        kwargs['project'] = self.request.GET.get('project')
        return kwargs

class BugUpdate(LoginRequiredMixin, UpdateView):
    model = Bugs
    form_class = BugUpdateForm

class BugDelete(LoginRequiredMixin, DeleteView):
    model = Bugs
    success_url = '/' 
from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model  = models.Project

    template_name ='project/list.html'

    paginate_by = 3

    login_url = "/login/"
    redirect_field_name = "project/list.html"

    def get_queryset(self):
        query_set = super().get_queryset()
        where =  {}
        q = self.request.GET.get('q', None)
        if q: 
            where['title__icontains'] = q
        return query_set.filter(**where)
    
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name ='project/create.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUdateForm
    template_name ='project/update.html'
    
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')

        
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
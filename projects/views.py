from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model  = models.Project

    template_name ='project/list.html'

    paginate_by = 3

    login_url = "/login/"
    redirect_field_name = "project/list.html"

    def get_queryset(self):
        query_set = super().get_queryset()
        where =  {'user_id':self.request.user}
        q = self.request.GET.get('q', None)
        if q: 
            where['title__icontains'] = q
        return query_set.filter(**where)
    
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name ='project/create.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = models.Project
    form_class = forms.ProjectUdateForm
    template_name ='project/update.html'

    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
     
class ProjectDeleteView(LoginRequiredMixin, DeleteView,UserPassesTestMixin):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')

    
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
     
class TaskCreateView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    
    def test_func(self):
        project_id = self.request.POST.get('project','')
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
       
class TaskUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
    
class TaskDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
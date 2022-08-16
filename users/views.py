from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            group = form.cleaned_data['groups']

            if group is not None:
                user_group = Group.objects.get(name=form.cleaned_data['groups'])
                user.groups.add(user_group)

                return redirect('login')


            # for form_ug in form.cleaned_data['groups']:
            #     user_group = Group.objects.get(name=form_ug.name)
            #     user.groups.add(user_group)
            else:
                return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})

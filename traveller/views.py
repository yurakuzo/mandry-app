from django.shortcuts import render, redirect  # noqa: disable=f401
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .forms import SignUpForm
from django.contrib.auth import login
from .forms import UpdateProfileForm
from traveller.models import Traveller
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'traveller/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'traveller/profile.html'


class ProfileDetailView(DetailView):
    model = Traveller
    template_name = 'traveller/profile.html'
    context_object_name = 'user'


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=request.user.id)
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'traveller/update_profile.html', {'form': form})


@login_required
def leave_comment(request, user_id):
    profile_user = get_object_or_404(Traveller, id=user_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # The form data is valid
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.receiver = profile_user
            new_comment.save()
            return redirect('profile', pk=user_id)
        else:
            # Form data is not valid, return the form with errors
            return render(request, 'path/to/comment_form_template.html', {'form': form, 'profile_user': profile_user})

    # If not a POST request, show the empty form
    form = CommentForm()
    return render(request, 'path/to/comment_form_template.html', {'form': form, 'profile_user': profile_user})

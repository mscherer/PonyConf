from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from proposals.forms import TalkForm
from proposals.models import Speech, Talk, Topic
from .signals import new_talk


def home(request):
    return render(request, 'proposals/home.html')


@login_required
def talk_list(request):
    return render(request, 'proposals/talks.html', {
        'my_talks': Talk.on_site.filter(speakers=request.user),
        'other_talks': Talk.on_site.exclude(speakers=request.user),
    })


@login_required
def talk_list_by_topic(request, topic):
    topic = get_object_or_404(Topic, slug=topic)
    return render(request, 'proposals/talk_list.html', {
        'title': 'Talks related to %s:' % topic,
        'talk_list': Talk.on_site.filter(topics=topic),
    })


@login_required
def talk_list_by_speaker(request, speaker):
    speaker = get_object_or_404(User, username=speaker)
    return render(request, 'proposals/talk_list.html', {
        'title': 'Talks with %s:' % speaker,
        'talk_list': Talk.on_site.filter(speakers=speaker),
    })


@login_required
def talk_edit(request, talk=None):
    if talk:
        talk = get_object_or_404(Talk, slug=talk)
        if talk.site != get_current_site(request):
            raise PermissionDenied()
        if not talk.has_perm(request.user):
            raise PermissionDenied()
    form = TalkForm(request.POST or None, instance=talk)
    if request.method == 'POST' and form.is_valid():
        if hasattr(talk, 'id'):
            talk = form.save()
            messages.success(request, 'Talk modified successfully!')
        else:
            talk = form.save(commit=False)
            talk.site = get_current_site(request)
            talk.proposer = request.user
            talk.save()
            form.save_m2m()
            Speech.objects.create(speaker=request.user, talk=talk)
            new_talk.send(talk.__class__, instance=talk)
            messages.success(request, 'Talk proposed successfully!')
        return redirect(talk.get_absolute_url())
    return render(request, 'proposals/talk_edit.html', {
        'form': form,
    })


class TalkDetail(LoginRequiredMixin, DetailView):
    queryset = Talk.on_site.all()
    def get_context_data(self, **kwargs):
        context = super(TalkDetail, self).get_context_data(**kwargs)
        context['edit_perm'] = self.object.is_editable_by(self.request.user)
        return context


class TopicList(LoginRequiredMixin, ListView):
    model = Topic


class SpeakerList(LoginRequiredMixin, ListView):
    queryset = User.objects.filter(speech__talk=Talk.on_site.all())
    template_name = 'proposals/speaker_list.html'


@login_required
def user_details(request, username):
    return render(request, 'proposals/user_details.html', {
        'user': get_object_or_404(User, username=username).profile,
    })

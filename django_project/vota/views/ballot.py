# coding=utf-8
"""Views for projects."""
# noinspection PyUnresolvedReferences
import logging
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, CreateView
from vota.forms import BallotCreateForm
from vota.models import Ballot, Committee

logger = logging.getLogger(__name__)


class BallotMixin(object):
    model = Ballot
    form_class = BallotCreateForm


class BallotDetailView(LoginRequiredMixin, BallotMixin, DetailView):
    context_object_name = 'ballot'
    template_name = 'ballot/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BallotDetailView, self).get_context_data(**kwargs)
        context['committee'] = Committee.objects.get(
            id=self.object.committee.id)
        return context

    def get_queryset(self):
        ballot_qs = Ballot.open_objects.all()
        return ballot_qs


class BallotCreateView(LoginRequiredMixin, BallotMixin, CreateView):
    context_object_name = 'ballot'
    template_name = 'ballot/create.html'

    def get_success_url(self):
        return reverse('ballot-detail', kwargs={
            'project_slug': self.object.committee.project.slug,
            'committee_slug': self.object.committee.slug,
            'slug': self.object.slug
        })
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, TemplateView, UpdateView, DeleteView, CreateView, View
from tutoring.models import Tutor, Client, Session
from tutoring.forms import SessionForm
from users.models import User
from decimal import Decimal

@method_decorator(login_required, name='dispatch')
class ManagerDashboardView(TemplateView):
    template_name = "tutoring/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(ManagerDashboardView, self).get_context_data(**kwargs)
        context["sessions"] = Session.objects.all()

        return context

@method_decorator(login_required, name='dispatch')
class AccountingView(TemplateView):
    template_name = "tutoring/accounting.html"

@method_decorator(login_required, name='dispatch')
class ClientsView(TemplateView):
    template_name = "tutoring/clients.html"

    def get_context_data(self, **kwargs):
        context = super(ClientsView, self).get_context_data(**kwargs)
        context["clients"] = Client.objects.all().order_by('user__last_name')

        return context

@method_decorator(login_required, name='dispatch')
class TutorsView(TemplateView):
    template_name = "tutoring/tutors.html"

    def get_context_data(self, **kwargs):
        context = super(TutorsView, self).get_context_data(**kwargs)
        context["tutors"] = Tutor.objects.all().order_by('user__last_name')

        return context

@method_decorator(login_required, name='dispatch')
class UserAccountingView(TemplateView):
    pass

@method_decorator(login_required, name='dispatch')
class TutorDashboardView(TemplateView):
    template_name = "tutoring/dashboard.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(TutorDashboardView, self).get_context_data(**kwargs)
        context["sessions"] = Session.objects.filter(tutor__user=user)

        return context

@method_decorator(login_required, name='dispatch')
class ClientDashboardView(TemplateView):
    template_name = "tutoring/dashboard.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(ClientDashboardView, self).get_context_data(**kwargs)
        context["sessions"] = Session.objects.filter(client__user=user)

        return context

@method_decorator(login_required, name='dispatch')
class SessionView(TemplateView):
    template_name = "tutoring/session.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        session_id = kwargs['session_id']
        session = Session.objects.get(id=session_id)

        context = super(SessionView, self).get_context_data(**kwargs)
        context['session'] = session
        
        return context

@method_decorator(login_required, name='dispatch')
class CreateSessionView(CreateView):
    model = Session
    template_name = 'tutoring/session-form.html'
    form_class = SessionForm
    
    def get_success_url(self):
        return reverse_lazy('session-detail', args=(self.object.id, ))

@method_decorator(login_required, name='dispatch')
class DashboardView(RedirectView):
    """
    Redirects the user to the appropriate dashboard
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user

        return user.dashboard

class SessionNoteUpdate(View):
    def post(self, request, session_id):
        notes = request.POST['notes']
        session = Session.objects.get(id=session_id)

        session.notes = notes
        session.save()

        return HttpResponse(status=200)

class SessionPaymentUpdate(View):
    def post(self, request, session_id):
        payment = request.POST['payment']
        session = Session.objects.get(id=session_id)

        session.paid += Decimal(payment)
        session.save()

        return HttpResponse(status=200)

class SessionEarningsUpdate(View):
    def post(self, request, session_id):
        payment = request.POST['payment']
        session = Session.objects.get(id=session_id)

        session.earnings_paid += Decimal(payment)
        session.save()

        return HttpResponse(status=200)


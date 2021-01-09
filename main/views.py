from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


class TermsView(TemplateView):
    template_name = 'main/terms.html'

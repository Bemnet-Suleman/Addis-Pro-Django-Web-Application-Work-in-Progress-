from django.urls import path
from . import views
urlpatterns=[
path("",views.home,name="home"),
path("portifolo/",views.portifolo,name="portifolo"),
path("portifolo/<int:id>/",views.portifolo_detail,name="portifolo_detail"),
path("services/",views.services,name="services"),
path("contact us/",views.contact,name="contact us"),
path("about us/",views.about,name="about us"),
path("privacy&policy/",views.privacy_and_policy,name="privacy&policy"),
path("terms of services/",views.terms_of_services,name="terms of services"),
path("testimonial/",views.testimonial,name="testimonial"),
path("team/",views.teams,name="Our teams"),
path("order/",views.order,name="order"),
path("pages/",views.pages,name="pages")]

from django.conf.urls import url
from django.urls import path
from django.core.exceptions import MultipleObjectsReturned
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/

urlpatterns = [
    # ex: /accounts/signup/
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    # url(r'user-base/', views.SignUpView.as_view(), name='user-base'),
    # user
    url(r'^$', views.Index.as_view(), name='index'),
    # url(r'^$', views.index, name='index'),
    url(r'article', views.article, name="article"),
    # url(r'article', views.article, name="article"),
    path('adetail/<int:pk>/', views.adetail, name="adetail"),
    path('type/<int:category_id>/', views.type, name="type"),
    # url(r'article_detail', views.article_detail, name="article_detail"),
    url(r'enterprise', views.enterprise, name="enterprise"),
    # url(r'company', views.company, name="company"),
    url(r'blog', views.blog, name="blog"),
    # url(r'blog', views.blog, name="blog"),
    url(r'bdetail', views.bdetail, name="bdetail"),
    # url(r'blog_detail', views.blog_detail, name="blog_detail"),
    url(r'plan', views.plan, name="plan"),
    # url(r'plan', views.plan, name="plan"),
    url(r'review', views.review, name="review"),
    # url(r'review', views.review, name="review"),
    url(r'staff', views.staff, name="staff"),
    # url(r'staff', views.staff, name="staff"),
    url(r'sdetail', views.sdetail, name="sdetail"),
    # url(r'staff_detail', views.staff_detail, name="staff_detail"),
    url(r'chat', views.chat, name="chat"),
    # url(r'chat', views.chat, name="chat"),
    url(r'fav', views.fav, name="fav"),
    # url(r'favorite', views.favorite, name="favorite"),
    url(r'notice_c', views.notice_c, name="notice_c"),
    # url(r'notice_company', views.notice_company, name="notice_company"),
    url(r'ncdetail', views.ncdetail, name="ncdetail"),
    # url(r'notice_company_detail', views.notice_company_detail, name="notice_company_detail"),
    url(r'nengine', views.nengine, name="nengine"),
    # url(r'notice_engine', views.notice_engine, name="notice_engine"),
    url(r'nedetail', views.nedetail, name="nedetail"),
    # url(r'notice_engine_detail', views.notice_engine_detail, name="notice_engine_detail"),
    url(r'order', views.order, name="order"),
    # url(r'order', views.order, name="order"),
    url(r'odetail', views.odetail, name="odetail"),
    # url(r'order_detail', views.order_detail, name="order_detail"),
    url(r'cancel', views.cancel, name="cancel"),
    # url(r'order_cancel', views.order_cancel, name="order_cancel"),
    url(r'ocdetail', views.ocdetail, name="ocdetail"),
    # url(r'order_cancel_detail', views.order_cancel_detail, name="order_cancel_detail"),
    url(r'onotExecuted', views.onotExecuted, name="onotExecuted"),
    # url(r'order_notExecuted', views.order_notExecuted, name="order_notExecuted"),
    url(r'ondetail', views.ondetail, name="ondetail"),
    # url(r'order_notExecuted_detail', views.order_notExecuted_detail, name="order_notExecuted_detail"),
    url(r'register', views.register, name="register"),
    # url(r'register', views.register, name="register"),
    url(r'rdetail', views.SignUpView.as_view(), name="rdetail"),
    # url(r'register_detail', views.register_detail, name="register_detail"),
    url(r'reserve', views.reserve, name="reserve"),
    # url(r'reserve', views.reserve, name="reserve"),
    url(r'rdate', views.rdate, name="rdate"),
    # url(r'reserve_date', views.reserve_date, name="reserve_date"),
    url(r'rddetail', views.rddetail, name="rddetail"),
    # url(r'reserve_date_detail', views.reserve_date_detail, name="reserve_date_detail"),
    url(r'rpayment', views.rpayment, name="rpayment"),
    # url(r'reserve_payment', views.reserve_payment, name="reserve_payment"),
    url(r'rpdetail', views.rpdetail, name="rpdetail"),
    # url(r'reserve_payment_detail', views.reserve_payment_detail, name="reserve_payment_detail"),
    url(r'rconfirmation', views.rconfirmation, name="rconfirmation"),
    # url(r'reserve_confirmation', views.reserve_confirmation, name="reserve_confirmation"),
    url(r'rdone', views.rdone, name="rdone"),
    # url(r'reserve_done', views.reserve_done, name="reserve_done"),
    url(r'search', views.search, name="search"),
    # url(r'search', views.search, name="search"),
    url(r'setting', views.setting, name="setting"),
    # url(r'setting', views.setting, name="setting"),
    url(r'sinquiry', views.sinquiry, name="sinquiry"),
    # url(r'setting_companyInquiry', views.setting_companyInquiry, name="setting_companyInquiry"),
    url(r'scontact', views.scontact, name="scontact"),
    # url(r'setting_contact', views.setting_contact, name="setting_contact"),
    url(r'scredit', views.scredit, name="scredit"),
    # url(r'setting_credit', views.setting_credit, name="setting_credit"),
    url(r'screditAdd', views.screditAdd, name="screditAdd"),
    # url(r'setting_creditAdd', views.setting_creditAdd, name="setting_creditAdd"),
    url(r'screditEdit', views.screditEdit, name="screditEdit"),
    # url(r'setting_creditEdit', views.setting_creditEdit, name="setting_creditEdit"),
    url(r'shidden', views.shidden, name="shidden"),
    # url(r'setting_hidden', views.setting_hidden, name="setting_hidden"),
    url(r'stpoint', views.stpoint, name="stpoint"),
    # url(r'setting_tpoint', views.setting_tpoint, name="setting_tpoint"),
    # url(r'sunsubscribe', views.sunsubscribe, name="sunsubscribe"),
    # url(r'setting_unsubscribe', views.setting_unsubscribe, name="setting_unsubscribe"),
    url(r'suserDetailChange', views.suserDetailChange, name="suserDetailChange"),
    # url(r'setting_userDetailChange', views.setting_userDetailChange, name="setting_userDetailChange"),
    url(r'login', views.Login.as_view(), name="login"),
    # url(r'login', views.login, name="login"),
    url(r'logout', views.Logout.as_view(), name="logout"),
    # url(r'logout', views.logout, name="logout"),
    # path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete'),
    # 退会
    path('Company_dataListView', views.Company_dataListView.as_view(), name='Company_dataListView'),
    # path('search/<int:pk>/', views.fav, name='search'),   
]
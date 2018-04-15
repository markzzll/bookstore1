from django.conf.urls import url
from users import views

urlpatterns = [

	url(r'^register/$',views.register,name='register'),

	url(r'^register_handle',views.register_handle,name='register_handle'),

	url(r'^login/$',views.login,name='login'),

	url(r'^login_check/$',views.login_check,name='login_check'),

	url(r'^logout/$',views.logout,name='logout'),

	url(r'^$', views.user, name='user'), # 用户中心-信息页

	url(r'^address/$',views.address,name='address'),#用户中心-地址页

	url(r'^order/$',views.order,name='order'),
#用户中心-订单页

	url(r'^verifycode/$',views.verifycode,name='verifycode'),
	#验证码功能

	url(r'^active/(?P<token>.*)/$', views.register_active, name='active'),  # 用户激活

]
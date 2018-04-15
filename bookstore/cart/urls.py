from django.conf.urls import url
from cart import views

urlpatterns = [
	#添加
	url(r'^add/$',views.cart_add,name='add'),
#获取用户购物车中商品的数目
	url(r'^count/$',views.cart_count,name='count'),
#展示购物车页面的功能
	url(r'^$',views.cart_show,name='show'),
#删除购物车中商品的信息
	url(r'^del/$',views.cart_del,name='delete'),
#更新购物车商品数目
	url(r'^update/$',views.cart_update,name='update')

]
from django.urls import path
from ecomapp import views


app_name = 'ecomapp'
urlpatterns = [

    path('', views.home.as_view(), name='home'),

    path('about/', views.about.as_view(), name='about'),
    path('base/', views.base.as_view(), name='base'),
    path("all-product/", views.AllProductView.as_view(), name='all-product'),
    path("product-details/<slug:slug>/", views.ProductDetails.as_view(), name="product-details"),

    path("add-to-cart-<int:pro_id>/", views.AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", views.MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", views.ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", views.EmptyCartView.as_view(), name= "emptycart"),
    path("check-out/", views.CheckOutView.as_view(), name="checkout"),

    path("register/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", views.CustomerLogOutView.as_view(), name="customerlogout"),
    path("login/", views.CustomerLoginView.as_view(), name = "customerlogin"),

    path("profile/", views.CustomerProfileView.as_view(), name = "customerprofile"),
    path("profile/order-<int:pk>/", views.CustomerOrderDetailView.as_view(), name="customerorderdetail"),

    path("search/", views.SearchView.as_view(), name= "search"),
    path("forgot-password/", views.PasswordForgotView.as_view(), name="passwordforgot"),
    path("password-reset/<email>/<token>/", views.PasswordResetView.as_view(), name="passwordreset"),

    path("admin-login/", views.AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", views.AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>", views.AdminOrderDetailView.as_view(), name="adminorderdetail"),
    path("admin-all-orders/", views.AdminOrderListView.as_view(), name='adminorderlist'),
    path("admin-order-<int:pk>-change/", views.AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),
    path("admin-product/list", views.AdminProductListView.as_view(), name = "adminproductlist"),
    path("admin-product/add", views.AdminProductCreateView.as_view(), name = "adminproductcreate")


]
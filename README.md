# PyShopDjango

1. Create Django Project

2. Run Development web server
	* open Terminal 
	* run command - 
	``` 
	python manage.py runserver
	```

3. Add new package  'products'
	* run command -
	```
	python manage.py startapp products
	```

4. Create first simple Hello World view
	 * on file views.py:
	 
  ```
  from django.shortcuts import render
  from django.http import HttpResponse      

  def index(request):  
      return HttpResponse('Hello World')
  ```

 5. URL Mapping
	* add 'urls.py' to package
	* create mapping to views module
```
from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.index),  
]
```
  * add mapping to main urls.py file
```
from django.contrib import admin  
from django.urls import path, include  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('products/', include('products.urls')),
]
```

6. Models
	* create class in models.py
	```
	from django.db import models
	
	class Product(models.Model):  
	    name = models.CharField(max_length=255)  
	    price = models.FloatField()  
	    stock = models.IntegerField()  
	    image_url = models.CharField(max_length=2083)
	 ```

7. Migrations
	* add the referance for this app to main settings.py 
		```
		INSTALLED_APPS = [
		    ...
		    ...
		         'products.apps.ProductsConfig', 
		     ]```
	* run command  -``` python manage.py makemigrations```
	* run command  - ```python manage.py migrate```

8. use Admin panel
	* create superuser:
		* run command - 
		```
		python manage.py createsuperuser
		```
	* register models in admin.py
	```
	from django.contrib import admin  
	from .models import Product, Order  
	  
	class ProductAdmin(admin.ModelAdmin):  
	    list_display = ('name', 'price', 'stock')  
	  
	class OrderAdmin(admin.ModelAdmin):  
	    list_display = ('customer_name', 'customer_email')  
	  
	admin.site.register(Product, ProductAdmin)  
	admin.site.register(Order, OrderAdmin)
	```

9. Template
	* import models and edit view functions
	 ```
		from .models import Product 
		
		def index(request):  
		    products = Product.objects.all()  
		    return render(request, 'index.html',  
				  {'products': products})			  	
	```
	* create template index.html in templates folder 
	 ```
	 	<!--templates/index.html-->
		<h1>Products</h1>  
		<ul>  
		  {% for product in products %}  
	        <li>{{ product.name }} (${{ product.price }})</li>  
		  {% endfor %}  
		</ul>			  	
	```

10. Add Bootstrap
	*  [getbootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
	* create base.html file
		* add block content in body
	* update index.html to extend base.html
	* define the block content

11. Rendering Cards

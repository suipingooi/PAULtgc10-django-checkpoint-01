from django.urls import path
import books.views

urlpatterns = [
    path('', books.views.index),
    path('create', books.views.create_book),
    path('update/<book_id>', books.views.update_book,
         name='update_book'),
    path('publishers/create', books.views.create_publisher),
    path('publishers', books.views.show_publishers,
         name='show_publishers'),
    path('publishers/update/<publisher_id>',
         books.views.update_publisher, name="update_publisher"),
    path('publishers/delete/<publisher_id>',
         books.views.delete_publisher, name="delete_publisher")
]

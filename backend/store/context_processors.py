from .models import Category
# Return the categories that are avialable
def categories(request):
    return {
        'categories': Category.objects.all()
    }
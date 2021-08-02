from .models import Category, Vendor


def all_category(request):
    category_list = Category.objects.all()

    params = {
        'category_list': category_list,
    }

    return params


def all_vendor(request):
    vendor_list = Vendor.objects.all()

    params = {
        'vendor_list': vendor_list,
    }

    return params
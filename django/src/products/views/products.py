from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from products.models import Product

from products.forms import ProductModelForm


class RestProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 3

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name,
                    'slug': itm.slug,
                    'price': itm.price,
                    'category': itm.category.name if itm.category else None,
                    'image': itm.image.url if itm.image else None
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RestProductListView, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_products:products')

        data['previous_url'] = None
        data['next_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page{page.previous_page_number()}'

        if page.has_next():
            data['next_url'] = f'{route_url}?page{page.next_page_number()}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     queryset = context.get('product_list')
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(queryset, 2)
    #     page_obj = paginator.get_page(page)
    #
    #     context['page_obj'] = page_obj
    #
    #     return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product_chars'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:products')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'slug', 'description', 'price', 'category', 'image']
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:products')


def products(request):
    chars = Product.objects.all()
    return render(
        request,
        'products/catalog.html',
        {
            'product_list': chars
        }
    )


def product_view(request, slug):
    char = Product.objects.get(slug=slug)
    return render(
        request,
        'products/product.html',
        {
            'product_chars': char
        }
    )


def product_create_view(request):
    form = ProductModelForm()
    success_url = reverse('products:products')

    if request.method == 'POST':
        form = ProductModelForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/create.html',
        {'form': form}
    )


def product_update_view(request, slug):
    obj = get_object_or_404(Product, slug=slug)

    form = ProductModelForm(instance=obj)
    success_url = reverse('products:products')

    if request.method == 'POST':
        form = ProductModelForm(
            request.POST,
            files=request.FILES,
            initial=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {
            'form': form,
            'product': obj
        }
    )


def product_delete_view(request, slug):
    obj = get_object_or_404(Product, slug=slug)
    success_url = reverse('products:products')

    if request.method == "POST":
        obj.delete()
        return redirect(success_url)

    return render(
        request,
        'products/delete.html',
        {'product': obj}
    )

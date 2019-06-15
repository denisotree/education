from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator

from products.models import Category

from products.forms import CategoryModelForm


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/list.html'
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     context = super(CategoryListView, self).get_context_data(**kwargs)
    #     queryset = context.get('category_list')
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(queryset, 2)
    #     page_obj = paginator.get_page(page)
    #
    #     context['page_obj'] = page_obj
    #
    #     return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        products = obj.product_set.all()
        page = self.request.GET.get('page')
        paginator = Paginator(products, 2)
        page_obj = paginator.get_page(page)

        return {
            'inst': obj,
            'products': page_obj
        }


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'categories/update.html'
    success_url = reverse_lazy('categories:list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('categories:list')
    context_object_name = 'inst'


def category_create_view(request):
    form = CategoryModelForm()
    success_url = reverse('products:products')

    if request.method == 'POST':
        form = CategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def category_update_view(request, pk):
    obj = get_object_or_404(Category, pk=pk)

    form = CategoryModelForm(instance=obj)
    success_url = reverse('products:products')

    if request.method == 'POST':
        form = CategoryModelForm(
            request.POST,
            files=request.FILES,
            initial=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'categories/update.html',
        {'form': form}
    )


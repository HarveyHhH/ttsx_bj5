from haystack.generic_views import SearchView


class MySearchView(SearchView):
    def get_context_data(self,*args,**kwargs):
        context = super(MySearchView,self).get_context_data(*args,**kwargs)
        context['choice'] = '0'
        context['title'] = '天天生鲜'
        page_obj = context['page_obj']
        page_list = []
        if page_obj.paginator.num_pages < 5:
            page_list = range(1,page_obj.paginator.num_pages+1)
        elif page_obj.number<=2:
            page_list = range(1,5+1)
        elif page_obj.number>=page_obj.paginator.num_pages-1:
            page_list = range(page_obj.paginator.num_pages-5+1,page_obj.paginator.num_pages+1)
        else:
            page_list = range(page_obj.number-2,page_obj.number+3)
        context['page_list'] = page_list
        return context

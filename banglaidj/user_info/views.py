from django.shortcuts import render

# Create your views here.

def show_user_info(request):
    ''' A django view to show user's info'''
    if request.method == 'POST':
        user_name_value = request.POST['user_name']
        context = {'name': user_name_value}
    return render(request, 'user_info/user_info.html', context)



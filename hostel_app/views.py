from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from hostel_app.forms import RoomSearchForm, BookingForm
from hostel_app.models import Room, Staff, Booking
from django.core.paginator import Paginator
from profile_user.models import Profile
from .forms import BookingForm, ProfileForm


class HostelAppView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'rooms.html'

    def get_queryset(self):
        return self.model.objects.filter(hottest=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staffs'] = Staff.objects.all()
        context['form'] = SubscriberForm()
        return context

    def post(self, request):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'subscribed.html')
        else:
            queryset = self.get_queryset()
            staff = Staff.objects.all()
            return render(request, self.template_name, context={'rooms': queryset, 'staffs': staff, 'form': form})
        
   

class HostelAppView2 (ListView):
   model = Room
   context_object_name = 'rooms'
   template_name = 'rooms2.html'
   paginate_by = 3
   
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(object_list=object_list, **kwargs)
       context['object-count'] = self.model.objects.count()
       paginator = Paginator(self.model.object_list, self.paginate_by)
       try:
           page = self.request.GET.get('page')
       except:
           page = 1
           
       try:
           context[self.context_object_name] = paginator.page(page)
       except:
           context[self.context_object_name] = paginator.page(1)
           
       context['object-count'] = self.model.objects.count()
       context['paginator'] = paginator
       return context
  
   def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        
        form = RoomSearchForm(self.request.GET)
        if form.is_valid():
            pass
        
        else:
            form = RoomSearchForm()
            
        context['form'] = form
        return context
        
   def get(self, request, *args, **kwargs):
       form = RoomSearchForm(self.request.GET)
       if form.is_valid():
           cd = form.cleaned_data
           rooms = self.model.objects.filter(name__icontains=cd['search'])
       else:
           rooms = self.model.objects.all()
       return render(request, self.template_name, self.get_context_data(object_list=rooms))
   
    
   
class StaffView (ListView):
   model = Staff
   context_object_name = 'staffs'
   template_name = 'rooms.html'
   
   
def restaurant_view(request):
    context = {'page':'restaurant'}
    return render(request, 'restaurant.html',context)

   
def fitness_view(request):
    context = {'page':'fitness'}
    return render(request, 'fitness.html',context)




   
def room_id_view(request, pk):
    pk = get_object_or_404(Room, pk=pk)
    booking = Booking.objects.all()
    if request.method=="POST": 
        form = BookingForm(request.POST) 
        if form.is_valid(): 
            booking =  form.save(commit=False) 
            booking.rooms = pk 
            booking.save() 
            form = BookingForm() 
    else:
        form = BookingForm()
    context = {"pk": pk,'page':'rooms', 'booking_list':booking, 'form':form}
    return render(request, "rooms_details.html", context)



def book_room(request):
    booking = Booking.objects.all()
    if request.method=="POST": 
        form = BookingForm(request.POST) 
        if form.is_valid(): 
            booking =  form.save(commit=False) 
            booking.save() 
            form = BookingForm() 
    else:
        form = BookingForm()
    context = {'page':'rooms', 'booking_list':booking, 'form':form, }
    return render(request, "booking.html", context)

def create_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile/success.html',{'profile': profile})
    except Profile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, 'profile/success.html', {'profile': profile})
    else:
        form = ProfileForm()
    return render(request, 'profile/create_profile.html', {'form': form})


def success(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/success.html', {'profile': profile})


def view_profile(request):
    profile = Profile.objects.get(user=request.user)
   
    return render(request, 'profile/profile_user.html', {'profile': profile})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, 'profile/success.html', {'profile': profile})
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/edit_profile.html', {'form': form})



from .forms import SubscriberForm


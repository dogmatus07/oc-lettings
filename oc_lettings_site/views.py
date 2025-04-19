from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile



# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'index.html')

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)

def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)

def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)

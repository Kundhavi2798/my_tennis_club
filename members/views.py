from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.template import loader
from .models import Member
from .form import MemberForm


# Create your views here.
def members(request):
    template = loader.get_template('myfirst.html')
    # This view will render a list of members
    return render(request, 'myfirst.html')

# View to list all members at /members/
def all_members(request):
    members = Member.objects.all()
    return render(request, 'all_members.html', {'members': members})

def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.first_name = request.POST['first_name']
        member.last_name = request.POST['last_name']
        member.email = request.POST['email']
        member.phone_number = request.POST['phone_number']
        member.save()
        return redirect('all_members')
    return render(request, 'edit_member.html', {'member': member})
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Member not found", status=404)

    if request.method == 'POST':
        member.first_name = request.POST.get('first_name', member.first_name)
        member.last_name = request.POST.get('last_name', member.last_name)
        member.email = request.POST.get('email', member.email)
        member.phone_number = request.POST.get('phone_number', member.phone_number)
        member.save()
        return redirect('all_members')
         

    return render(request, 'edit_member.html', {'member': member})

def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('all_members')
    return render(request, 'delete_member.html', {'member': member})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_members')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})
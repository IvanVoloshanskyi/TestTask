from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from groups.forms import GroupForm
from users.models import Group, User


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/group_list.html', {'groups': groups})


def group_add(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group added successfully')
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'groups/group_form.html', {'form': form})


def group_edit(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/group_form.html', {'form': form})


def group_delete(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    users_in_group = User.objects.filter(group=group)

    if users_in_group.exists():
        messages.error(request, 'Group deletion is not allowed because it has associated users.', extra_tags='danger')
        return redirect('group_list')

    group.delete()
    messages.success(request, 'Group deleted successfully.')
    return redirect('group_list')

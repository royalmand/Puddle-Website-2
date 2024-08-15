from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import ConversationMessageForm
from conversation.models import Conversation

# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass # TODO: redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation 
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:details', pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/newconvo.html', {
        'form': form
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def details(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    return render(request, 'conversation/details.html', {
        'conversation': conversation
    })
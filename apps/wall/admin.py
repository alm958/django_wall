from django.contrib import admin

# Register your models here.
from .models import User, Message, Comment
from .forms import UserForm

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    # class Meta:
    #     model = User

class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Message

class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment

admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)

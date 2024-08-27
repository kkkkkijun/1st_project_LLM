from cafe.models import Comment
from users.models import Like
from django import forms

class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment
        fields = [ 
            "content",
            "menu_id"
        ]
        widgets = {
            "content" : forms.Textarea(
                attrs={
                    "placeholder" : "댓글 달기..."
                }
            )
        }

class LikeForm(forms.ModelForm): 
    class Meta: 
        model = Like
        fields = [
            "user_id", 
            "menu_id"
        ]
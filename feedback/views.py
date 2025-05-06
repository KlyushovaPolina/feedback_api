from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializer
from .forms import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages

class FeedbackCreateAPIView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Обращение успешно отправлено",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Обращение успешно отправлено!')
            return redirect('feedback:feedback_form')
        else:
            messages.error(request, 'Ошибка при отправке. Проверьте форму.')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import UserFile
from .google_drive import get_drive_service
from googleapiclient.http import MediaFileUpload
import os
import magic

def get_category(mime_type):
    if mime_type.startswith('image'):
        return 'image'
    elif mime_type.startswith('video'):
        return 'video'
    elif mime_type in ['application/pdf', 'application/msword',
                       'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        return 'document'
    else:
        return 'other'

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = form.cleaned_data['file_name']

            # Завантаження файлу на сервер
            file_path = os.path.join('uploads', uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Визначення категорії файлу за MIME типом
            mime = magic.Magic(mime=True)
            mime_type = mime.from_file(file_path)
            category = get_category(mime_type)

            # Завантаження файлу на Google Drive
            drive_service = get_drive_service()
            file_metadata = {'name': file_name}
            media = MediaFileUpload(file_path, resumable=True)
            file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            file_id = file.get('id')

            # Збереження інформації про файл у базі даних
            user_file = UserFile(user=request.user, file_name=file_name, file_id=file_id, category=category)
            user_file.save()

            # Видалення файлу з локального сервера після завантаження
            os.remove(file_path)

            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'files/upload.html', {'form': form})

@login_required
def file_list(request):
    category = request.GET.get('category')
    if category:
        files = UserFile.objects.filter(user=request.user, category=category)
    else:
        files = UserFile.objects.filter(user=request.user)
    return render(request, 'files/file_list.html', {'files': files})

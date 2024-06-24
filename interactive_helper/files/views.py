from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import UserFile
from .google_drive import get_drive_service
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
import os
import magic, psutil, time

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


def create_permission(file_id):
    drive_service = get_drive_service()
    try:
        permission = {
            'type': 'anyone',
            'role': 'reader',
        }
        drive_service.permissions().create(
            fileId=file_id,
            body=permission,
        ).execute()
    except HttpError as error:
        print(f'An error occurred: {error}')


def get_file_download_link(file_id):
    drive_service = get_drive_service()
    request = drive_service.files().get_media(fileId=file_id)
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    return download_url


def delete_file(request, file_id):
    if request.method == 'POST':
        try:
            # Отримання файлу з бази даних
            user_file = UserFile.objects.get(file_id=file_id, user=request.user)

            # Видалення файлу з Google Drive
            drive_service = get_drive_service()
            drive_service.files().delete(fileId=file_id).execute()

            # Видалення файлу з бази даних
            user_file.delete()

            return redirect('files:file_list')
        except UserFile.DoesNotExist:
            return HttpResponseForbidden()
        except HttpError as error:
            print(f'An error occurred: {error}')
            return HttpResponseForbidden()

    return HttpResponseForbidden()

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name

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

            # Надання доступу до файлу
            create_permission(file_id)

            # Збереження інформації про файл у базі даних
            user_file = UserFile(user=request.user, file_name=file_name, file_id=file_id, category=category)
            user_file.save()

            # Видалення файлу з локального сервера після завантаження
            print(file_path,' deleted')
            try:
                # Надання всіх прав доступу до файлу
                os.chmod(file_path, 0o777)
                os.remove(file_path)
                print(f"Файл {file_path} успішно видалено.")
            except FileNotFoundError:
                print(f"Файл {file_path} не знайдено.")
            except PermissionError:
                print(f"Немає дозволу на видалення файлу {file_path}.")
            except Exception as e:
                print(f"Помилка під час видалення файлу {file_path}: {e}")

            return redirect('files:file_list')
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
    for file in files:
        file.download_url = get_file_download_link(file.file_id)
    return render(request, 'files/file_list.html', {'files': files})


"""<ul>
        {% for file in files %}
            <li>
                {{ file.file_name }} - {{ file.category }} - <a href="{{ file.download_url }}" target="_blank">Download</a>
            </li>
        {% endfor %}
    </ul>"""
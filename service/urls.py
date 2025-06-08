from django.urls import path

from service.views import *

urlpatterns = [
    # Generic APIs
    path('Healthcheck', HealthCheck.as_view(), name='healthcheck'),
    
    # Master APIs
    path('Doc/DocumentCategories', DocumentCategoryListView.as_view(), name='document_categories_list'),
    
    # Documents CRUD APIs
    path('Doc/UploadDocument', UploadDocumentView.as_view(), name='upload_document'),
    path('Doc/DownloadDocument', DownloadDocumentView.as_view(), name='download_document'),
    path('Doc/DeleteDocument', DeleteDocumentView.as_view(), name='delete_document'),
    path('Doc/DeleteAllDocument/<int:user_id>', DeleteAllUserDocumentsView.as_view(), name='delete_all_documents_for_user'),
    path('Doc/DocumentList/<int:user_id>', UserDocumentListView.as_view(), name='user_document_list'),
    
    # Conversion APIs
    path('Doc/ConvertDocument', ConvertDocumentView.as_view(), name='convert_document'),
]

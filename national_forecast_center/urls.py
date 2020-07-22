from django.urls import path
from . import views

urlpatterns = [

    #path('', views.dashboard, name='dashboard'),
    path('', views.forecast, name='forecast'),
    path('reportes', views.reports, name='reports'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('upload_docx_file', views.UploadFileView.as_view(), name='upload_docx_file'),

    # CRUD views
    # Create
    path('create_ae/', views.AECreateView.as_view(), name='create_ae'),
    path('create_ni/', views.NICreateView.as_view(), name='create_ni'),
    path('create_pt5/', views.PT5CreateView.as_view(), name='create_pt5'),
    path('create_ptm/', views.PTMCreateView.as_view(), name='create_ptm'),
    path('create_pthoy/', views.PTHOYCreateView.as_view(), name='create_pthoy'),
    path('create_ptrd/', views.PTRDCreateView.as_view(), name='create_ptrd'),
    path('create_ptt/', views.PTTCreateView.as_view(), name='create_ptt'),
    path('create_dp10/', views.DP10CreateView.as_view(), name='create_dp10'),
    path('create_pttn/', views.PTTNCreateView.as_view(), name='create_pttn'),
    path('create_egt/', views.EGTCreateView.as_view(), name='create_egt'),
    path('create_act/', views.ACTCreateView.as_view(), name='create_act'),
    
    # Read
    path('view_ae/<int:pk>', views.AEReadView.as_view(), name='view_ae'),
    path('view_ni/<int:pk>', views.NIReadView.as_view(), name='view_ni'),
    path('view_pt5/<int:pk>', views.PT5ReadView.as_view(), name='view_pt5'),
    path('view_ptm/<int:pk>', views.PTMReadView.as_view(), name='view_ptm'),
    path('view_pthoy/<int:pk>', views.PTHOYReadView.as_view(), name='view_pthoy'),
    path('view_ptrd/<int:pk>', views.PTRDReadView.as_view(), name='view_ptrd'),
    path('view_ptt/<int:pk>', views.PTTReadView.as_view(), name='view_ptt'),
    path('view_dp10/<int:pk>', views.DP10ReadView.as_view(), name='view_dp10'),
    path('view_pttn/<int:pk>', views.PTTNReadView.as_view(), name='view_pttn'),
    path('view_egt/<int:pk>', views.EGTReadView.as_view(), name='view_egt'),
    path('view_act/<int:pk>', views.ACTReadView.as_view(), name='view_act'),

    # Update
    path('update_ae/<int:pk>', views.AEUpdateView.as_view(), name='update_ae'),
    path('update_ni/<int:pk>', views.NIUpdateView.as_view(), name='update_ni'),
    path('update_pt5/<int:pk>', views.PT5UpdateView.as_view(), name='update_pt5'),
    path('update_ptm/<int:pk>', views.PTMUpdateView.as_view(), name='update_ptm'),
    path('update_pthoy/<int:pk>', views.PTHOYUpdateView.as_view(), name='update_pthoy'),
    path('update_ptrd/<int:pk>', views.PTRDUpdateView.as_view(), name='update_ptrd'),
    path('update_ptt/<int:pk>', views.PTTUpdateView.as_view(), name='update_ptt'),
    path('update_dp10/<int:pk>', views.DP10UpdateView.as_view(), name='update_dp10'),
    path('update_pttn/<int:pk>', views.PTTNUpdateView.as_view(), name='update_pttn'),
    path('update_egt/<int:pk>', views.EGTUpdateView.as_view(), name='update_egt'),
    path('update_act/<int:pk>', views.ACTUpdateView.as_view(), name='update_act'),

    # Delete
    path('delete_ae/<int:pk>', views.AEDeleteView.as_view(), name='delete_ae'),
    path('delete_ni/<int:pk>', views.NIDeleteView.as_view(), name='delete_ni'),
    path('delete_pt5/<int:pk>', views.PT5DeleteView.as_view(), name='delete_pt5'),
    path('delete_ptm/<int:pk>', views.PTMDeleteView.as_view(), name='delete_ptm'),
    path('delete_pthoy/<int:pk>', views.PTHOYDeleteView.as_view(), name='delete_pthoy'),
    path('delete_ptrd/<int:pk>', views.PTRDDeleteView.as_view(), name='delete_ptrd'),
    path('delete_ptt/<int:pk>', views.PTTDeleteView.as_view(), name='delete_ptt'),
    path('delete_dp10/<int:pk>', views.DP10DeleteView.as_view(), name='delete_dp10'),
    path('delete_pttn/<int:pk>', views.PTTNDeleteView.as_view(), name='delete_pttn'),
    path('delete_egt/<int:pk>', views.EGTDeleteView.as_view(), name='delete_egt'),
    path('delete_act/<int:pk>', views.ACTDeleteView.as_view(), name='delete_act'),

  
   
]


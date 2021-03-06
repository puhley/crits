from django.conf.urls import patterns

# Dashboard
urlpatterns = patterns('crits.dashboards.views',
    (r'^new_saved_search/$', 'new_save_search'),
    (r'^$', 'dashboard'),
    (r'^id/(?P<dashId>\w+)/$', 'dashboard'),
    (r'^edit_saved_search/(?P<id>\S+)/$', 'edit_save_search'),
    (r'^delete_save_search/$', 'delete_save_search'),
    (r'^load_data/(?P<obj>\w+)/$', 'load_data'),
    (r'^load_data/(?P<obj>\w+)/(?P<term>\w+)/$', 'load_data'),
    (r'^save_search/$', 'save_search'),
    (r'^save_new_dashboard/$', 'save_new_dashboard'),
    (r'^destroy_dashboard/$', 'destroy_dashboard'),
    (r'^get_dashboard_table_data/(?P<tableName>\w+)/$', 'get_dashboard_table_data'),
    (r'^configurations/$', 'saved_searches_list'),
    (r'^toggle_table_visibility/$', 'toggle_table_visibility'),
    (r'^set_default_dashboard/$', 'set_default_dashboard'),
    (r'^set_dashboard_public/$', 'set_dashboard_public'),
    (r'^ignore_parent/(?P<id>\S+)/$', 'ignore_parent'),
    (r'^delete_dashboard/$', 'delete_dashboard'),
    (r'^rename_dashboard/$', 'rename_dashboard'),
    (r'^change_theme/$', 'change_theme'),
    (r'^create_blank_dashboard/$', 'create_blank_dashboard'),
)

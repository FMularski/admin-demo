# Customizing django admin - RPG demo
## 1. custom admin page [feat/1-nav]
admin site as an object - index, reorganizing navigation (get_app_list)
* 1.1 demo/admin_model_nav.py
* 1.2 create custom admin site class in demo/admin.py
* 1.3 create custom admin config in demo/apps.py
* 1.4 replace django.contrib.admin with the custom admin config in demo/settings.py

## 2. Custom presentation of data - list views [feat/2-list-view]
* 2.1 apply list_display, list_editable, readonly_fields, search_fields, list_filter, list_per_page, ordering + get_methods
* 2.2 format_html

## 3. Custom representation of data - change views [feat/3-change-view]
* 3.1 change view - fields, readonly_fields, fieldsets
* 3.2 inlines - model, fields, readonly_fields, max_num, min_num, extra, can_delete, ordering

## 4. Admin actions [feat/4-actions]

## 5. Hooks method [feat/5-hooks]
* 5.1 save_model (character)
* 5.3 delete_model (character)
* 5.2 save_formset (guild)

## 6. Useful packages [feat/6-libs]
* 6.1 admindocs
* 6.2 django-export-import
* 6.3 django-admin-interface

## 7. Applying a custom theme [feat/7-theme]
* 7.1 custom template, staticfiles
* 7.2 commander

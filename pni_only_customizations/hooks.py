# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pni_only_customizations"
app_title = "Pni Only Customizations"
app_publisher = "Jigar Tarpara"
app_description = "PNI Site Only Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "team@khatavahi.in"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = [
	{
		"dt":"Custom Field", 
		"filters": [
			[
				"fieldname", "in", (
					"base_uom_rate"
				)
			]
		]
	}
]
# include js, css files in header of desk.html
# app_include_css = "/assets/pni_only_customizations/css/pni_only_customizations.css"
# app_include_js = "/assets/pni_only_customizations/js/pni_only_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/pni_only_customizations/css/pni_only_customizations.css"
# web_include_js = "/assets/pni_only_customizations/js/pni_only_customizations.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pni_only_customizations.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pni_only_customizations.install.before_install"
# after_install = "pni_only_customizations.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pni_only_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pni_only_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"pni_only_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"pni_only_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pni_only_customizations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pni_only_customizations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pni_only_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pni_only_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pni_only_customizations.task.get_dashboard_data"
# }


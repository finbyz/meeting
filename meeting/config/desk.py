# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {       
        	"label": _("Tools"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Meeting",
                    "label": _("Meeting"),
                    "description": _("Arrange meetings within Organisation"),
                    "onboard": 1,
       	},
			]
		},
        {       
        	"label": _("Tools"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Meeting",
                    "label": _("MyFirstDocType"),
                    "description": _("To arrange meetings within Organisation"),
                    "onboard": 1,
       	},
			]
		}
	]
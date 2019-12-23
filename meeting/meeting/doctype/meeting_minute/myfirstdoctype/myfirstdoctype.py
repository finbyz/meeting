# -*- coding: utf-8 -*-
# Copyright (c) 2019, shivani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MyFirstDocType(Document):
	def validate(self):
		for attendee in self.attendees:
			if not attendee.full_name:
				user = frappe.get_doc("User", attendee.attendee)
				attendee.full_name = " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))

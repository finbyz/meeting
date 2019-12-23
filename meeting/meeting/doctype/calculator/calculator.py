# -*- coding: utf-8 -*-
# Copyright (c) 2019, shivani and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Calculator(Document):
	def validate(self):
		self.amount = self.rate * self.quantity

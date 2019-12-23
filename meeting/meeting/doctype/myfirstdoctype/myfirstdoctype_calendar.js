frappe.views.calendar["MyFirstDocType"] = {
	field_map: {
		"start": "start",
		"end": "end",
		"id": "name",
		"title": "title",
		"status": "status",
		"allDay": "all_day",
	},
	get_events_method: "meeting.api2.get_meetings"
}
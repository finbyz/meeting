frappe.ui.form.on("MyFirstDocType", {
	send_emails: function(frm) {
		if(frm.doc.status === "Planned") {
			frappe.call({
				method: "meeting.api2.send_invitation_emails",
				args: {
					meeting: frm.doc.name
				}
			});
		}
		else {
			alert("Meeting Status must be 'Planned'");
		}
	},
});

frappe.ui.form.on("Meeting Attendee 2", {
    attendee: function(frm, cdt, cdn) {
        var attendee = frappe.model.get_doc(cdt, cdn);
        
        if (attendee.attendee)
        // if attendee, get full name
        {
            frm.call({
                method: "meeting.meeting.doctype.myfirstdoctype.myfirstdoctype.get_full_name",
                args: {
                    attendee: attendee.attendee
                },
                callback: function(r) {
                    frappe.model.set_value(cdt, cdn, "full_name", r.message);
                }
            });

            console.log(frm.fields_dict);
        }
        else
        // if no attendee, clear the full name
        {
            frappe.model.set_value(cdt, cdn, "full_name", null);
        }

    }
     

});
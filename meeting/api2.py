import frappe
from frappe import _
from frappe.utils import add_days, nowdate

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("MyFirstDocType", meeting)
    meeting.check_permission("email")

    if meeting.status == "Planned":
        frappe.sendmail(
            recipients = [d.attendee for d in meeting.attendees],
            sender = frappe.session.user,
            subject = meeting.title,
            message = meeting.invitation_message,
            reference_doctype = meeting.doctype,
            reference_name = meeting.name
        )
        meeting.status = "Invitation Sent"
        meeting.save()

        frappe.msgprint(_("Invitation Sent."))

    else:
        frappe.msgprint(_("Meeting Status must be 'Planned'"))

@frappe.whitelist()
def get_meetings(start="11-11-2019", end="12-11-2019"):
    if not frappe.has_permission("MyFirstDocType", "read"):
        raise frappe.PermissionError
    return frappe.db.sql("""
        select timestamp(`date`, from_time) as start,
        timestamp(`date`, to_time) as end,
        name,
        title,
        status,
        0 as all_day
        from `tabMyFirstDocType`
        where `date` between %(start)s and %(end)s""", {
            "start": start,
            "end": end
        }, as_dict = True
    )

def make_orientation_meeting(doc, method):
    """Scheduling an orientation meeting for those who just joins"""
    myfirstdoctype = frappe.get_doc({
        "doctype": "MyFirstDocType",
        "title": "Orientation for {0}".format(doc.first_name),
        "date": add_days(nowdate(), 1),
        "from_time": "10:00",
        "to_time": "10:30",
        "status": "Planned",
        "attendees": [{
            "attendee": doc.name
        }]
    })
    # to ignore the permission bcoz current user might not have permission to create the meetings
    myfirstdoctype.flags.ignore_permissions = True
    myfirstdoctype.insert()
    frappe.msgprint(_("Orientation eeting has been scheduled for {0}").format(doc.first_name))
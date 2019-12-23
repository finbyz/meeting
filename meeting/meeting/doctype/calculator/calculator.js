// Copyright (c) 2019, shivani and contributors
// For license information, please see license.txt
frappe.ui.form.on('Calculator', {
	// refresh(frm) {
	// 	d.show();
	// },
	rate: function(frp) {
		if (frp.doc.quantity > 0)
		{
			let amt = frp.doc.rate * frp.doc.quantity;
			frp.set_value('amount', amt);
		}
		else
		{
			frp.set_value('amount', 0);
		}
	},
	quantity: function(frp) {
		if (frp.doc.rate > 0)
		{
			let amt = frp.doc.rate * frp.doc.quantity;
			frp.set_value('amount', amt);
		}
		else
		{
			frp.set_value('amount', 0);
		}
	}
});


// let d = new frappe.ui.Dialog({
//     title: 'Enter details',
//     fields: [
//         {
//             label: 'First Name',
//             fieldname: 'first_name',
//             fieldtype: 'Data'
//         },
//         {
//             label: 'Last Name',
//             fieldname: 'last_name',
//             fieldtype: 'Data'
//         },
//         {
//             label: 'Age',
//             fieldname: 'age',
//             fieldtype: 'Int'
//         }
//     ],
//     primary_action_label: 'Submit',
//     primary_action(values) {
//         console.log(values);
//         d.hide();
//     }
// });
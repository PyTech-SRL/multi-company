# © 2023 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo.addons.base.tests.common import BaseCommon


class Test(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner_view = cls.env.ref("base.view_partner_form")

    def test_class_company(self):
        arch, view = self.env["res.partner"]._get_view(view_id=self.partner_view.id)
        for field in arch.xpath("//field[@name='barcode']"):
            self.assertIn("building", field.attrib.get("class"))

======================
Odoo Product Write Bug
======================

**Author**
**********
* BizzAppDev Systems Pvt. Ltd.

**Installation**
****************
* Under applications, the application odoo_product_write_bug can be installed/uninstalled.

**Issue**
*********
* When try to update more than one fields at product variant level then field's values get false.
* https://drive.google.com/file/d/1TJDz82wrWP2Lz-aavDlQaru-4fON9lXN/view

**Description**
***************
* Technical explanation:
    - We have inherited write() method of product.template and tried to write values in the product.pricelist.item from the product.template's write() method.

* Steps to Reproduce an issue:
    - Create a new product variant(product.product) and save it.
    - Edit newly created product, update Income Account and Expense Account field at the same time.
    - Save the records, after saving Expense Account field get false.

**Configuration**
*****************
* #N/A

**Known issues/Roadmap**
************************
* #N/A

**Changelog**
*************
* 22/09/2021 - Created new module.

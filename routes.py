from flask import Blueprint
from controller.CustomerController import getAllCustomer, registerCustomer, loginCustomer
from controller.StaffController import getAllStaff, registerStaff, loginStaff
from controller.EbookController import deleteEbookByID, getAllEbook, getEbookByID, editEbookByID, addEbook, deleteEbookByID, getAllEbook2, getEbookByID2
from controller.OrdersController import getAllOrders



route_bp = Blueprint('route_bp', __name__)

# CUSTOMER
route_bp.route('/user/register', methods=['POST'])(registerCustomer)
route_bp.route('/user/All', methods=['GET'])(getAllCustomer)
route_bp.route('/user/login', methods=['POST'])(loginCustomer)


# STAFF
route_bp.route('/admin/register', methods=['POST'])(registerStaff)
route_bp.route('/admin/All', methods=['GET'])(getAllStaff)
route_bp.route('/admin/login', methods=['POST'])(loginStaff)

route_bp.route('/admin/ebook/', methods=['GET'])(getAllEbook)
route_bp.route('/admin/ebook/', methods=['POST'])(addEbook)
route_bp.route('/admin/ebook/<id>', methods=['GET'])(getEbookByID)
route_bp.route('/admin/ebook/<id>', methods=['PUT'])(editEbookByID)
route_bp.route('/admin/ebook/<id>', methods=['DELETE'])(deleteEbookByID)


# EBOOK
route_bp.route('/ebook/', methods=['GET'])(getAllEbook2)
route_bp.route('/ebook/<id>', methods=['GET'])(getEbookByID2)

# ORDERS
route_bp.route('/ebook/All', methods=['GET'])(getAllOrders)



from flask import Flask,request,render_template,redirect,jsonify
from controller.customer_controller import CustomerController
from controller.order_controller import OrderController
from controller.tailor_controller import TailorController
from controller.clothes_controller import ClothesController

app = Flask(__name__,template_folder="view", static_folder="view/assets")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customer", methods=["GET", "POST", "DELETE"])
def customer():
    if request.method == "GET":
        return render_template("customer.html", customer_list=CustomerController.find_all())

    elif request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        phone = request.form.get("phone")
        email = request.form.get("email")
        national_id = request.form.get("national_id")
        birth_date = request.form.get("birth_date")
        status, message = CustomerController.save(name, family, phone, email, national_id, birth_date)
        return render_template("customer.html", customer_list=CustomerController.find_all())

    elif request.method == "DELETE":
        id = int(request.args.get("id"))
        CustomerController.remove(id)
        return render_template("customer.html", customer_list=CustomerController.find_all())


@app.route("/order", methods=["GET", "POST", "DELETE"])
def order():
    if request.method == "GET":
        return render_template("order.html", order_list=OrderController.find_all())

    elif request.method == "POST":
        order_date = request.form.get("order_date")
        delivery_date = request.form.get("delivery_date")
        status = request.form.get("status")
        customer_id = request.form.get("customer_id")
        tailor_id = request.form.get("tailor_id")
        clothes_id = request.form.get("clothes_id")
        status, message = OrderController.save(order_date, delivery_date, status, customer_id, tailor_id, clothes_id)
        return render_template("order.html", order_list=OrderController.find_all())

    elif request.method == "DELETE":
        id = int(request.args.get("id"))
        OrderController.remove(id)
        return render_template("order_view.html", order_list=OrderController.find_all())


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tailor", methods=["GET", "POST", "DELETE"])
def tailor():
    if request.method == "GET":
        return render_template("tailor.html", tailor_list=TailorController.find_all())

    elif request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        phone = request.form.get("phone")
        salary = request.form.get("salary")
        national_id = request.form.get("national_id")
        birth_date = request.form.get("birth_date")
        status = request.form.get("status")
        status, message = CustomerController.save(name,family,phone,salary,national_id,birth_date,status)
        return render_template("tailor.html", tailor_list=TailorController.find_all())

    elif request.method == "DELETE":
        id = int(request.args.get("id"))
        TailorController.remove(id)
        return render_template("tailor.html", tailor_list=TailorController.find_all())

@app.route("/clothes", methods=["GET", "POST", "DELETE"])
def clothes():
    if request.method == "GET":
        return render_template("clothes.html", clothes_list=ClothesController.find_all())

    elif request.method == "POST":
        name_clothes = request.form.get("name_clothes")
        fabric = request.form.get("fabric")
        color = request.form.get("color")
        price = request.form.get("price")
        size = request.form.get("size")
        description = request.form.get("description")
        status, message = ClothesController.save(name_clothes, fabric, color, price, size, description)
        return render_template("clothes_view.html", clothes_list=ClothesController.find_all())

    elif request.method == "DELETE":
        id = int(request.args.get("id"))
        ClothesController.remove(id)
        return render_template("clothes_view.html", clothes_list=ClothesController.find_all())



@app.route("/api")
def api():
    return f"{jsonify(CustomerController.find_all()[1])}"
    return f"{jsonify(OrderController.find_all()[1])}"
    return f"{jsonify(TailorController.find_all()[1])}"
    return f"{jsonify(ClothesController.find_all()[1])}"


app.run(host="192.168.39.100", port=80, debug=True)
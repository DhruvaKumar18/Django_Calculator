# calculator/views.py

from django.shortcuts import render

def home(request):
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "+":
                result = num1 + num2

            elif operation == "-":
                result = num1 - num2

            elif operation == "*":
                result = num1 * num2

            elif operation == "/":
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2

        except:
            result = "Invalid Input"

    return render(request, "home.html", {"result": result})
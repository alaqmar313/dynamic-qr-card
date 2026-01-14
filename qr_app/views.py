from django.shortcuts import render, get_object_or_404
from .models import Card
import qrcode
import base64
from io import BytesIO

def home(request):
    qr_code = None
    card = None

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        company = request.POST.get("company")
        address = request.POST.get("address")

        card = Card.objects.create(
            name=name,
            phone=phone,
            email=email,
            company=company,
            address=address
        )

        qr_url = request.build_absolute_uri(f"/card/{card.id}/")

        qr = qrcode.make(qr_url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "qr_app/home.html", {
        "qr_code": qr_code,
        "card": card
    })


def view_card(request, id):
    card = get_object_or_404(Card, id=id)
    return render(request, "qr_app/card.html", {"card": card})

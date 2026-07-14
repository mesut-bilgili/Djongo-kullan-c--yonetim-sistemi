from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages  # Uyarı mesajları için ekledik
from .models import Person

# ReportLab bileşenleri
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Türkçe karakter desteği için Arial fontunu kaydediyoruz
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

# 1. HOME VIEW (TC Kontrolü ve Mesaj Sistemi Eklendi)
def home(request):
    if request.method == "POST":
        person_id = request.POST.get("person_id")
        tc_number = request.POST.get("tc_number")

        # --- ÇİFT KAYIT (TC) KONTROLÜ ---
        # Eğer güncelleme yapıyorsak kendisi hariç, yeni kayıt yapıyorsak tüm veritabanında bu TC var mı kontrol et
        tc_kontrol = Person.objects.filter(tc_number=tc_number)
        if person_id:
            tc_kontrol = tc_kontrol.exclude(id=person_id)

        if tc_kontrol.exists():
            messages.error(request, f"{tc_number} TC kimlik numarasıyla kayıtlı bir kişi zaten sistemde mevcut!")
            return redirect("home")
        # --------------------------------

        if person_id:
            # --- GÜNCELLEME İŞLEMİ ---
            person = get_object_or_404(Person, id=person_id)
            person.first_name = request.POST.get("first_name")
            person.last_name = request.POST.get("last_name")
            person.tc_number = tc_number
            person.gender = request.POST.get("gender")
            person.phone = request.POST.get("phone")
            person.email = request.POST.get("email")
            person.note = request.POST.get("note")
            
            if request.FILES.get("photo"):
                person.photo = request.FILES.get("photo")
                
            person.save()
            messages.success(request, "Kayıt başarıyla güncellendi.")
        else:
            # --- YENİ KAYIT ---
            Person.objects.create(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                tc_number=tc_number,
                gender=request.POST.get("gender"),
                phone=request.POST.get("phone"),
                email=request.POST.get("email"),
                note=request.POST.get("note"),
                photo=request.FILES.get("photo")
            )
            messages.success(request, "Kayıt başarıyla oluşturuldu.")
            
        return redirect("home")

    persons = Person.objects.all()
    return render(request, "tasks/home.html", {"persons": persons})


# 2. GENERATE PDF VIEW
def generate_pdf(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{person.first_name}.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)

    # Başlık
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(180, 800, "PERSON INFORMATION")

    # Bilgiler (Türkçe karakterlerin çıkması için Arial yapıyoruz)
    pdf.setFont("Arial", 12)
    pdf.drawString(70, 740, f"Name      : {person.first_name}")
    pdf.drawString(70, 720, f"Surname   : {person.last_name}")
    pdf.drawString(70, 700, f"TC Number : {person.tc_number}")
    pdf.drawString(70, 680, f"Gender    : {person.gender}")
    pdf.drawString(70, 660, f"Phone     : {person.phone}")
    pdf.drawString(70, 640, f"E-mail    : {person.email}")
    pdf.drawString(70, 620, f"Note      : {person.note}")

    # Görsel Çizdirme Alanı
    if person.photo and hasattr(person.photo, 'path'):
        try:
            pdf.drawImage(person.photo.path, 420, 610, width=120, height=150)
        except Exception as e:
            pdf.drawString(420, 740, "[Fotoğraf Yüklenemedi]")

    pdf.save()
    return response
# Asosiy obrazni tanlash
FROM python:3.12

# Ishlayotgan direktoriya
WORKDIR /app

# Lokal fayllarni obrazga ko'chirish
COPY . /app

# Python paketlarini o'rnatish
RUN pip install -r requirements.txt

# Port ochish
EXPOSE 8000

# Serverni ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

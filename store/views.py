from django.shortcuts import render

# Create your views here.
def home(request):
    page_title = "Homepage"

    happy_customers = [
        {
            "name": "Mubarak Adebanjo",
            "content": "Can't express how much satisfaction i gained from trading with Techie Health.",
            "avatar": "images/person_2.jpg"
        },
        {
            "name": "Abdul Malik Diyaolu",
            "content": "I really love their services. Recommended for good customer relationship :)",
            "avatar": "images/person_3.jpg"
        },
        {
            "name": "Abdul Mateen Jolaosho",
            "content": "Omor, Nice service. Closeness to customer. Really recommendable.",
            "avatar": "images/person_1.jpg"
        }
    ]

    why_us = [
        {
            "number": 1,
            "content": "Extra fast service delivery",
        },
        {
            "number": 2,
            "content": "Reliable customer services",
        },
        {
            "number": 3,
            "content": "Proffesionalism is core",
        },
        {
            "number": 4,
            "content": "Free delivery for drugs above #5000",
        },
    ]

    home_slider = [
        {
            "image": "images/hero_bg4.jpg",
            "title": "Techie Health",
            "subtitle": "We are a family of medical and health care providers",
            "link": "https://techiehealth.com",
            "link_topic": "home"
        },
        {
            "image": "images/hero_bg_2.jpg",
            "title": "<strong class='text-brown'>TECHIEHEALTH</strong> Opens 24 Hours",
            "subtitle": "We are a family of medical and health care providers",
            "link": "https://techiehealth.com",
            "link_topic": "home"
        },
        {
            "image": "images/hero_bg3.jpg",
            "title": "New Medicine <strong class='text-brown'>Everyday</strong>",
            "subtitle": "We Stock our store nearly everyday. You can always get what you want.",
            "link": "https://techiehealth.com",
            "link_topic": "home"
        },
    ]

    context = {
        "page_title": page_title,
        "products": [1, 2, 3, 4, 5],
        "testimonials": happy_customers,
        "why_us": why_us,
        "home_slider": home_slider,
    }
    return render(request, 'store/home.html', context=context)

def about(request):
    page_title = "About us"

    upper = [
        {
            "title": "Why Us",
            "content": "We provide you with quality services you can ever imagine.",
        },
        {
            "title": "History",
            "content": "Built on true values, Techie Health Ng was estabished to solve not just drug delivery issues but also common clinnical resposibilities.",
        },
        {
            "title": "Awards",
            "content": "Proffesionalism is core",
        }
    ]

    leaders = [
        {
            "name": "Ayobami Diyaolu",
            "content": "An hardworking youthful Nigerian with strong believe and supporrt for Anti-Microbial awearness.",
            "avatar": "images/person_2.jpg",
            "title": "CEO/Co-Founder"
        },
        {
            "name": "Basirat Diyaolu",
            "content": "A loving and caring Mum. Mother of two. Librarian.",
            "avatar": "images/person_3.jpg",
            "title": "Co-Founder"
        },
        {
            "name": "Name Unknown",
            "content": "Sales is the drive.",
            "avatar": "images/person_1.jpg",
            "title": "Phamascist"
        }
    ]

    context = {
        "page_title": page_title,
        "upper": upper,
        "leaders": leaders,
    }
    return render(request, 'store/about.html', context=context)

def contact(request):
    page_title = "Contact Us"


    context = {
        "page_title": page_title,
    }
    return render(request, 'store/contact.html', context=context)
from apis import views


api_urls = [
    ("/", views.index, "flask scaffolding index url")
]

other_urls = []

all_urls = api_urls + other_urls

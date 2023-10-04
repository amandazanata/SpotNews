{% extends "base.html" %}
{% load static %}
{% block title %}Página de Detalhes da Notícia{% endblock %}
{% block main %}
    <div class="news-details">
        <h1 class="news-title">{{ details.title }}</h1>
        <p class="news-content">{{ details.content }}</p>
        <section>
            {% for category in details.categories.all %}<span class="news-categories">{{ category }}</span>{% endfor %}
        </section>
        <span class="news-author">{{ details.author }}</span>
        <img src="{% static details.image %}" alt="image of {{ details.title }}">
        <span>{{ details.created_at|date:"d/m/Y" }}</span>
    </div>
{% endblock %}
```

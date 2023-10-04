{% extends "base.html" %}
{% load static %}
{% block title %}Formulário para Nova Notícia{% endblock %}
{% block main %}
    <h1>Fomulário para Nova Categoria</h1>
    <form action="{% url 'news-form' %}"
          method="post"
          enctype="multipart/form-data">
        {% csrf_token %}
        <label for="{{ form.title.id_for_label }}">Título</label>
        {{ form.title }}
        <label for="{{ form.content.id_for_label }}">Conteúdo</label>
        {{ form.content }}
        <label for="{{ form.author.id_for_label }}">Autoria</label>
        {{ form.author }}
        <label for="{{ form.created_at.id_for_label }}">Criado em</label>
        {{ form.created_at }}
        <label for="{{ form.image.id_for_label }}">URL da Imagem</label>
        {{ form.image }}
        {{ form.categories }}
  <button type="submit">Salvar</button>
    </form>
{% endblock %}
```

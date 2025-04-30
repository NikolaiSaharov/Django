from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Platform(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Название платформы")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Платформа"
        verbose_name_plural = "Платформы"

class Game(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Название игры")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='games/', blank=True, null=True, verbose_name="Изображение")
    categories = models.ManyToManyField(Category, related_name='games', verbose_name="Категории")
    platforms = models.ManyToManyField(Platform, related_name='games', verbose_name="Платформы")
    release_date = models.DateField(verbose_name="Дата выпуска")
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True, blank=True, related_name='games', verbose_name="Разработчик")
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True, related_name='games', verbose_name="Издатель")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class Developer(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Название разработчика")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    logo = models.ImageField(upload_to='developers/', blank=True, null=True, verbose_name="Логотип")
    founded_date = models.DateField(verbose_name="Дата основания")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"

class Publisher(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Название издателя")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    logo = models.ImageField(upload_to='publishers/', blank=True, null=True, verbose_name="Логотип")
    founded_date = models.DateField(verbose_name="Дата основания")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews', verbose_name="Игра")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name="Пользователь")
    rating = models.IntegerField(verbose_name="Рейтинг (1-10)", choices=[(i, str(i)) for i in range(1, 11)])
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отзыв от {self.user.username} на {self.game.title}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Пользователь")
    games = models.ManyToManyField(Game, related_name='orders', verbose_name="Игры")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=MAX_LENGTH, choices=[
        ('pending', 'Ожидает'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен')
    ], default='pending', verbose_name="Статус")

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist', verbose_name="Пользователь")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='wishlist', verbose_name="Игра")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.user.username} добавил {self.game.title} в список желаемого"
    
    class Meta:
        verbose_name = "Список желаемого"
        verbose_name_plural = "Списки желаемого"
        unique_together = ('user', 'game')
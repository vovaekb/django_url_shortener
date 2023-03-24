from django.db import models

class VisitStatistics(models.Model):
    """Model definition for VisitStatistics."""
    total_visits = models.IntegerField()

    def __str__(self):
        """Unicode representation of VisitStatistics."""
        pass


class Link(models.Model):
    """Model definition for Link."""
    full_url = models.CharField(max_length=256)
    slug = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    statistics = models.OneToOneField(VisitStatistics, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Link."""
        return self.name


class Visit(models.Model):
    """Model definition for Visit."""
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    ip_address = models.CharField(max_length=50)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Visit."""
        pass


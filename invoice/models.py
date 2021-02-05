from django.db import models


class Company(models.Model):
    """ Model representing a company. """

    name = models.CharField(max_length=255)
    company_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'


class Invoice(models.Model):
    """ Model representing an invoice. """

    internal_reference = models.CharField(max_length=36, unique=True)
    gross_amount = models.DecimalField("Total Invoice Amount",
                                       decimal_places=2,
                                       max_digits=20,
                                       blank=True, null=True, default=0)
    supplier_reference = models.CharField(max_length=36)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'invoice'

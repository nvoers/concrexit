from rest_framework import serializers

from partners.models import Vacancy
from .vacancy_category import VacancyCategorySerializer


class VacancySerializer(serializers.ModelSerializer):
    """Vacancy serializer."""

    class Meta:
        """Meta class for vacancy serializer."""

        model = Vacancy
        fields = (
            "pk",
            "title",
            "description",
            "location",
            "keywords",
            "link",
            "partner",
            "company_name",
            "company_logo",
            "categories",
        )

    categories = VacancyCategorySerializer(many=True)

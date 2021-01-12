from college.models import College
from reviews.models import Review


class IngestionEngine:

    def __init__(self):
        self.college = None
        self.scraping_source = None

    def declare_college(self, college_uuid):
        self.college = College.objects.get(uuid=college_uuid)

    def declare_scraping_source(self, source):
        self.scraping_source = source

    def ingest(self, college_json):
        self.declare_college(college_json['college_uuid'])
        self.declare_scraping_source(college_json['source'])
        review_objs = []
        for _, review in college_json['reviews'].items():
            review_obj = self.create_review_object(review)
            if review_obj:
                review_objs.append(
                    review_obj
                )
        Review.objects.bulk_create(review_objs)

    def create_review_object(self, review):
        review_text = review.get('review')
        if not self.check_if_already_exists(review_text):
            return Review(
                college=self.college,
                comment=review_text,
                source=self.scraping_source,
                name=review.get('name')
            )

    @staticmethod
    def check_if_already_exists(review_comment):
        return Review.objects.filter(comment=review_comment).exists()

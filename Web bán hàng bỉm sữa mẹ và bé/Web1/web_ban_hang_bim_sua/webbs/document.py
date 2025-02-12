from elasticsearch_dsl import Document, Text, Date, Float
from elasticsearch_dsl.connections import connections
from .models import Course

# Define Elasticsearch connection
# connections.create_connection(hosts=['http://localhost:9200/'])
connections.create_connection(hosts=['http://elasticsearch:9200'])
class DanhMucDocument(Document):
    name = Text()
    description = Text()
    year = Float()
    startDate = Date()
    endDate = Date()
    class Index:
        name = 'courses'  # Elasticsearch index name
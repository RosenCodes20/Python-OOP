class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category.edit(new_name)

    def edit_topic(self, topic_id, new_name, new_storage_folder):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        topic.edit(new_name, new_storage_folder)

    def edit_document(self, document_id, new_name):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        document.edit(new_name)

    def delete_category(self, category_id):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(document)

    def get_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        return str(document)

    def __repr__(self):
        result = [*[str(d) for d in self.documents]]
        return "\n".join(map(str, result))
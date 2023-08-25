import uuid
from django.db import models

class Notes(models.Model):
    noteId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userName = models.CharField(max_length=65)
    color = models.CharField(max_length=50, default="GREY")
    isTrashed = models.BooleanField(default=False)
    isPinned = models.BooleanField(default=False)
    isArchived = models.BooleanField(default=False)
    textContent = models.CharField(max_length=1000)
    title = models.CharField(max_length=60)
    userEditedTimestamp = models.DateTimeField(auto_now=True)
    createdTimestamp = models.DateTimeField(auto_now_add=True)
    labels = models.CharField(max_length=50, default="personal")

    class Meta:
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title

    def archive(self):
        self.isArchived = True
        self.save()

    def unarchive(self):
        self.isArchived = False
        self.save()

    def trash(self):
        self.isTrashed = True
        self.save()

    def untrash(self):
        self.isTrashed = False
        self.save()

    def pin(self):
        self.isPinned = True
        self.save()

    def unpin(self):
        self.isPinned = False
        self.save()

    def add_label(self, label):
        if label not in self.labels.split(', '):
            if self.labels:
                self.labels += f', {label}'
            else:
                self.labels = label
            self.save()

    def remove_label(self, label):
        labels_list = self.labels.split(', ')
        if label in labels_list:
            labels_list.remove(label)
            self.labels = ', '.join(labels_list)
            self.save()

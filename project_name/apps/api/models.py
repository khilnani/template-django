from django.db import models
import os

class UploadFile(models.Model):
    data = models.FileField(upload_to='uploaded_files/')

    def save(self, *args, **kwargs):
        filepath, filename = os.path.split(self.data.name)
        filecontent = self.data.read()

        print( filecontent )

        super(UploadFile, self).save(*args, **kwargs)
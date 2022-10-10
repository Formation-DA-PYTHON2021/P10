from django.db import models


TYPES = [
    ('BACKEND', 'BACKEND'),
    ('FRONTEND', 'FRONTEND'),
    ('iOS', 'iOS'),
    ('ANDROID', 'ANDROID')
]

PRIORITIES = [
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGH', 'HIGH')
]

TAGS = [
    ('BUG', 'BUG'),
    ('TASK', 'TASK'),
    ('UPGRADE', 'UPGRADE')
]

STATUSES = [
    ('TODO', 'TODO'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('DONE', 'DONE')
]

ROLES = [
    ('AUTHOR', 'AUTHOR'),
    ('CONTRIBUTOR', 'CONTRIBUTOR')
]

PERMISSIONS = [
    ('CREATE', 'CREATE'),
    ('READ', 'READ'),
    ('UPDATE', 'UPDATE'),
    ('DELETE', 'DELETE')
]


class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    project_id = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=8, choices=TYPES)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    contributor_id = models.IntegerField()
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=6, choices=PERMISSIONS, default='CREATE')
    role = models.CharField(max_length=11, choices=ROLES, default='CONTRIBUTOR')

    def __str__(self):
        return self.user_id


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=2048)
    tag = models.CharField(max_length=7, choices=TAGS)
    priority = models.CharField(max_length=6, choices=PRIORITIES)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=STATUSES, default='TODO')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_id = models.IntegerField()
    description = models.CharField(max_length=2048)
    author_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

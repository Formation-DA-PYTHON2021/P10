from django.db import models
from django.conf import settings

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
    ('ALL', 'ALL'),
    ('RESTRICT', 'RESTRICT')
]


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=8, choices=TYPES)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='author')

    def __str__(self):
        return f'id: {self.id} - projet : {self.title}'


class Contributor(models.Model):
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, )
    permission = models.CharField(max_length=8, choices=PERMISSIONS)
    role = models.CharField(max_length=11,
                            choices=ROLES,
                            default='CONTRIBUTOR')

    def __str__(self):
        return str(f'user: {self.user_id} '
                   f'- id project: {self.project_id.id} '
                   f'- role: {self.role}')


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=2048)
    tag = models.CharField(max_length=7, choices=TAGS)
    priority = models.CharField(max_length=6, choices=PRIORITIES)
    status = models.CharField(max_length=11, choices=STATUSES, default='TODO')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=Contributor,
                                         on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=2048)
    author_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models
# from django.utils import timezone


class Rubric(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL,
                               null=True)
    rubric_name = models.CharField(_('Rubric name'), max_length=255)
    insert_date = models.DateTimeField(_('Insert Date'), auto_now_add=True)
    update_date = models.DateTimeField(_('Update Date'), auto_now=True)

    def __str__(self):
        return self.rubric_name


class ArticleManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(status=Article.PUBLISHED)

    def drafted(self):
        return self.get_queryset().filter(status=Article.DRAFT)

    def archived(self):
        return self.get_queryset().filter(status=Article.ARCHIVED)


def generate_filename(instance, filename):  # for generate comprehensible file name
    filename = instance.title + '.jpg'
    return '{0}/{1}'.format(instance, filename)


class Article(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    ARCHIVED = 3

    objects = ArticleManager()

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL,
                               null=True)
    rubric = models.ForeignKey('articles.Rubric', related_name='articles',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    title = models.CharField(_('Article Title'), max_length=255)
    slug = models.CharField(_('Slug'), max_length=255, help_text=_(
        'For SEO'
    ))

    content = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to=generate_filename, null=True, blank=True)

    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    status = models.PositiveSmallIntegerField(_('Status'),
                                              db_index=True,
                                              choices=(
                                                  (DRAFT, _('Draft')),
                                                  (PUBLISHED, _('Published')),
                                                  (ARCHIVED, _('Archived'))
                                              ), default=DRAFT)
    published_at = models.DateTimeField(
        _('Published At'),
        auto_now_add=False, auto_now=False, null=True, blank=True)

    likes = models.PositiveIntegerField(default=0)

    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

        indexes = [
            models.Index(fields=['author', 'status'], name='author_status_idx')
        ]
        ordering = ('-created_at',)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    article = models.ForeignKey('articles.Article',
                                related_name='comments',
                                on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approved(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
        # return '{} -> [{}]'.format(self.author.username, self.article)

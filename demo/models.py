from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailsearch import index


# ABSTRACT MODELS
# =============================

class AbstractLinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class AbstractRelatedLink(AbstractLinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(AbstractLinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class AbstractCarouselItem(AbstractLinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(AbstractLinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class ContactFieldsMixin(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True


# PAGE MODELS
# =============================

# Home page

class HomePage(Page):
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    class Meta:
        verbose_name = "Homepage"


class HomePageCarouselItem(Orderable, AbstractCarouselItem):
    page = ParentalKey('HomePage', related_name='carousel_items')

class HomePageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('HomePage', related_name='related_links')

HomePage.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),

    InlinePanel(HomePage, 'carousel_items', label="Carousel items"),
    InlinePanel(HomePage, 'related_links', label="Related links"),
]


# Standard pages

class StandardPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

class StandardPageCarouselItem(Orderable, AbstractCarouselItem):
    page = ParentalKey('StandardPage', related_name='carousel_items')

class StandardPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('StandardPage', related_name='related_links')

StandardPage.content_panels = Page.content_panels + [
    FieldPanel('intro', classname="full"),
    InlinePanel(StandardPage, 'carousel_items', label="Carousel items"),
    FieldPanel('body', classname="full"),
    InlinePanel(StandardPage, 'related_links', label="Related links"),
]

StandardPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]


class StandardIndexPage(Page):
    intro = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

class StandardIndexPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('StandardIndexPage', related_name='related_links')

StandardIndexPage.content_panels = Page.content_panels + [
    FieldPanel('intro', classname="full"),
    InlinePanel(StandardIndexPage, 'related_links', label="Related links"),
]

StandardIndexPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]


# Blog pages

class BlogPage(Page):
    body = RichTextField()
    tags = ClusterTaggableManager(through='BlogPageTag', blank=True)
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    def get_blog_index(self):
        # Find closest ancestor which is a blog index
        return BlogIndexPage.ancestor_of(self).last()

class BlogPageCarouselItem(Orderable, AbstractCarouselItem):
    page = ParentalKey('BlogPage', related_name='carousel_items')

class BlogPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('BlogPage', related_name='related_links')

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')

BlogPage.content_panels = Page.content_panels + [
    FieldPanel('date'),
    FieldPanel('body', classname="full"),
    InlinePanel(BlogPage, 'carousel_items', label="Carousel items"),
    InlinePanel(BlogPage, 'related_links', label="Related links"),
]

BlogPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
    FieldPanel('tags'),
]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    def get_blog_entries(self):
        # Get list of live blog pages that are descendants of this page
        entries = BlogPage.objects.descendant_of(self).live()

        # Order by most recent date first
        entries = entries.order_by('-date')

        return entries

    def get_context(self, request):
        # Get blog entries
        entries = self.get_blog_entries()

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            entries = entries.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(entries, 10)  # Show 10 entries per page
        try:
            entries = paginator.page(page)
        except PageNotAnInteger:
            entries = paginator.page(1)
        except EmptyPage:
            entries = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['entries'] = entries
        return context

class BlogIndexPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('BlogIndexPage', related_name='related_links')

BlogIndexPage.content_panels = Page.content_panels + [
    FieldPanel('intro', classname="full"),
    InlinePanel(BlogIndexPage, 'related_links', label="Related links"),
]


# Events pages

class EventPage(Page):
    AUDIENCE_CHOICES = (
        ('public', "Public"),
        ('private', "Private"),
    )

    date_from = models.DateField("Start date")
    date_to = models.DateField(
        "End date",
        null=True,
        blank=True,
        help_text="Not required if event is on a single day"
    )
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)
    audience = models.CharField(max_length=255, choices=AUDIENCE_CHOICES)
    location = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    cost = models.CharField(max_length=255)
    signup_link = models.URLField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('get_audience_display'),
        index.SearchField('location'),
        index.SearchField('body'),
    )

    def get_event_index(self):
        # Find closest ancestor which is an event index
        return EventIndexPage.objects.ancester_of(self).last()

class EventPageCarouselItem(Orderable, AbstractCarouselItem):
    page = ParentalKey('EventPage', related_name='carousel_items')

class EventPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('EventPage', related_name='related_links')

class EventPageSpeaker(Orderable, AbstractLinkFields):
    page = ParentalKey('EventPage', related_name='speakers')
    first_name = models.CharField("Name", max_length=255, blank=True)
    last_name = models.CharField("Surname", max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def name_display(self):
        return self.first_name + " " + self.last_name

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        ImageChooserPanel('image'),
        MultiFieldPanel(AbstractLinkFields.panels, "Link"),
    ]

EventPage.content_panels = Page.content_panels + [
    FieldPanel('date_from'),
    FieldPanel('date_to'),
    FieldPanel('time_from'),
    FieldPanel('time_to'),
    FieldPanel('location'),
    FieldPanel('audience'),
    FieldPanel('cost'),
    FieldPanel('signup_link'),
    InlinePanel(EventPage, 'carousel_items', label="Carousel items"),
    FieldPanel('body', classname="full"),
    InlinePanel(EventPage, 'speakers', label="Speakers"),
    InlinePanel(EventPage, 'related_links', label="Related links"),
]

EventPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]


class EventIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    def get_events(self):
        # Get list of live event pages that are descendants of this page
        events = EventPage.objects.descendant_of(self).live()

        # Filter events list to get ones that are either
        # running now or start in the future
        events = events.filter(date_from__gte=date.today())

        # Order by date
        events = events.order_by('date_from')

        return events

class EventIndexPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('EventIndexPage', related_name='related_links')

EventIndexPage.content_panels = Page.content_panels + [
    FieldPanel('intro', classname="full"),
    InlinePanel(EventIndexPage, 'related_links', label="Related links"),
]


# Person page

class PersonPage(Page, ContactFieldsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    intro = RichTextField(blank=True)
    biography = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('first_name'),
        index.SearchField('last_name'),
        index.SearchField('intro'),
        index.SearchField('biography'),
    )

class PersonPageRelatedLink(Orderable, AbstractRelatedLink):
    page = ParentalKey('PersonPage', related_name='related_links')

PersonPage.content_panels = Page.content_panels + [
    FieldPanel('first_name'),
    FieldPanel('last_name'),
    FieldPanel('intro', classname="full"),
    FieldPanel('biography', classname="full"),
    ImageChooserPanel('image'),
    MultiFieldPanel(ContactFieldsMixin.panels, "Contact"),
    InlinePanel(PersonPage, 'related_links', label="Related links"),
]

PersonPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]


# Contact page

class ContactPage(Page, ContactFieldsMixin):
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

ContactPage.content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    MultiFieldPanel(ContactFieldsMixin.panels, "Contact"),
]

ContactPage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
]


# Form page

class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')

FormPage.content_panels = Page.content_panels + [
    FieldPanel('intro', classname="full"),
    InlinePanel(FormPage, 'form_fields', label="Form fields"),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
]


# Advert snippet

class Advert(models.Model):
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='adverts',
        null=True,
        blank=True
    )
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        PageChooserPanel('page'),
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __unicode__(self):
        return self.text

register_snippet(Advert)


class AdvertPlacement(models.Model):
    page = ParentalKey('wagtailcore.Page', related_name='advert_placements')
    advert = models.ForeignKey('Advert', related_name='+')

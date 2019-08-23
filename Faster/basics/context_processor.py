from .models import RssSubscription


def rss_info(request):
    rss_info = RssSubscription.objects.filter(status='p').order_by('-id')
    return {'rss_info': rss_info}

import urllib2
import simplejson as json
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils import translation
from project.sift.settings import FLICKR_API_KEY

# This script was made for a single use, review before running
from project.sift.models import CatPhoto, Source, CatAlbum


class Command(BaseCommand):
    help = 'Download a set from Flickr'

    @staticmethod
    def _resource_already_exists(key):
        return CatPhoto.objects.filter(source_key=key).exists()

    def handle(self, *args, **options):
        translation.activate('en')
        set_id = '72157629276386494'
        page = 1
        set_url = 'https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=' + FLICKR_API_KEY + '&photoset_id=' + set_id + '&extras=license,owner_name&format=json&nojsoncallback=1&page=' + str(page)
        # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{o-secret}_o.(jpg|gif|png)
        image_url_template = 'https://farm%s.staticflickr.com/%s/%s_%s_b.jpg'
        # https://www.flickr.com/photos/{user-id}/{photo-id}
        reference_url_template = 'https://www.flickr.com/photos/%s/%s'
        request = urllib2.Request(set_url)
        response = urllib2.urlopen(request)
        data = response.read()
        data = json.loads(data)
        source = Source.objects.filter(description='Flickr').first()
        if not source:
            source = Source(
                name='Flickr',
                description='Flickr'
            )
            source.save()
        album = CatAlbum.objects.get(pk=15)
        for photo in data['photoset']['photo']:
            if not self._resource_already_exists(photo['id']):
                new_photo = CatPhoto(
                    source=source,
                    source_url=(reference_url_template % ('swedish_heritage_board', photo['id'])),
                    source_key=photo['id'],
                    title=photo['title'],
                    author='Berit Wallenberg'
                )
                try:
                    image_url = image_url_template % (photo['farm'], photo['server'], photo['id'], photo['secret'])
                    opener = urllib2.build_opener()
                    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36")]
                    img_response = opener.open(image_url)
                    new_photo.image.save("ceric.jpg", ContentFile(img_response.read()))
                    new_photo.save()
                    album.photos.add(new_photo)
                except:
                    print "Problem loading image %s" % photo['id']
                    continue
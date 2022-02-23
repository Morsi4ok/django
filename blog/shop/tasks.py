import logging
from django_rq import job
from shop.models import Product

logger = logging.getLogger(__name__)


@job
def run_products_update():
    Product.objects.filter(cost=0).update(status="OUT_OF_STOCK")


def some_view_or_function():
    run_products_update.delay()


@job
def run_oma_spider():
    def crawler_results(signal, sender, item, response, spider):
        if item["image"]:
            response = requests.get(item["image"])
            if response.ok:
                path = Path(item["image"])
                open(settings.MEDIA_ROOT / path.name, "wb").write(response.content)
                item["image"] = path.name
        Product.objects.update_or_create(external_id=item["external_id"], defaults=item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(MileSpider)
    process.start()

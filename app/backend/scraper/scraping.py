# -*- coding: utf-8 -*-
from lxml import html
import requests
import asyncio
import nest_asyncio


def scraping(list_of_links_and_configs):
    results = []
    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop)
    responses = loop.run_until_complete(
        organize_tasks(*list_of_links_and_configs)
    )
    for response in responses:
        results.append(response)
    return results


async def organize_tasks(*tuples_of_links_and_configs):
    tasks = []
    for tuple_of_link_and_config in tuples_of_links_and_configs:
        tasks.append(scraper(tuple_of_link_and_config))
    return await asyncio.gather(*tasks)


async def scraper(tuple_of_link_and_config):
    link, config = tuple_of_link_and_config
    html_tree = await get_html_tree(link)
    result = await find_element(link, html_tree, config)
    return result


async def get_html_tree(link):
    html_string = requests.get(link).content
    html_tree = html.fromstring(html_string)
    return html_tree


async def find_element(link, html_tree, conf):
    result = {
        "service_name": conf["service_name"],
        "link": link
    }
    service_name = conf.pop("service_name", None)
    for field in conf:
        xpath_or_with_endpoint = conf[field]
        if isinstance(xpath_or_with_endpoint, dict):
            (endpoint, xpath), = xpath_or_with_endpoint.items()
        else:
            xpath = xpath_or_with_endpoint
            endpoint = None
        scraped = html_tree.xpath(xpath)
        if not scraped:
            continue
        try:
            scraped = list(map(lambda x: x.text, scraped))
        except AttributeError:
            scraped = list(scraped)
        finally:
            for i, scraped_item in enumerate(scraped):
                scraped[i] = scraped_item if endpoint is None \
                    else endpoint + scraped_item
            if len(scraped) == 1:
                scraped = scraped[0]
        result[field] = scraped
    conf["service_name"] = service_name
    return result


if __name__ == "__main__":
    from app.backend.google_search.mining import mining
    from app.backend.google_search.filtering import filtering
    findings = mining("pythad")
    filtered = filtering(findings)
    print(scraping(filtered))

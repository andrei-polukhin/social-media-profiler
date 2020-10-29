# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import nest_asyncio

from lxml import html


def scraping(list_of_links_and_configs):
    results = []
    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop)
    responses = loop.run_until_complete(
        organize_tasks(loop, *list_of_links_and_configs)
    )
    for response in responses:
        results.append(response)
    return results


async def organize_tasks(loop, *tuples_of_links_and_configs):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for tuple_of_link_and_config in tuples_of_links_and_configs:
            tasks.append(scraper(session, tuple_of_link_and_config))
        return await asyncio.gather(*tasks)


async def scraper(session, tuple_of_link_and_config):
    link, config = tuple_of_link_and_config
    html_string = await get_html_string(session, link)
    html_tree = await get_html_tree(html_string)
    result = await find_element(link, html_tree, config)
    return result


async def get_html_string(session, link):
    async with session.get(link) as response:
        return await response.text()


async def get_html_tree(html_tree):
    return html.fromstring(html_tree)


async def find_element(link, html_tree, conf):
    result = {"service_name": conf["service_name"], "link": link}
    service_name = conf.pop("service_name", None)
    for field in conf:
        xpath_or_with_endpoint = conf[field]
        if isinstance(xpath_or_with_endpoint, dict):
            ((endpoint, xpath),) = xpath_or_with_endpoint.items()
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
        for i, scraped_item in enumerate(scraped):
            scraped[i] = scraped_item if endpoint is None else endpoint + scraped_item
        if len(scraped) == 1:
            scraped = scraped[0]
        result[field] = scraped
    conf["service_name"] = service_name
    return result


if __name__ == "__main__":
    from app.backend.scraping.google_search.mining import mining
    from app.backend.scraping.google_search.filtering import filtering

    findings = mining("pythad")
    filtered = filtering(findings)
    print(scraping(filtered))

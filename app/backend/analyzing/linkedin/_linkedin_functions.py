# -*- coding: utf-8 -*-
"""The LinkedIn analyzing module with functions."""

import copy

from typing import List


def linkedin_analyze(scraping_response: dict) -> dict:
    """
    Call other functions to take scraping response and confine it to a few keys.

    Args:
        `scraping_response`: the dict that has been received after scraping.
    Returns:
        `dict`: the dictionary with filtered information about subjects.
    """
    returned_dictionary = scraping_response["linkedin"]
    (character_of_return, returned_subjects), = returned_dictionary.items()
    filtered_subjects = {}
    filtered_subjects[character_of_return] = filtered_list = []
    for returned_subject in returned_subjects:
        filtered_subject = _linkedin_analyze_all(returned_subject)
        filtered_list.append(filtered_subject)
    return filtered_subjects


def _linkedin_analyze_all(subject_after_return: dict) -> dict:
    """
    Take an initial scraped subject and run filtering rules against it (see code).

    Args:
        `subject_after_return`: an initial scraped subject.
    Returns:
        `dict`: the dictionary with filtered information about it.
    """
    selecting_rules = {
        "certifications": [
            "authority",
            "name",
            "timePeriod",
            "url"
        ],
        "education": [
            "degreeName",
            "fieldOfStudy",
            "schoolName",
            "timePeriod"
        ],
        "experience": [
            "company",
            "companyName",
            "locationName",
            "timePeriod",
            "title"
        ],
        "skills": ["name"]
    }
    filtered_dict = copy.deepcopy(subject_after_return)
    for dictionary_key, dictionary_selectors in selecting_rules.items():
        filtered_dict = _linkedin_analyze_by_selector(
            subject_after_return, filtered_dict, dictionary_key, dictionary_selectors
        )
    return filtered_dict


def _linkedin_analyze_by_selector(
        subject_after_return: dict, filtered_dict: dict, dict_key: str, dict_selector: List[str]
) -> dict:
    """
    Filter a returned subject with selectors key and values.

    Args:
        subject_after_return: an initial scraped subject.
        filtered_dict: the dictionary with filtered information from `subject_after_return`.
        dict_key: the selector in an initial scraped subject to which filtering should run against.
        dict_selector: the values to which filtering should run against.
    Returns:
        filtered_dict: the dictionary with filtered information from `subject_after_return`.
    """
    returned_certifications = subject_after_return[dict_key]
    filtered_dict[dict_key] = list_of_filtered_certifications = []
    for returned_certification in returned_certifications:
        filtered_certification = {
            k: v
            for k, v in returned_certification.items()
            if k in dict_selector
        }
        list_of_filtered_certifications.append(filtered_certification)
    return filtered_dict

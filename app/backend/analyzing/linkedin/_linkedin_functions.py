# -*- coding: utf-8 -*-
import copy


def linkedin_analyze(scraping_response):
    returned_dictionary = scraping_response["linkedin"]
    (character_of_return, returned_subjects), = returned_dictionary.items()
    filtered_subjects = {}
    filtered_subjects[character_of_return] = filtered_list = []
    for returned_subject in returned_subjects:
        filtered_subject = _linkedin_analyze_all(returned_subject)
        filtered_list.append(filtered_subject)
    return filtered_subjects


def _linkedin_analyze_all(subject_after_return):
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


def _linkedin_analyze_by_selector(subject_after_return, filtered_dict, dict_key, dict_selector):
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


if __name__ == "__main__":
    print(linkedin_analyze({'linkedin': {'found_subjects': [{'certifications': [{'authority': 'Coursera', 'company': {'active': True, 'entityUrn': 'urn:li:fs_miniCompany:2453129', 'logo': {'com.linkedin.common.VectorImage': {'artifacts': [{'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '200_200/0?e=1612396800&v=beta&t=EHDhgWg4IlDfhRUDdcUfl4Q9LAt3qFaHsfhmm3HsqS0', 'height': 200, 'width': 200}, {'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '100_100/0?e=1612396800&v=beta&t=MY8l728fLQEDvnvBHnnNuS924zqWX-u6MisNXLO_X-8', 'height': 100, 'width': 100}, {'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '400_400/0?e=1612396800&v=beta&t=zdus18BsefygJOLb1NxlcrgcbhPjmxBg62nV5sC2cZU', 'height': 400, 'width': 400}], 'rootUrl': 'https://media-exp1.licdn.com/dms/image/C4E0BAQGt72dvhq4yRA/company-logo_'}}, 'name': 'Coursera', 'objectUrn': 'urn:li:company:2453129', 'showcase': False, 'trackingId': 'R14BaWOiT7+3opE2DjPImQ==', 'universalName': 'coursera'}, 'companyUrn': 'urn:li:fs_miniCompany:2453129', 'displaySource': 'coursera.org', 'licenseNumber': 'EJM73S6VCK3C', 'name': 'Neural Networks and Deep Learning', 'timePeriod': {'startDate': {'month': 2, 'year': 2018}}, 'url': 'https://www.coursera.org/account/accomplishments/verify/EJM73S6VCK3C'}, {'authority': 'Coursera', 'company': {'active': True, 'entityUrn': 'urn:li:fs_miniCompany:2453129', 'logo': {'com.linkedin.common.VectorImage': {'artifacts': [{'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '200_200/0?e=1612396800&v=beta&t=EHDhgWg4IlDfhRUDdcUfl4Q9LAt3qFaHsfhmm3HsqS0', 'height': 200, 'width': 200}, {'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '100_100/0?e=1612396800&v=beta&t=MY8l728fLQEDvnvBHnnNuS924zqWX-u6MisNXLO_X-8', 'height': 100, 'width': 100}, {'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '400_400/0?e=1612396800&v=beta&t=zdus18BsefygJOLb1NxlcrgcbhPjmxBg62nV5sC2cZU', 'height': 400, 'width': 400}], 'rootUrl': 'https://media-exp1.licdn.com/dms/image/C4E0BAQGt72dvhq4yRA/company-logo_'}}, 'name': 'Coursera', 'objectUrn': 'urn:li:company:2453129', 'showcase': False, 'trackingId': 'bydZGbihT96mbJ1RGsI4XQ==', 'universalName': 'coursera'}, 'companyUrn': 'urn:li:fs_miniCompany:2453129', 'displaySource': 'coursera.org', 'licenseNumber': 'HKEZ5JXH6XQB', 'name': 'Architecting with Google Kubernetes Engine Specialization', 'timePeriod': {'startDate': {'month': 12, 'year': 2019}}, 'url': 'https://www.coursera.org/account/accomplishments/specialization/HKEZ5JXH6XQB'}, {'authority': 'Udemy', 'company': {'active': True, 'entityUrn': 'urn:li:fs_miniCompany:822535', 'logo': {'com.linkedin.common.VectorImage': {'artifacts': [{'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '200_200/0?e=1612396800&v=beta&t=5zw-YHSEMi7z4LGvU_CrvcuE4Etta-ebXXWr1a27xA8', 'height': 200, 'width': 200}, {'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '100_100/0?e=1612396800&v=beta&t=bpxZ9bsrIjgK585EkShhhnXRJQL1qA9Vu-HQiy-SiOU', 'height': 100, 'width': 100}, {'expiresAt': 1612396800000, 'fileIdentifyingUrlPathSegment': '400_400/0?e=1612396800&v=beta&t=1-6cnXMj6Krj5nDrCnvVnJR3UhXSpmbY2_5op2tFzIQ', 'height': 400, 'width': 400}], 'rootUrl': 'https://media-exp1.licdn.com/dms/image/C560BAQH0VNXBrdkklA/company-logo_'}}, 'name': 'Udemy', 'objectUrn': 'urn:li:company:822535', 'showcase': False, 'trackingId': 'DutEeIeWRLKV+1CUm7+Wgg==', 'universalName': 'udemy'}, 'companyUrn': 'urn:li:fs_miniCompany:822535', 'displaySource': 'udemy.com', 'name': 'Serverless for AWS', 'url': 'https://www.udemy.com/certificate/UC-7566639c-159c-43fc-a396-47b0ec529b9a/?utm_campaign=email&utm_source=sendgrid.com&utm_medium=email'}], 'education': [{'degreeName': 'Doctor of Philosophy - PhD', 'degreeUrn': 'urn:li:fs_degree:900', 'entityUrn': 'urn:li:fs_education:(ACoAACcgiYoBxF5N7LgmA3mm4aSVlztSDuBjaIg,565920957)', 'fieldOfStudy': 'Theoretical Mechanics', 'schoolName': 'Institute of Mathematics NAS of Ukraine', 'timePeriod': {'endDate': {'year': 2006}, 'startDate': {'year': 2000}}}], 'experience': [{'company': {'employeeCountRange': {'end': 50, 'start': 11}, 'industries': ['Information Technology and Services']}, 'companyLogoUrl': 'https://media-exp1.licdn.com/dms/image/C560BAQHuQ5AuTe-JUQ/company-logo_', 'companyName': 'Xenoss', 'companyUrn': 'urn:li:fs_miniCompany:27100989', 'entityUrn': 'urn:li:fs_position:(ACoAACcgiYoBxF5N7LgmA3mm4aSVlztSDuBjaIg,1439131201)', 'geoLocationName': 'Kiev Region, Ukraine', 'geoUrn': 'urn:li:fs_geo:100220281', 'locationName': 'Kiev Region, Ukraine', 'region': 'urn:li:fs_region:(ua,10183)', 'timePeriod': {'startDate': {'month': 3, 'year': 2019}}, 'title': 'Software Engineer'}, {'company': {'employeeCountRange': {'end': 200, 'start': 51}, 'industries': ['Information Technology and Services']}, 'companyLogoUrl': 'https://media-exp1.licdn.com/dms/image/C560BAQG7lMwE1vgWvA/company-logo_', 'companyName': 'INFOZAHYST', 'companyUrn': 'urn:li:fs_miniCompany:10134579', 'entityUrn': 'urn:li:fs_position:(ACoAACcgiYoBxF5N7LgmA3mm4aSVlztSDuBjaIg,1439131251)', 'geoLocationName': 'Kiev Region, Ukraine', 'geoUrn': 'urn:li:fs_geo:100220281', 'locationName': 'Kiev Region, Ukraine', 'region': 'urn:li:fs_region:(ua,10183)', 'timePeriod': {'endDate': {'month': 3, 'year': 2019}, 'startDate': {'month': 8, 'year': 2018}}, 'title': 'Software Engineer'}], 'firstName': 'Dmytro', 'geoCountryName': 'Ukraine', 'headline': 'Software Engineer at Xenoss', 'honors': [], 'industryName': 'Computer Software', 'languages': [], 'lastName': 'Ovchynnykov', 'locationName': 'Ukraine', 'publications': [], 'skills': [{'name': 'Node.js', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:18276', 'name': 'Node.js'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:18276'}, {'name': 'PostgreSQL', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:2018', 'name': 'PostgreSQL'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:2018'}, {'name': 'React'}, {'name': 'JavaScript', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:218', 'name': 'JavaScript'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:218'}, {'name': 'Redux'}, {'name': 'GraphQL', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:55393', 'name': 'GraphQL'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:55393'}, {'name': 'SQL', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:483', 'name': 'SQL'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:483'}, {'name': 'Docker Products', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:50281', 'name': 'Docker Products'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:50281'}, {'name': 'Linux', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:301', 'name': 'Linux'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:301'}, {'name': 'MongoDB'}, {'name': 'Representational State Transfer (REST)'}, {'name': 'ElasticSearch'}, {'name': 'Prisma'}, {'name': 'TypeScript', 'standardizedSkill': {'entityUrn': 'urn:li:fs_miniSkill:50517', 'name': 'TypeScript'}, 'standardizedSkillUrn': 'urn:li:fs_miniSkill:50517'}, {'name': 'RabbitMQ'}], 'student': False}]}}))

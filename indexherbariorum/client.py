import requests

DEFAULT_BASE_URL = 'http://sweetgum.nybg.org/science/api/v1'
RESOURCE_NAMES = ['staff', 'institutions']


class HttpRequestError(Exception):
    """Raised when a request is not successful."""
    pass


class InvalidKeyError(Exception):
    """Raised when invalid key is used"""
    pass


class IndexHerbariorumApi:
    """Performs requests to the Index Herbariorum API web services.
    Refer to https://github.com/nybgvh/IH-API/wiki for API documentation.
    """

    def countries(self):
        """Get all available countries.

        :raises HttpRequestError: if request is not successful.

        :return: JSON Response
        """

        return self.get_json(requests.get(DEFAULT_BASE_URL + '/countries'))

    def staff(self, rq={}):
        """Performs search for staff.

        :param rq: optional HTTP GET parameters.
        :type rq: dict

        :raises InvalidKeyError: when 'download' key is present.
        :raises HttpRequestError: if request is not successful.

        :return: JSON Response
        """

        if rq:
            if 'download' in rq:
                raise InvalidKeyError("'download' key not allowed. Use download() function instead.")
            return self.get_json(requests.get(DEFAULT_BASE_URL + '/staff/search', params=rq))
        else:
            return self.get_json(requests.get(DEFAULT_BASE_URL + '/staff'))

    def institution(self, code):
        """Get an institution based on code.

        :param code: Institution code.
        :type code: string

        :raises HttpRequestError: if request is not successful.

        :return: JSON Response
        """

        return self.get_json(requests.get(DEFAULT_BASE_URL + '/institutions/{}'.format(code)))

    def institutions(self, rq={}):
        """Performs search for institutions.

        :param rq: optional HTTP GET parameters.
        :type rq: dict

        :raises InvalidKeyError: when 'download' key is present.
        :raises HttpRequestError: if request is not successful.

        :return: JSON Response
        """

        if rq:
            if 'download' in rq:
                raise InvalidKeyError("'download' key not allowed. Use download() function instead.")
            return self.get_json(requests.get(DEFAULT_BASE_URL + '/institutions/search', params=rq))
        else:
            return self.get_json(requests.get(DEFAULT_BASE_URL + '/institutions'))

    def count_countries(self):
        """Returns the total number of countries.

        :raises HttpRequestError: if request is not successful.

        :return: int
        """

        countries = self.countries()
        return countries['meta']['hits']

    def count_staff(self, rq={}):
        """Returns the total number of staff records based on search.

        :param rq: optional HTTP GET parameters.
        :type rq: dict

        :raises HttpRequestError: if request is not successful.

        :return: Count as int
        """

        if rq:
            body = self.get_json(requests.get(DEFAULT_BASE_URL + '/staff/search', params=rq))
            return body['meta']['hits']
        else:
            body = self.get_json(requests.get(DEFAULT_BASE_URL + '/staff'))
            return body['meta']['hits']

    def count_institutions(self, rq={}):
        """Returns the total number of institution records based on search.

        :param rq: optional HTTP GET parameters.
        :type rq: dict

        :raises HttpRequestError: if request is not successful.

        :return: int
        """

        if rq:
            body = self.get_json(requests.get(DEFAULT_BASE_URL + '/institutions/search', params=rq))
            return body['meta']['hits']
        else:
            body = self.get_json(requests.get(DEFAULT_BASE_URL + '/institutions'))
            return body['meta']['hits']

    def download(self, resource, rq={}, filename='index_herbariorum.csv'):
        """Download results as a CSV file.

        :param resource: Valid resource name. Must match 'staff' or 'institutions'.
        :type resource: string

        :param rq: HTTP GET parameters.
        :type rq: dict

        :param filename: Name of the file that will be created.
        :type filename: string

        :raises HttpRequestError: if request is not successful.
        :raises HttpRequestError: when invalid resource name.
        :raises IOError: when it fails to create csv.

        :return: CSV File
        """

        if resource in RESOURCE_NAMES:
            try:
                rq['download'] = 'yes'
                response = requests.get(DEFAULT_BASE_URL + '/{}/search'.format(resource),
                                        params=rq,
                                        headers={"Content-Type": "text/csv"})

                if response.status_code == 200:
                    csv_content = response.content
                    with open(filename, 'wb') as output:
                        output.write(csv_content)
                        output.close()
                else:
                    raise HttpRequestError("HTTP Error: %s" % response.status_code)
            except IOError as error:
                raise("Error downloading csv file: %s" % error)
        else:
            raise HttpRequestError("Invalid resource name")

    def get_json(self, response):
        """Returns body as JSON.

        :param response: Body from the request
        :type: Response object

        :raises HttpRequestError: if request is not successful.

        :return: JSON
        """

        if response.status_code != 200:
            raise HttpRequestError("HTTP Error: %s" % response.status_code)
        else:
            return response.json()



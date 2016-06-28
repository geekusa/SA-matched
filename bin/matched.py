#!/opt/splunk/bin/python

from splunklib.searchcommands import *
import sys
import csv


@Configuration()
class searchTermMatch(StreamingCommand):
    labelfield = Option(
        doc='''
        **Syntax:** **labelfield=***<fieldname>*
        **Description:** Name of the field that will hold the match count''',
        validate=validators.Fieldname())

    search_terms_field = Option(
        doc='''
        **Syntax:** **search_terms_field=***<fieldname>*
        **Description:** Name of the field that will contain the terms to search with''',
        validate=validators.Fieldname())

    csv_file = Option(
        doc='''**Syntax:** **csv=***<path>*
        **Description:** CSV file that will contain the terms to search with''',
        name='csv', validate=validators.File())

    textfield = Option(
        doc='''
        **Syntax:** **search_terms=***<fieldname>*
        **Description:** Name of the field that will contain the text to search against''',
        validate=validators.Fieldname())

    def stream(self, records):
        if self.labelfield:
            fieldname = self.labelfield
        else:
            fieldname = "searchTermsMatched"
        #if csv file contains the search terms
        try:
            reader = csv.DictReader(self.csv_file)
            search_terms_list = []
            for row in reader:
                for k,v in row.items():
                    search_terms_list.append(v)
        except:
            pass
        for record in records:
            outputlist = []
            if self.textfield:
                text = record[self.textfield]
            else:
                text = record['_raw']
            #if a field contains the search terms
            try:
                search_terms = record[self.search_terms_field]
                search_terms = search_terms.split(",")
                for term in search_terms:
                    if term.lower() in text.lower():
                        outputlist.append(term)
                        record[fieldname] = outputlist
            except:
                pass
            try:
                for term in search_terms_list:
                    if term.lower() in text.lower():
                        outputlist.append(term)
                        record[fieldname] = outputlist
            except:
                pass
            yield record

dispatch(searchTermMatch, sys.argv, sys.stdin, sys.stdout, __name__)

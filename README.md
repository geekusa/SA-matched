##SA-matched

This supporting add-on provides one command -- `matched`. It is built on the Splunk SDK.

Available at:

[Github](https://github.com/geekusa/SA-matched)

Version: 1.0

Command reference:

#matched

##Description

The `matched` command finds which terms exist in a field of text from a field or csv list of terms. Unless you specify a different field, `matched` results are based on the contents of the `_raw` field.

The result of the matched command appends a new field to each event. You can specify what to name the field with the `lablefield` parameter, which defaults to `searchTermsMatched`. Either `csv` or `search_terms_field` parameter is required. `search_terms_field` must be a comma separated list of terms.

Command was created because of need identified in  [Splunk Answers 33662 - Identfying the Search Terms Matched](https://answers.splunk.com/answers/33662/identfying-the-search-terms-matched.html).

##Syntax

matched csv=\<filename.csv\>|search\_terms\_field=\<field\> \[labelfield=\<field\>] \[fieldname=\<field\>] \[\<field-list\>]

###Required arguments

 **csv|search_terms_field**  
    **Syntax:** csv=\<path\> OR search\_terms\_field=\<field\>  
    **Description:** Specify a CSV filename including the complete path. Alternatively specify a field with a comma separated list of terms to search through.  
    **Usage:** For the csv option, if the CSV file is in an appropriate directory then merely specifying the filename.csv is sufficient, otherwise entire path will need to be entered:  `/home/user/filename.csv`

###Optional arguments

 **textfield**  
   	**Syntax:** \<field\> ...  
   	**Description:** The field used to search against for term matches.  
   	**Default:** `_raw`

  **labelfield**  
   	**Syntax:** labelfield=\<field\>  
   	**Description:** Name of the field to write the matched search terms to.  
   	**Default:** searchTermsMatched

##Examples

###**1: Using a lookup to free form search then find out what matched**

`* [|inputlookup ransomware_variants|rename variant as search|format]|table _time _raw|matched csv="/opt/splunk/etc/system/lookups/ransomware_variants.csv"`

### Support
Support will be provided through Splunkbase

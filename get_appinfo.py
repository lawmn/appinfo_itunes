#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import urllib2
import sys

RESULTS_PARAMS = [
'kind',
'features',
'supportedDevices',
'isGameCenterEnabled',
'artistViewUrl',
'artworkUrl60',
'screenshotUrls',
'ipadScreenshotUrls',
'artworkUrl512',
#'description',
'currency',
'genres',
'genreIds',
'releaseDate',
'sellerName',
'bundleId',
'trackId',
'trackName',
'primaryGenreName',
'primaryGenreId',
#'releaseNotes',
'formattedPrice',
'wrapperType',
'trackCensoredName',
'trackViewUrl',
'contentAdvisoryRating',
'artworkUrl100',
'languageCodesISO2A',
'fileSizeBytes',
'sellerUrl',
'trackContentRating',
'averageUserRating',
'userRatingCount',
]


def get_urlrsrc(url = ''):
    return urllib2.urlopen(url).read()

def get_output(bundleid = '', rsrc_json = None):
    # get header
    output_list = get_headerlist(bundleid, rsrc_json)

    # get appinfo
    appinfo2data = None
    if not len(rsrc_json['results']) == 0:
        appinfo2data = rsrc_json['results'][0]
    output_list.extend(get_appinfolist(appinfo2data))

    # standard output
    output = u'\t'.join(output_list)
    return output.encode('utf8').rstrip()

def get_appinfolist(appinfo2data = None):
    if not appinfo2data:
        return ['' for appinfo in RESULTS_PARAMS]

    output_list = []
    for appinfo in RESULTS_PARAMS:
        if not appinfo in appinfo2data:
            output_list.append('')
            continue
        data = appinfo2data[appinfo]
        if isinstance(data, list):
            data = list2csv(data)
        if isinstance(data, bool):
            data = bool2uni(data)
        if isinstance(data, int):
            data = int2uni(data)
        if isinstance(data, float):
            data = float2uni(data)
        output_list.append(data)

    return output_list

def list2csv(l = None):
    return u','.join(l)

def bool2uni(b = None):
    return unicode(b)

def int2uni(i = None):
    return unicode(i)

def float2uni(f = None):
    return unicode(int(f))

def get_headerlist(bundleid = '', rsrc_json = None):
    return [
        unicode(bundleid),
        unicode(rsrc_json['resultCount']),
        ]

def get_appinfo(bundleid = ''):
    url = 'https://itunes.apple.com/lookup?bundleId=%s' % bundleid
    print get_output(bundleid, json.loads(get_urlrsrc(url)))

if __name__ == "__main__":
    bundleid = 'jp.co.jorudan.NorikaeAnnai'
    if len(sys.argv) == 2:
        bundleid = sys.argv[1]

    get_appinfo(bundleid)

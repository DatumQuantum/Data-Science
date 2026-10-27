#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:56:11 2018

@author: ntl008
"""

import os
import json
import facebook
import requests
from argparse import ArgumentParser

def get_parser():
    parser=ArgumentParser()
    parser.add_argument('--page')
    parser.add_argument('--n',default=500,type=int)
    return parser

if __name__=='__main__':
    parser=get_parser()
    args=parser.parse_args()
    
    token=''
    graph = facebook.GraphAPI(token)
    all_fields=['id','likes.summary(true)','permalink_url']
    all_fields=','.join(all_fields)
    
    
    posts = graph.get_connections('NBAIndia','posts',fields=all_fields)
    #page=graph.get_object(args.page,fields=all_fields)
    
    downloaded=0
    while True:
        if downloaded >= args.n:
            break
        try:
            fname="posts_{}.json1".format(args.page)
            with open(fname,'a') as f:
                for post in posts['data']:
                    downloaded+=1
                    f.write(json.dumps(post)+"\n")
                posts=requests.get(posts['paging']['next']).json()
        except KeyError:
            break
           
    #print(json.dumps(page, indent=4))
    

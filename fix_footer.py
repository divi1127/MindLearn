# -*- coding: utf-8 -*-
import os
import re

files = [
    'terms-condition.html', 'services.html', 'privacy-policy.html',
    'index.html', 'contact.html', 'blog-details.html',
    'blog-details-3.html', 'blog-details-2.html',
    'blog-details-1.html', 'about.html'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove 'Call Us 7/24'
    content = re.sub(r'\s*<span class=\"fw-medium tw-text-4 text-paragraph-600 tw-mb-1 d-block\">\s*Call Us 7/24\s*</span>', '', content)
    
    # Add 'Proudly Developed & Designed by Jodtech Company'
    target = '<span class=\"fw-normal tw-text-4 text-black\">© All Copyright 2026 by Mind Wave</span>'
    replacement = '''<div class=\"d-flex flex-column tw-gap-1\">
          <span class=\"fw-normal tw-text-4 text-black\">© All Copyright 2026 by Mind Wave</span>
          <span class=\"fw-normal tw-text-4 text-black\">Proudly Developed & Designed by Jodtech Company</span>
        </div>'''
    
    if target in content:
        content = content.replace(target, replacement)
        print(f'Successfully updated footer text in {f}')
    else:
        print(f'Target copyright text not found in {f}')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

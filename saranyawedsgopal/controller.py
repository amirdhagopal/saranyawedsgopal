#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import webapp2
import os
import cgi
import logging


jinja_environment = jinja2.Environment( loader = jinja2.FileSystemLoader(os.path.dirname(__file__) ))
html_path = 'html/'	
template_path = 'template/'
page_path =  html_path + 'page.html'

class BaseHandler(webapp2.RequestHandler):
    pass
    
class HomeHandler(BaseHandler):
    def get(self):
        template_values = {}
        template_values['header'] = 'Saranya Weds Gopal'
    	
    	template_values['page_title'] = 'Saranya Weds Gopal'
    	template_values['form_name'] = template_path + 'home_form.template'

    	template = jinja_environment.get_template(page_path)
    	self.response.out.write(template.render(template_values))
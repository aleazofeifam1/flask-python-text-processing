#!/usr/bin/env python
# -*- coding: utf-8 -*-
from code.run import api
from app.controllers import *

api.add_resource(File, '/uploader')
api.add_resource(File, '/files/<string:path>')




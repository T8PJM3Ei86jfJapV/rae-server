# -*- coding: utf-8 -*-

import json
import logging

import requests

from dao.pattern import DataDaoFactory

logger = logging.getLogger('AgentService')
DEFAULT_SERVICE_PORT = '8080'


def get_agent_by_id(agent_id):
    agent_dao = DataDaoFactory().get('AgentDao')
    agent = agent_dao.get_by_id(agent_id)
    # return agent if exists
    # else raise error
    if agent:
        return agent
    else:
        raise Exception('Agent not found!')


def get_last_package(agent_id):
    agent_dao = DataDaoFactory().get('AgentDao')
    pkg_dao = DataDaoFactory().get('PackageDao')

    logger.info('get last package by agent id: agent_id = {0}'.format(agent_id))
    pkg_id = agent_dao.get_last_package_id(agent_id)
    logger.info('the last package id is {0}'.format(pkg_id))

    if not pkg_id:
        return None

    # get package object by its id
    package = pkg_dao.get_by_id(pkg_id)
    return package


def create(agent):
    agent_dao = DataDaoFactory().get('AgentDao')
    agent_dao.save_or_update(agent)


def post_request(url, instruct):
    logger.info('request {0}, data={1}'.format(url, json.dumps(instruct)))
    req = requests.post(url, data=instruct)
    logger.info('status code: {0}, content: {1}'.format(req.status_code, req.text))
    return req


def fetch(agent, link):
    instruct = {
        'agent_name': agent.name,
        'agent_action': 'fetch',
        'package_link': link
    }
    url = 'http://%(host)s:%(port)s/async' % agent
    post_request(url, instruct)


def start(agent):
    instruct = {
        'agent_name': agent.name,
        'service_port': DEFAULT_SERVICE_PORT,
        'agent_action': 'start',
    }
    url = 'http://%(host)s:%(port)s/async' % agent
    post_request(url, instruct)


def restart(agent):
    instruct = {
        'agent_name': agent.name,
        'service_port': DEFAULT_SERVICE_PORT,
        'agent_action': 'restart',
    }
    url = 'http://%(host)s:%(port)s/async' % agent
    post_request(url, instruct)


def alive(agent):
    instruct = {
        'agent_name': agent.name,
        'agent_action': 'alive',
    }
    url = 'http://%(host)s:%(port)s/sync' % agent
    response = post_request(url, instruct)
    if response.text and response.text.code == '200':
        return True
    else:
        return False


def stop(agent):
    instruct = {
        'agent_name': agent.name,
        'agent_action': 'stop',
    }
    url = 'http://%(host)s:%(port)s/async' % agent
    post_request(url, instruct)

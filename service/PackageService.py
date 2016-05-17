# -*- coding: utf-8 -*-

from model import Package

from dao.pattern import DataDaoFactory

pkg_dao = DataDaoFactory().get('PackageDao')


def save(agent_id, rel_path):
    args = dict(
        agent_id = agent_id, 
        rel_path = rel_path
    )
    package = Package(**args)
    pkg_dao.save(package)


def deleted(id):
    pkg_dao.delete_by_id(id)
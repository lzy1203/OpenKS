"""
Abstract dataset format HDG for Heterogeneous Distributed Graph
"""
from typing import List

class HDG(object):

	def __init__(
		self, 
		entity_types: List = [], 
		relation_types: List = [], 
		entity_attrs: List = [], 
		relation_attrs: List = [], 
		entities: List = [], 
		relations: List = []
		) -> None:
		self._entity_types = entity_types
		self._relation_types = relation_types
		self._entity_attrs = entity_attrs
		self._relation_attrs = relation_attrs
		self._entities = entities
		self._relations = relations

	@property
	def entity_types(self):
		return self._entity_types
	
	@entity_types.setter
	def entity_types(self, entity_types):
		self._entity_types = entity_types

	@property
	def relation_types(self):
		return self._relation_types
	
	@relation_types.setter
	def relation_types(self, relation_types):
		self._relation_types = relation_types

	@property
	def entity_attrs(self):
		return self._entity_attrs
	
	@entity_attrs.setter
	def entity_attrs(self, entity_attrs):
		self._entity_attrs = entity_attrs

	@property
	def relation_attrs(self):
		return self._relation_attrs
	
	@relation_attrs.setter
	def relation_attrs(self, relation_attrs):
		self._relation_attrs = relation_attrs

	@property
	def entities(self):
		return self._entities
	
	@entities.setter
	def entities(self, entities):
		self._entities = entities

	@property
	def relations(self):
		return self._relations
	
	@relations.setter
	def relations(self, relations):
		self._relations = relations
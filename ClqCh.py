"""
@author-Aayushi Srivastava
Generates chordal graphs using Cliques of a graph
"""

import random

import numpy as numpy
import itertools

import networkx as nx
import matplotlib.pyplot as plt

class CliqueTest:
	def __init__(self, noNodes):
		self.noNodes = noNodes
		self.vertexList = []
		self.edgeList = []
		self.H = {}
		self.clqsub = []
		self.cliquecount = 0
		self.clqnghbr = 0
	def addVertices(self,noNodes):
		#print "Hi"
		for x in range(1,self.noNodes+1):
			self.H = nx.Graph(self.H)
			self.H.add_node(x)
			print "See it"
			clqsub =list(nx.enumerate_all_cliques(self.H))#output list of list
			print "Clique list is:"
			print clqsub
			random.shuffle(clqsub)
			cliqutaken = random.choice(clqsub)
			self.H.add_nodes_from(cliqutaken)
			print "Considered the below clique"
			print cliqutaken
			#self.H = nx.to_dict_of_lists(self.H)
			#if len(self.H) > 1:
				#for j in cliqutaken:
					#self.addanEdge(self.H, self.edgeList,j,x)
			print "We will see now"
			self.H = nx.Graph(self.H)
			k = len(clqsub)
			print "Length is :"
			print k
			if type(self.H) is not dict:
				self.H = nx.to_dict_of_lists(self.H)
				print "Graph is now"
				print self.H
			for key, value in self.H.iteritems():
				#print "See you soon"
				for v in value:
					#print "Go"
					if key < v:
						#print "I can do"
						e = []
						e.append(key)
						e.append(v)
						self.edgeList.append(e)
			#self.H = nx.to_dict_of_lists(self.H)
			if len(self.H) > 1:
				for j in cliqutaken:
					self.addanEdge(self.H, self.edgeList, j, x)
			self.H = nx.Graph(self.H)
			self.plotGraph(self.H)
	def addanEdge(self,graphtoAdd,edgeListtoAdd, v1, v2):
		#self.H = nx.to_dict_of_lists(self.H)
		print type(self.H)
		graphtoAdd[v1].append(v2)
		graphtoAdd[v2].append(v1)
		e = []
		e.append(v1)
		e.append(v2)
		edgeListtoAdd.append(e)
	def plotGraph(self, graphtoDraw):
		GD = nx.Graph(self.H)
		pos = nx.spring_layout(GD)
		nx.draw(GD,pos, width=8.0,alpha=0.5,with_labels=True)
		plt.title("Graph to see")
		plt.draw()
		plt.show()
	if __name__ == "__main__":
		print "Working to generate clique list"
val = input("Enter number of nodes : ")	
clq = CliqueTest(val)
clq.addVertices(val)

###################################################################################################
####
####                  CClabeling -- unittests
#### 
###################################################################################################


import unittest
import os, sys

import CC_labeling_8, graphics
import numpy as np

class TestSequenceFunctions(unittest.TestCase): #subclass unittest.TestCase


   def testDisjointSets(self):
        d = CC_labeling_8.disjointSet(100)
        d.makeSet(3)
        d.makeSet(4)
        d.makeSet(5)
        d.makeSet(6)
        d.union(4,5)
        d.union(4,6)
        self.assertListEqual([4,3],[d.find(6),d.find(3)])

   def testDisjointRegions(self):
        d = CC_labeling_8.disjointRegions(100)
        d.makeSet(3,1,1)
        d.makeSet(4,2,1)
        d.makeSet(5,4,3)
        d.makeSet(6,4,2)
        d.union(4,5)
        d.union(4,6)
        self.assertListEqual([(4, (2, 1)),(3, (1, 1))],[d.find(6),d.find(3)])
 
       
   def testComponentLabeling(self):
        mat =  [[1, -1, 2, 2, 2], [-1, -1, 2, 2, 2],
                [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]]
        graphics.plotHeatMap(mat)
        cclab = CC_labeling_8.CC_lab(mat)
        cclab.connectedComponentLabel()
        graphics.plotHeatMap(cclab.labels)
        labelsComp = [[0, 1, 3, 3, 3], [1, 1, 3, 3, 3],
                      [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]]
        for i in range(len(labelsComp)):
            self.assertListEqual(labelsComp[i],cclab.labels[i])
  
   def testComponentLabeling2(self):
        mat =  [[1, -1, -1, 2, 1,3], [2, 2, 2, 2, 3,3],
                [7, 7, 7, 7, 3,3], [6, 6, 7, 5, 4, 5], [6, 6, 6, 5, 5, 5]]
        graphics.plotHeatMap(mat)
        cclab = CC_labeling_8.CC_lab(mat)
        cclab.connectedComponentLabel()
        graphics.plotHeatMap(cclab.labels)
        labelsComp = [[0, 1, 1, 5, 3, 4], [5, 5, 5, 5, 4, 4],
                      [6, 6, 6, 6, 4, 4], [7, 7, 6, 8, 9, 8],
                      [7, 7, 7, 8, 8, 8]]
        for i in range(len(labelsComp)):
            self.assertListEqual(labelsComp[i],cclab.labels[i])
            
   def testComponentLabeling3(self): # visuel
        map_,points, volumes = graphics.MapGenerator(100, 100, 10, 100)
         
        graphics.plotHeatMap(map_)
        cclab = CC_labeling_8.CC_lab(map_)
        cclab.connectedComponentLabel()
        graphics.plotHeatMap(cclab.labels)


   def testComponentLabelingNeighborRegions(self):
        mat =  [[1, -1, -1, 2, 1,3], [2, 2, 2, 2, 3,3],
                [7, 7, 7, 7, 3,3], [6, 6, 7, 5, 4, 5], [6, 6, 6, 5, 5, 5]]
        graphics.plotHeatMap(mat)
        cclab = CC_labeling_8.CC_lab(mat)
        cclab.connectedComponentLabel()
        graphics.plotHeatMap(cclab.labels)
        computed = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                computed.append([x for x in (cclab.neighborRegions(cclab.labels[i][j],mat))])

        labelsComp = [[1, 5], [0, 5], [0, 5], [0, 1, 3, 4, 6], [4, 5], [3, 5, 6, 8, 9], [0, 1, 3, 4, 6], [0, 1, 3, 4, 6],
                      [0, 1, 3, 4, 6], [0, 1, 3, 4, 6], [3, 5, 6, 8, 9], [3, 5, 6, 8, 9], [4, 5, 7, 8, 9], [4, 5, 7, 8, 9],
                      [4, 5, 7, 8, 9], [4, 5, 7, 8, 9], [3, 5, 6, 8, 9], [3, 5, 6, 8, 9],
                      [6, 8], [6, 8], [4, 5, 7, 8, 9], [4, 6, 7, 9], [4, 6, 8], [4, 6, 7, 9], [6, 8], [6, 8], [6, 8],
                      [4, 6, 7, 9], [4, 6, 7, 9], [4, 6, 7, 9]]
        for i in range(len(labelsComp)):
            self.assertListEqual(labelsComp[i],computed[i])

  		
   def assertListAlmostEqual(self, list1, list2, tol):
        """
        Assert if two lists are almost equal
        """
        self.assertEqual(len(list1), len(list2))
        for a, b in zip(list1, list2):
             self.assertAlmostEqual(a, b, tol)


   def assertListEqual(self, list1, list2):
        """
        Assert if two lists are almost equal
        """
        self.assertEqual(len(list1), len(list2))
        for a, b in zip(list1, list2):
             self.assertEqual(a, b)

             
   def assertMatrixAlmostEqual(self, mat1, mat2, tol):
        """
        Assert if two matrices are almost equal
        """
        self.assertEqual((len(mat1[0]),len(mat2[0])), (len(mat1[1]),len(mat2[1])))
        for i in range(len(mat1)):
            for a, b in zip(mat1[i], mat2[i]):
                 self.assertAlmostEqual(a, b, tol)


   def assertMatrixEqual(self, mat1, mat2):
        """
        Assert if two matrices are almost equal
        """
        self.assertEqual((len(mat1[0]),len(mat2[0])), (len(mat1[1]),len(mat2[1])))
        for i in range(len(mat1)):
            for a, b in zip(mat1[i], mat2[i]):
                 self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()

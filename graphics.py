##########################################################################################
####
####              			 Vizualization tools 
#### 
##########################################################################################
 
import math
import numpy as np
import random
import pylab as pl
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import pyplot as plt
from pylab import *

def MapGenerator(dimx, dimy, n_blobs, elevation, addWhiteNoise = False, noise_level = 0.01, oriented = False):
    '''
    Compute map with (gaussian) blobs for a map at least 20x20 pixels
    If oriented is True, blobs are randomly oriented, and not necessarily parallel to axis.
    '''
    if(dimx < 20 or dimy < 20):
        print 'WARNING: please draw a larger map' 
        return
    
    Xin, Yin = mgrid[0:dimx, 0:dimy]

    mapMat = []

    # initialize map with 0 background
    for i in range(dimx):
        tmp = []
        for j in range(dimy):
            tmp.append(0.)
        mapMat.append(tmp)
        
    # add blobs
    rdx = [(int) (math.floor(x * (dimx-1))) for x in np.random.random_sample(n_blobs)]
    rdy = [(int) (math.floor(y * (dimy-1))) for y in np.random.random_sample(n_blobs)]
    points = zip(rdx, rdy)

    volumes = []
    for j in range(len(points)):
        volumes.append(0.)
        
    k = 0
    
    for center_x, center_y in points:
        
        width_x = math.floor(min([dimx, dimy])/float(10*np.random.randint(2,5))) * (1 + np.random.random()) 
        width_y = math.floor(min([dimx, dimy])/float(10*np.random.randint(2,5))) * (1 + np.random.random())
        col = elevation * (1 + (np.random.random()))
        
        if(oriented):
            
            gauss_ = gaussian_oriented(col, center_x, center_y, width_x, width_y)(Xin,Yin)
  
        else:
            
            gauss_ = gaussian(col, center_x, center_y, width_x, width_y)(Xin,Yin)
            
        for i in range(dimx):
            for j in range(dimy):
                mapMat[i][j] += gauss_[i][j]
                volumes[k] += gauss_[i][j]

        k += 1
        
    return mapMat, points, volumes
	
	
	
	
def plotHeatMap(mat):
    '''
    Plot heatmap with intensity matrix mat (color depends on intensity)
    '''
     
    nrows = len(mat)
    ncols = len(mat[0])

    mat = adjustMat(nrows, ncols,mat)
        
    x = arange(0, nrows+1, 1)
    y = arange(0, ncols+1, 1)
    X,Y = meshgrid(x,y)
     
    z = [tuple(mat[i]) for i in range(nrows)]
    zzip = zip(*z)

    pl.pcolor(X,Y,zzip)
    pl.colorbar()
    pl.axis([0,nrows,0,ncols]) ## modified
    pl.show()

	
	
def adjustMat(size1, size2, mat):
    '''
    Shrink matrix to desired size
    Zero padding
    '''
    if(len(mat) >= size1):
        mat = mat[:size1]
    else: # zero padding
        for i in range(len(mat), size1):
            mat.append([0]*size2)
                
    matTmp = []
    for i in range(size1):
        if(len(mat[i])==size2):
            matTmp.append([x for x in mat[i]])
        elif(len(mat[i])>size2):
            tmp = []
            for j in range(size2):
                tmp.append(mat[i][j])
            matTmp.append([x for x in tmp])
        else:
            tmp = []
            for j in range(len(mat[i])):
                tmp.append(mat[i][j])
            matTmp.append([x for x in tmp]+[0]*(size2-len(mat[i])))

    return matTmp
	
	
	
def gaussian(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)
    return lambda x,y: height*np.exp(-(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)
	
def gaussian_oriented(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)
    return lambda x,y: height*np.exp(-(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2+np.random.random()*np.random.randint(-1,2)*((center_x-x)/width_x)*((center_y-y)/width_y))/2)

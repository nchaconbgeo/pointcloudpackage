import numpy as np
from PIL import Image
from skimage.morphology import flood_fill

import time

class Projection:
    points = []
    IMAGE_SIZE_X = 1920
    IMAGE_SIZE_Y = 1080
    MAX_INDEX_X = IMAGE_SIZE_X - 1
    MAX_INDEX_Y = IMAGE_SIZE_Y - 1

    FILL_COLOR = 255
    CANVAS_COLOR = 0

    OFFSETS = (np.asarray((1, 0), dtype = int), np.asarray((-1, 0), dtype = int), np.asarray((0, 1), dtype = int), np.asarray((0, -1), dtype = int))


    toPixel = np.asarray((MAX_INDEX_X, MAX_INDEX_Y))
    data = None

    #normalize the direction so that the the larger coordinate has a magnitude of 1 and the smaller coordinate has a magnitude less than 1
    #also return the step count as the second tuple element
    def increment(self, direction):
        if(abs(direction[0]) > abs(direction[1])):
            return (np.asarray((np.sign(direction[0]), direction[1] / abs(direction[0]))), int(abs(direction[0])))
        else:
            return (np.asarray((direction[0] / abs(direction[1]), np.sign(direction[1]))), int(abs(direction[1])))

    def drawLine(self, p1, p2):
        p1Pixel = np.clip(np.rint(p1 * Projection.toPixel), 1, Projection.MAX_INDEX_X - 1)
        p2Pixel = np.clip(np.rint(p2 * Projection.toPixel), 1, Projection.MAX_INDEX_X - 1)
        direction = p2Pixel - p1Pixel
        increment = self.increment(direction)
        pos = np.asarray(p1Pixel, dtype=np.float64)
        for i in range(increment[1]):
            pos += increment[0]
            self.data[round(pos[0]), round(pos[1])] = 255

        
        

    def __init__(self, points):
        self.points = points
        lastTime = time.time()
        self.data = np.zeros((Projection.IMAGE_SIZE_X,Projection.IMAGE_SIZE_Y), dtype = np.uint8)
        print("Time to create numpy array:", time.time() - lastTime)
        lastTime = time.time()

        for i in range(len(points) - 1):
            self.drawLine(points[i], points[i+1])
        self.drawLine(self.points[-1], self.points[0])

        print("Time to draw lines:", time.time() - lastTime)
        lastTime = time.time()

        #self.floodFill(np.asarray((0, 0), dtype = int))
        self.data = flood_fill(self.data, (0, 0), Projection.FILL_COLOR, connectivity=1)

        print("Time to flood fill:", time.time() - lastTime)
        lastTime = time.time()

        im = Image.fromarray(self.data)
        im.save("output.png", "PNG")

        print("Time to save file:", time.time() - lastTime)
        lastTime = time.time()

    def floodFill(self, origin):
        sources = [origin]

        while sources:
            pointCoordinates = sources.pop()
            if not ((pointCoordinates >= [0, 0]) & (pointCoordinates <= [Projection.MAX_INDEX_X, Projection.MAX_INDEX_Y])).all():
                continue
            if self.data[pointCoordinates[0], pointCoordinates[1]] != Projection.CANVAS_COLOR:
                continue

            self.data[pointCoordinates[0], pointCoordinates[1]] = Projection.FILL_COLOR
            sources.append(pointCoordinates + Projection.OFFSETS[0])
            sources.append(pointCoordinates + Projection.OFFSETS[1])
            sources.append(pointCoordinates + Projection.OFFSETS[2])
            sources.append(pointCoordinates + Projection.OFFSETS[3])


if(__name__ == "__main__"):
    points = ((0.40921306255714096, 0.3980571905296093), (0.13076036071113106, 0.24022055099603334), (0.8652827152524055, 0.3155552520088608), (0.6975741757329712, 0.8894532748453461), (0.4912523681609122, 0.42275059433298745), (0.056919691562803076, 0.4563131622495147))
    points = [np.asarray(p) for p in points]

    p = Projection(points)
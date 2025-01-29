from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData, maxItr = 200, hiddenLayerList = hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200,hiddenLayerList = hiddenLayers)

# def q5Test():
#     print ("Q5 Test\n")
#     print ("Now testing Pen Data\n")
#     iteration = 0
#     penDataList = []
#     while iteration < 5:
#         penNet, testAccuracy = testPenData()
#         penDataList.append(testAccuracy)
#         iteration += 1

#     print ("Max of the Pen Data is:", max(penDataList))
#     print ("Average of the Pen Data is:", average(penDataList))
#     print ("Standard Deviation of the Pen Data is:", stDeviation(penDataList))
#     print ("\n")

#     print ("Now testing Car Data\n")
#     iteration = 0
#     carDataList = []
#     while iteration < 5:
#         carNet, testAccuracy = testCarData()
#         carDataList.append(testAccuracy)
#         iteration += 1

#     print ("Max of the Car Data is:", max(carDataList))
#     print ("Average of the Car Data is:", average(carDataList))
#     print ("Standard Deviation of the Car Data is:", stDeviation(carDataList))
#     print ("\n")

# q5Test()
def printResults(results):
    print("MAX:     {}".format(max(results)))
    print("AVERAGE: {}".format(average(results)))
    print("STD:     {}".format(stDeviation(results)))

def q6():
    print("Q6")

    print("PENDATA")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(20, 41, 5):
        pen_results = []
        for _ in range(5):
            pen_results.append(testPenData([i])[1])
        print("PENDATA PERCEPTRON COUNT {}".format(i))
        printResults(pen_results)


    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("CARDATA")

    # for i in range(0, 41, 5):
    #     car_results = []
    #     for _ in range(5):
    #         car_results.append(testCarData([i])[1])
    #     print("CARDATA PEREPTRON COUNT {}".format(i))
    #     printResults(car_results)

q6()

import twoPoint.twoPercentage as twoPercentage
import twoPoint.twoPoints as twoPoints
import twoPoint.twoPointScatter as twoPointScatter


def updateTwoPoint():
    twoPointScatter.twoPointScatter()
    twoPoints.twoPoint()
    twoPercentage.twoPercentage()


if __name__ == '__main__':
    updateTwoPoint()

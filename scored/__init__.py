from scored import scoredScatter, scoredPercentage, scoreds, scoredRankTable


def updateScored():
    scoredScatter.scoredScatter()
    scoredPercentage.scoredPercentage()
    scoreds.scored()
    scoredRankTable.scoredRank()


if __name__ == '__main__':
    updateScored()

import sys
distanceA, distanceB, taxispeed, wait, walkspeed = map(int, input().split())


def getresult(distanceA, distanceB, taxispeed,
              wait, walkspeed ):
    timeA = wait + distanceA*1000/taxispeed
    timeB = distanceB*1000/walkspeed
    if timeA == timeB:
        return "same"
    elif timeA > timeB:
        return "Walk"
    else:
        return "Taxi"
result = getresult(distanceA, distanceB, taxispeed,
              wait, walkspeed)
print(result)
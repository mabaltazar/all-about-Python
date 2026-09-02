def equilateral(sides):
    return (
        sum(sides) > 2*max(sides) and
        len(set(sides)) == 1
    )


def isosceles(sides):
    return (
        sum(sides) > 2*max(sides) and
        len(set(sides)) < 3
    )
    
def scalene(sides):
    return (
        sum(sides) > 2*max(sides) and
        len(set(sides)) == 3
    )

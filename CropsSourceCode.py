values = {
(10.0, 6.3, 'Sandy Soil'): 'Corn',
(22.4, 6.5, 'Desert Soil'): 'Wheat',
(21.7, 5.8, 'Alluvial Soil'): 'Rice',
(16.9, 6.6, 'Loamy Soil'): 'Maize',
(22.5, 6.1, 'Loamy Soil'): 'Sweet Potatoes',
(19.5, 6.8, 'Volcanic Soil'): 'Coffee Beans',
(25.0, 5.0, 'Loamy Soil'): 'Tea Plants',
(25.3, 5.8, 'Clay Soil'): 'Tobacco',
(21.1, 6.2, 'Clay Soil'): 'Strawberries',
(30.4, 5.3, 'Alluvial Soil'): 'Jute'
}


def crops(temp, pH, soil, values, diffT = {}, diffP = {}, score = {}):

    for (a, b, c) in values:

        diffT[values[(a, b, c)]] = abs(temp - a)
        diffP[values[(a, b, c)]] = abs(pH - b)
        score[values[(a, b, c)]] = 0.5 if soil == c else 0

    sort = lambda lst: sorted(lst.items(), key = lambda t: t[1])
    sortT = sort(diffT)
    sortP = sort(diffP)

    def points(score, lst):

        largest = lst[-1][-1]
        for i in lst:
            
            currentV = i[1]
            value = (largest - currentV) / float(largest) # Max: 1
            score[i[0]] = score[i[0]] + value
            
        return score


    score = points(points(score, sortP), sortT) # Composite Function
    score = sort(score)
    score.reverse()
    return score


def main():
    
    loop = crops(33.4, 6.6, raw_input('Soil type: '), values)
    print 'The best crops are:'
    for i in loop: print i[0] + ':', i[-1]


if __name__ == '__main__': main()

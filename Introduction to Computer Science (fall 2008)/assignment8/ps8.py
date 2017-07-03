# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
import json
import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    #define the dictionary of the mapped courses
    subjects_dic = {}
    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    for line in inputFile:
        #remove the white space from eachline
        line = line.strip()
        #split the line to a list of items
        line = line.split(',')
        #the first value should be a string which is the name of the course
        subjects_dic[line[0]] = int(line[1]),int(line[2])        
        #inside the the name of the course is a tuble with the value and hours

    return subjects_dic
        
    # done: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).




def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    #find the minimum value of the working hours so we can stop when we hit it.
    subjects_keys = subjects.keys()
    work_hours = []
    for key in subjects_keys:
        work_hours.append(subjects[key][1])
    minimum_working_hours = min(work_hours)
    #introduce answer and condition with true
    chosen_subjects = {}
    #introduce iterator
    i = 1
    hold = 0
    #do a while maxwork is bigger than 0
    while maxWork > 0:
        #build the keys list
        keys = subjects.keys()
        print 'list length is ',len(keys), 'and iterator is at ',i
        #check if the list is only one item than we are done
        if len(keys) == 1:
            #can we still add this item to the chosen subjects?
            if subjects[keys[0]][1] <= maxWork:
                    maxWork = maxWork - subjects[keys[hold]][1]
                    print 'Max work is now ', maxWork
                    chosen_subjects[keys[hold]] = subjects[keys[hold]]
                    del subjects[keys[hold]]
                    print chosen_subjects
                    return chosen_subjects
            #if not return the chosen subjects list
            else:
                print chosen_subjects
                return chosen_subjects
            
        #check the first two items of the subjects
        max_value = comparator(subjects[keys[hold]],subjects[keys[i]])
        #if the first item is bigger continue with comparision
        #and make sure the list is not over
        if max_value == True:
            print subjects[keys[hold]],subjects[keys[i]],'comparision is true'
            print 'max work is ',maxWork
            
            #check if we have reached the end of the list
            if i + 1 >= len(keys):
                #if the value is bigger than max work delete the course from the list
                if subjects[keys[hold]][1] > maxWork:
                    i = 1
                    hold = 0
                    print 'Removed ', subjects[keys[hold]]
                    del subjects[keys[hold]]
                    continue
                #if we have than minus from max work(if possible) and add the subject to chosen
                if subjects[keys[hold]][1] <= maxWork:
                    maxWork = maxWork - subjects[keys[hold]][1]
                    print 'Max work is now ', maxWork
                    chosen_subjects[keys[hold]] = subjects[keys[hold]]
                    if maxWork < minimum_working_hours:
                        print 'luckely ended computation earlier because of low MaxWork'
                        print chosen_subjects
                        return chosen_subjects
                        
                    #remove this item because it's bigger than maxwork now
                    del subjects[keys[hold]]
                    #reset the counters to start comparing
                    i = 1
                    hold = 0
                    continue
            #continue iteration if no valid situation is found
            i += 1
                
        #if the second item is bigger(false) make the holder the second item
        #check first to make sure we are not at the end of the list
        #if we are at the end of the list than we need to make the second decision tree with a
        #take of the values on the other hand
        if max_value == False:
            print subjects[keys[hold]],subjects[keys[i]],'comparision is false'
            if i + 1 >= len(keys):
                #if the value is bigger than max work delete the course from the list
                if subjects[keys[i]][1] > maxWork:
                    i = 1
                    hold = 0
                    print 'Removed ', subjects[keys[i]]
                    del subjects[keys[i]]
                    continue
                #if we have than minus from max work(if possible) and add the subject to chosen
                if subjects[keys[i]][1] <= maxWork:
                    maxWork = maxWork - subjects[keys[i]][1]
                    print 'Max work is now ', maxWork
                    chosen_subjects[keys[i]] = subjects[keys[i]]
                    if maxWork < minimum_working_hours:
                        print 'luckely ended computation earlier because of low MaxWork'
                        print chosen_subjects
                        return chosen_subjects
                    #remove this item because it's bigger than maxwork now
                    del subjects[keys[i]]
                    #reset the counters to start comparing
                    i = 1
                    hold = 0
                    continue
            #continue iteration if no valid situation is found
            hold = i
            i += 1
            print 'next comparision is ', subjects[keys[hold]],subjects[keys[i]]

    return chosen_subjects
        
smallCatalog = {'6.00': (16, 8),'1.00': (7, 7),'6.01': (5, 3),'15.01': (9, 6)}
chosen = greedyAdvisor(smallCatalog, 15, cmpValue)
printSubjects(chosen)

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

if __name__ == '__main__':
    #subjects_dic = loadSubjects(SUBJECT_FILENAME)
    with open('data.txt') as json_data:
        subjects_dic = json.load(json_data)
    #printSubjects(subjects_dic)
    

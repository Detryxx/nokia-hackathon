import ast


def input_days(input_file):                                     #makes the input file into a dictionary containing the codes as the key and the events as the value for each respective days' code
    with open(input_file, "r") as file:
        file_content = file.read()
        try:
            day = ast.literal_eval(file_content)                    #actually does the conversion
        except SyntaxError:
            pass

    return {tuple(codes): events for codes, events in day}      #returns the dict of the days


def fewest_unknown(could_be, assigned):                         #checks which code has the fewest possible events
    min_cand = float("inf")                                     #minimum candidates are infinite which is the worst case
    selected = None

    for code in could_be:
        if code not in assigned:                                #it checks wether or not an item in could_be is in assigned
            cands = len(could_be[code])                         #counts events left
            if cands < min_cand:
                min_cand = cands
                selected = code

    return selected                                             #returns the best one


def backtrack(could_be, assigned):
    if all(code in assigned for code in could_be):              #if everything has been assigned, were good and it returns the solution
        return assigned

    best_code = fewest_unknown(could_be, assigned)              #chucks the things into the fewest_unknown func and that does what the name implies

    for event in could_be[best_code]:                           #tries to assign the events
        assigned[best_code] = event
        result = backtrack(could_be, assigned)                  #continue with the assignment recursively
        if result is not None:                                  #if it found the solution-
            return result                                       #it returns the result

        del assigned[best_code]                                 #if we didnt succeed, it undoes the assignment

    return None                                                 #if there are no valid assignments it cant find the solution


def decoder(input_file):
    """
    this is the like initinal decoder but it also decodes the whole decoding thing using another function
    it takes the input file,  throws that into the like file reading function and using that,
    it tries to solve it, and which it could get passed into the decoded dict, and if it could find it,
    it passes the cb4a - which is could_be for assignment - and the already decoded stuff to the bakctrack function
    """
    days = input_days(input_file)                               #makes use of the input_days func to exctract data
    could_be = {}                                               #initial - not too sure about codes and event pairs
    decoded = {}                                                #the stuff that is 100% good

    for codes, events in days.items():
        event_tup = set(events)                                 #converts the events into a tuple for faster processing
        for code in codes:
            if code not in could_be:
                could_be[code] = event_tup.copy()               #it assumes that code corresponds to every event that day
            else:
                could_be[code] &= event_tup                     #only keeps events that it sees on the same day that the code appears

    for k, v in could_be.items():                               #if it only has one candidate, it counts it as immediately decoded
        if len(v) == 1:
            decoded[k] = next(iter(v))

    while True:                                                 #try to get better assignments
        are_we_getting_any_closer = False                       #assuemes we hit a dead end
        for code, events_tup in days.items():
            if code not in decoded and len(events) == 1:        #if only one code appears with one event, it assumes its correct
                event = events_tup
                decoded[code] = event
                are_we_getting_any_closer = True
        if not are_we_getting_any_closer:
            break                                               #if no new codes can be decoded, it stops

    cb4a = could_be.copy()                                      #copies the could_be dict for the backtrack func
    for entries in could_be:
        if entries in decoded:                                  #removes things from the cb4a dict if theyre decoded
            cb4a.pop(entries)

    decoded = backtrack(cb4a, decoded)                          #uses the backtrack func to decode the remaining events

    solution = "{\n"                                            #makes the solution pretty like in the readme
    for k, v in decoded.items():
        solution += f'    "{k}": "{v}",\n'
    solution += "}"

    return solution


print(decoder("./input.txt"))

"""
    ast - needed for literal_eval
"""
import ast


def input_days(input_file):
    """
        Keyword Args:
        input_file -- the input file

        Makes the input file into a dictionary containing the codes as the key and the events as the
        value for each respective days' code
    """
    with open(input_file, "r", encoding="utf-8") as file:
        file_content = file.read()

        day = ast.literal_eval(file_content)    #actually does the conversion

    return {tuple(codes): events for codes, events in day}  #returns the dict of the days


def fewest_unknown(could_be, assigned):
    """
        Checks which code has the fewest possible events

        Keyword Args:
        could_be -- the code that hasn't been assigned
        assigned -- the code that has been assigned

        It starts off with the worst case scenario, which is infinite events assigned to a code,
        then it preforms a check for codes in could_be that are also in assigned.
        It then counts the events for that code and sets the minimum candidates to that number, and
        it does this for all the codes.
        After that it returns the selected which is the code that has the fewest possible events.
    """
    min_cand = float("inf") #minimum candidates are infinite which is the worst case
    selected = None

    for code in could_be:
        if code not in assigned:    #it checks whether an item in could_be is in assigned
            cands = len(could_be[code]) #counts events for that code
            if cands < min_cand:
                min_cand = cands
                selected = code

    return selected #returns the best one


def backtrack(could_be, assigned):
    """
        Backtracks to the code with the fewest events and tries to solve it

        Keyword Args:
        could_be -- the codes the decoder couldn't solve
        assigned -- the codes the decoder knows for sure

        Checks if everything has been assigned yet, if yes it returns the assigned, if not
        it finds the code we're the most confident in meaning it has the least events associated
        with it. It then plugs the events into itself recursively, and if it found the solution it
        returns it. If it didn't find a solution it deletes that from the assigned.
        If it couldn't find a solution it returns None.
    """
        #if everything has been assigned, were good and it returns the solution
    if all(code in assigned for code in could_be):
        return assigned

        #plugs the things into the fewest_unknown func and that does what the name implies
    best_code = fewest_unknown(could_be, assigned)

    for event in could_be[best_code]:   #tries to assign the events
        assigned[best_code] = event
        result = backtrack(could_be, assigned)  #continue with the assignment recursively
        if result is not None:  #if it found the solution
            return result   #it returns the result

        del assigned[best_code] #if we didn't succeed, it undoes the assignment

    return None #if there are no valid assignments it cant find the solution


def decoder(input_file):
    """
        Initial decoder, uses the backtrack function to decode the rest

        Keyword Args:
            input_file -- the input file

        Tries to decode the file by finding a code that can only correspond to one event, by that I
        mean that it assumes a code is responsible for all events that happened that day, and by
        narrowing it down by excluding events that didn't happen when the code was sent. It then
        puts those into the decoded dictionary.
        After that, it plugs the 'cb4a' list - which means could_be for assignment - into the
        backtrack function. That then returns the things it could decode.
        The solution is then printed as per the readme.
    """
    days = input_days(input_file)   #makes use of the input_days func to extract data
    could_be = {}   #initial - not too sure about codes and event pairs
    decoded = {}    #the stuff that is 100% good

    for codes, events in days.items():
        event_tup = set(events) #converts the events into a tuple for faster processing
        for code in codes:
            if code not in could_be:
                    #it assumes that code corresponds to every event that day
                could_be[code] = event_tup.copy()
            else:
                    #only keeps events that it sees on the same day that the code appears
                could_be[code] &= event_tup

        #if it only has one candidate, it counts it as immediately decoded
    for k, v in could_be.items():
        if len(v) == 1:
            decoded[k] = next(iter(v))

    while True: #try to get better assignments
        are_we_getting_any_closer = False   #assuemes we hit a dead end
        for code, events_tup in days.items():
                #if only one code appears with one event, it assumes its correct
            if code not in decoded and len(events) == 1:
                event = events_tup
                decoded[code] = event
                are_we_getting_any_closer = True
        if not are_we_getting_any_closer:
            break   #if no new codes can be decoded, it stops

    cb4a = could_be.copy()  #copies the could_be dict for the backtrack function
    for entries in could_be:
        if entries in decoded:  #removes things from the cb4a dict if they're decoded
            cb4a.pop(entries)

    decoded = backtrack(cb4a, decoded)  #uses the backtrack function to decode the remaining events

    solution = "{\n"    #makes the solution pretty just like in the readme
    items = list(decoded.items())
    for i, (k, v) in enumerate(items):
        if i == len(items) - 1:
            solution += f'    "{k}": "{v}"\n'
        else:
            solution += f'    "{k}": "{v}",\n'

    solution += "}"

    return solution


print(decoder("./input.txt"))

def print_directory_contents(sPath):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    import os
    print os.listdir(sPath)
    for folder in os.listdir(sPath):
        #print(os.path.join(sPath,folder))
        ch = os.path.join(sPath,folder)
        if os.path.isdir(ch):
            print_directory_contents(ch)
        else:
            print ch



print_directory_contents('C:\Users')
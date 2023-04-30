# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def find_caller(self):
   
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """

    current_frame = currentframe()

    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.

    if current_frame is not None:
        current_frame = current_frame.f_back

    rv = "(unknown file)", 0, "(unknown function)"

    while hasattr(current_frame, "f_code"):

        co = current_frame.f_code
        filename = os.path.normcase(co.co_filename)

        if filename == _source_file:
            current_frame = current_frame.f_back
        
        else:
            rv = (co.co_filename, current_frame.f_lineno, co.co_name)
            return rv



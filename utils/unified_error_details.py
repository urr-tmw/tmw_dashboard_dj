import os, sys
def format_exception_message():
    """Capture and format exception details."""
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return (
        f"Exception Type: {exc_type.__name__}\n"
        f"FileName: {fname}\n"
        f"Code Line no: {exc_tb.tb_lineno}\n"
        f"Exact Error: {str(exc_obj)}"
    )
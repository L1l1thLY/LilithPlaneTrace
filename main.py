from LPTrace.LPTrace import LPTrace
import getpass
if __name__ == '__main__':
    password = getpass.unix_getpass("Input database password")
    lpt = LPTrace(db_password=password, start_index=7)
    lpt.generate_trace()
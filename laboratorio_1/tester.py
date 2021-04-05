
import traceback
import sys
import os
import tarfile



    


def test_summary(dispindex, ntests):
    return "Test %d/%d" % (dispindex, ntests)

def show_result(testsummary, testcode, correct, got, expected, verbosity):
    if correct:
        if verbosity > 0:
            print( "%s: Correct." % testsummary)
        if verbosity > 1:
            print( '\t', testcode)
            print()
    else:
        print( "%s: Incorrect." % testsummary)
        print( '\t', testcode)
        print( "Got:     ", got)
        print( "Expected:", expected)

def show_exception(testsummary, testcode):
    print( "%s: Error." % testsummary)
    print( "While running the following test case:")
    print( '\t', testcode)
    print( "Your code encountered the following error:")
    traceback.print_exc()
    print


def get_lab_module():
    lab = None

    # Try the easy way first
    try:
        from tests import lab_number
        lab = __import__('lab%s' % lab_number)
    except ImportError:
        pass

    for labnum in xrange(6):
        try:
            lab = __import__('lab%s' % labnum)
        except ImportError:
            pass

    if lab == None:
        raise ImportError( "Cannot find your lab; or, error importing it.  Try loading it by running 'python labN.py' (for the appropriate value of 'N').")

    if not hasattr(lab, "LAB_NUMBER"):
        lab.LAB_NUMBER = labnum
    
    return lab

def xrange(*args, **kwargs):
    return iter(range(*args, **kwargs))
    
def run_test(test, lab):
    id, type, attr_name, args = test
    attr = getattr(lab, attr_name)

    if type == 'VALUE':
        return attr
    elif type == 'FUNCTION':
        return attr(*args)
    else:
        raise Exception( "Test Error: Unknown TYPE '%s'.  Please make sure you have downloaded the latest version of the tester script.  If you continue to see this error, contact a TA.")


def test_offline(verbosity=1):
    import tests as tests_module
    test_names = list(tests_module.__dict__.keys())
    test_names.sort()

    tests = [ (x[:-8],
               getattr(tests_module, x),
               getattr(tests_module, "%s_testanswer" % x[:-8]),
               getattr(tests_module, "%s_expected" % x[:-8]),
               "_".join(x[:-8].split('_')[:-1]))
              for x in test_names if x[-8:] == "_getargs" ]
    
    ntests = len(tests)
    ncorrect = 0
    
    for index, (testname, getargs, testanswer, expected, fn_name) in enumerate(tests):
        dispindex = index+1
        summary = test_summary(dispindex, ntests)

        if getargs == 'VALUE':
            type = 'VALUE'
            getargs = lambda: getattr(get_lab_module(), testname)
            fn_name = testname
        else:
            type = 'FUNCTION'
            
        try:
            answer = run_test((0, type, fn_name, getargs()), get_lab_module())
            correct = testanswer(answer)
        except Exception:
           
            show_exception(summary, testname)
            continue
        
        show_result(summary, testname, correct, answer, expected, verbosity)
        if correct: ncorrect += 1
    
    print ("Passed %d of %d tests." % (ncorrect, ntests))
    return ncorrect == ntests




    





if __name__ == '__main__':
    test_offline()

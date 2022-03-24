import os
import inspect as sys_inspect
import warnings
from functools import wraps
from parameterized.parameterized import inspect
from parameterized.parameterized import parameterized
from parameterized.parameterized import default_doc_func
from parameterized.parameterized import default_name_func
from parameterized.parameterized import skip_on_empty_helper
from parameterized.parameterized import reapply_patches_if_need
from parameterized.parameterized import delete_patches_if_need
from parameterized import parameterized_class
from Easyauto.testdata import conversion
from Easyauto.logging.exceptions import FileTypeError

__all__ = [
    'file_data', 'data', 'data_class'
]


def file_data(file, line=1, sheet='Sheet1', key=None):
    '''
    Support file parameterization.

    d.json
    ```json
    {
     'login':  [
        ['admin', 'admin123'],
        ['guest', 'guest123']
     ]
    }
    ```
    >>  @file_data(file='d.json', key='login')
    ... def test_case(self, username, password):
    ...     print(username)
    ...     print(password)
    '''
    if file is None:
        raise FileExistsError('File name does not exist.')

    stack_t = sys_inspect.stack()
    ins = sys_inspect.getframeinfo(stack_t[1][0])
    file_dir = os.path.dirname(os.path.abspath(ins.filename))

    if os.path.isfile(file) is True:
        file_path = file
    elif '/' in file or '\\' in file:
        file = file.replace('\\', '/')
        current_dir = os.path.join(file_dir, file)
        parent_dir = os.path.join(os.path.dirname(file_dir), file)
        parent_dir_dir = os.path.join(os.path.dirname(os.path.dirname(file_dir)), file)
        parent_dir_dir_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(file_dir))), file)
        parent_dir_dir_dir_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_dir)))), file)

        if os.path.isfile(current_dir) is True:
            file_path = current_dir
        elif os.path.isfile(parent_dir) is True:
            file_path = parent_dir
        elif os.path.isfile(parent_dir_dir) is True:
            file_path = parent_dir_dir
        elif os.path.isfile(parent_dir_dir_dir) is True:
            file_path = parent_dir_dir_dir
        elif os.path.isfile(parent_dir_dir_dir_dir) is True:
            file_path = parent_dir_dir_dir_dir
        else:
            raise FileExistsError(f'No "{file}" data file found.')
    else:
        file_path = None
        find_dir = os.path.dirname(file_dir)
        for root, dirs, files in os.walk(find_dir, topdown=False):
            for f in files:
                if f == file:
                    file_path = os.path.join(root, file)
                    break
            else:
                continue
            break

        if file_path is None:
            raise FileExistsError(f'No "{file}" data file found.')

    suffix = file.split('.')[-1]
    if suffix == 'csv':
        data_list = conversion.csv_to_list(file_path, line=line)
    elif suffix == 'xlsx':
        data_list = conversion.excel_to_list(file_path, sheet=sheet, line=line)
    elif suffix == 'json':
        data_list = conversion.json_to_list(file_path, key=key)
    elif suffix == 'yaml':
        data_list = conversion.yaml_to_list(file_path, key=key)
    else:
        raise FileTypeError(f'Your file is not supported: {file}')

    return data(data_list)


def data(input, name_func=None, doc_func=None, skip_on_empty=False, **legacy):
    ''' A 'brute force' method of parameterizing test cases. Creates new
        test cases and injects them into the namespace that the wrapped
        function is being defined in. Useful for parameterizing tests in
        subclasses of 'UnitTest', where Nose test generators don't work.

        >> @data([('foo', 1, 2)])
        ... def test_add1(name, input, expected):
        ...     actual = add1(input)
        ...     assert_equal(actual, expected)
        ...
        >> locals()
        ... 'test_add1_foo_0': <function ...> ...
        >>
        '''

    if 'testcase_func_name' in legacy:
        warnings.warn('testcase_func_name= is deprecated; use name_func=',
                      DeprecationWarning, stacklevel=2)
        if not name_func:
            name_func = legacy['testcase_func_name']

    if 'testcase_func_doc' in legacy:
        warnings.warn('testcase_func_doc= is deprecated; use doc_func=',
                      DeprecationWarning, stacklevel=2)
        if not doc_func:
            doc_func = legacy['testcase_func_doc']

    doc_func = doc_func or default_doc_func
    name_func = name_func or default_name_func

    def parameterized_expand_wrapper(f, instance=None):
        frame_locals = inspect.currentframe().f_back.f_locals

        parameters = parameterized.input_as_callable(input)()

        if not parameters:
            if not skip_on_empty:
                raise ValueError(
                    'Parameters iterable is empty (hint: use '
                    '`parameterized.expand([], skip_on_empty=True)` to skip '
                    'this test when the input is empty)'
                )
            return wraps(f)(skip_on_empty_helper)

        digits = len(str(len(parameters) - 1))
        for num, p in enumerate(parameters):
            name = name_func(f, '{num:0>{digits}}'.format(digits=digits, num=num), p)
            # If the original function has patches applied by 'mock.patch',
            # re-construct all patches on the just former decoration layer
            # of param_as_standalone_func so as not to share
            # patch objects between new functions
            nf = reapply_patches_if_need(f)
            frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
            frame_locals[name].__doc__ = doc_func(f, num, p)

        # Delete original patches to prevent new function from evaluating
        # original patching object as well as re-constructed patches.
        delete_patches_if_need(f)

        f.__test__ = False

    return parameterized_expand_wrapper


def data_class(attrs, input_values):
    '''
    Parameterizes a test class by setting attributes on the class.
    '''
    return parameterized_class(attrs, input_values)


import sys,os
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)
import Easyauto

class SampleTest(Easyauto.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("http://www.itest.info")
       
        print('test_case')


if __name__ == '__main__':
    Easyauto.main(debug=True)
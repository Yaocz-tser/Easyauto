
import sys,os
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)
import Easyauto

class SampleTest(Easyauto.TestCase):
    # 这是分支提交 2022年3月23日11:45:52
    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
       
        self.assertElement(css="#kw")

if __name__ == '__main__':
    Easyauto.main(debug=True)
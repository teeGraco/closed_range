from main.closedsection import ClosedSection, InputTypeError, InputValueError
import pytest



class Test_2整数を入力すると閉区間インスタンスを生成する確認:
    def test_２つの整数3と5を入力とするインスタンスを生成するクラスの作成ができることの確認(self):
        closed_section = ClosedSection(3,5)
        assert isinstance(closed_section, ClosedSection), "正しいインスタンスが生成されていません。"
    
    def test_２つの整数3と3を入力とするインスタンスを生成するクラスの作成ができることの確認(self):
        closed_section = ClosedSection(3,3)
        assert isinstance(closed_section, ClosedSection), "正しいインスタンスが生成されていません。"        

    def test_２つの小数1_2と1_7を入力をするとInputTypeErrorを出力(self):
        with pytest.raises(InputTypeError):
            closed_section = ClosedSection(1.2,1.7)

    def test_上端点より下端点が大きい入力5と3の場合はInputValueErrorを出力(self):
        with pytest.raises(InputValueError):
            closed_section = ClosedSection(5,3)
    
class Test_整数閉区間オブジェクトは文字列表現を返せる:
    @pytest.fixture
    def initialize(self):
        closed_section = ClosedSection(3,5)
        return closed_section

    def test_入力3と5に対して閉区間情報35を出力する(self, initialize):
        assert initialize.stringify() == "[3,5]", "異なる文字列が返っています。"
    
    def test_入力3と5に対して下端値3を返す関数getLower(self, initialize):
        assert initialize.getLower() == 3, "期待した値3以外の値が返っています。"

    def test_入力3と5に対して上端値5を返す関数getUpper(self,initialize):
        assert initialize.getUpper() == 5, "期待した値5以外の値が返っています。"   

class Test_整数の閉区間は指定した整数を含むかどうかを判定できる:
    @pytest.fixture
    def initialize(self):
        closed_section = ClosedSection(3,7)
        return closed_section

    def test_入力3と7に対して2が含まれない(self,initialize):
        assert initialize.is_element_of(2) == False, "閉区間[3,7]の中に2が含まれることになっています。"
    
    def test_入力3と7に対して3が含まれる(self,initialize):
        assert initialize.is_element_of(3) == True, "閉区間[3,7]の中に3が含まれないことになっています。"
    
    def test_入力3と7に対して7が含まれる(self,initialize):
        assert initialize.is_element_of(7) == True, "閉区間[3,7]の中に7が含まれないことになっています。"

    def test_入力3と7に対して8が含まれない(self,initialize):
        assert initialize.is_element_of(8) == False, "閉区間[3,7]の中に8が含まれることになっています。"

class Test_整数の閉区間は別の閉区間と等価かどうかを判定できる:
    @pytest.fixture
    def compare(self):
        closed_section = ClosedSection(3,5)
        return closed_section

    def test_入力3と5は入力3と5と等価である(self,compare):
        closed_section = ClosedSection(3,5)
        assert compare.equals(closed_section), "[3,5]と[3,5]が等価でないことになっています。"

    def test_入力3と5は入力3と7と等価ではない(self,compare):
        closed_section = ClosedSection(3,7)
        assert compare.equals(closed_section) == False, "[3,5]と[3,7]が等価になっています。"    

    def test_入力3と5は入力1と5と等価ではない(self,compare):
        closed_section = ClosedSection(1,5)
        assert compare.equals(closed_section) == False, "[3,5]と[1,5]が等価になっています。"  

    def test_入力3と5は入力1と7と等価ではない(self,compare):
        closed_section = ClosedSection(1,7)
        assert compare.equals(closed_section) == False, "[3,5]と[1,7]が等価になっています。"  

    def test_入力3と5に対して異なるクラスのインスタンスと比較された場合例外を返す(self,compare):
        with pytest.raises(NotImplementedError):
            compare.equals("[3,5]"), "入力がinvalidです。" 

class Test_整数の閉区間は別の閉区間に完全に含まれるかどうかを判定できる:
    @pytest.fixture
    def compare(self):
        closed_section = ClosedSection(3,7)
        return closed_section
    
    def test_入力3と4は入力3と7に含まれる(self,compare):
        closed_section = ClosedSection(3,4)
        assert compare.includes(closed_section) == True, "入力3と4は入力3と7に含まれる"
    
    def test_入力4と6は入力3と7に含まれる(self,compare):
        closed_section = ClosedSection(4,6)
        assert compare.includes(closed_section) == True, "入力4と6は入力3と7に含まれる"

    def test_入力4と7は入力3と7に含まれる(self,compare):
        closed_section = ClosedSection(4,7)
        assert compare.includes(closed_section) == True, "入力4と7は入力3と7に含まれる"

    def test_入力3と7は入力3と7に含まれる(self,compare):
        closed_section = ClosedSection(3,7)
        assert compare.includes(closed_section) == True, "入力3と7は入力3と7に含まれる"

    def test_入力1と7は入力3と7に含まれない(self,compare):
        closed_section = ClosedSection(1,7)
        assert compare.includes(closed_section) == False, "入力1と7は入力3と7に含まれない"

    def test_入力3と9は入力3と7に含まれない(self,compare):
        closed_section = ClosedSection(3,9)
        assert compare.includes(closed_section) == False, "入力3と9は入力3と7に含まれない"

    def test_入力1と2は入力3と7に含まれない(self,compare):
        closed_section = ClosedSection(1,2)
        assert compare.includes(closed_section) == False, "入力1と2は入力3と7に含まれない"

    def test_入力8と9は入力3と7に含まれない(self,compare):
        closed_section = ClosedSection(8,9)
        assert compare.includes(closed_section) == False, "入力8と9は入力3と7に含まれない"

    def test_入力3と5に対して異なるクラスのインスタンスと比較された場合例外を返す(self,compare):
        with pytest.raises(NotImplementedError):
            compare.includes("[3,5]"), "入力がinvalidです。" 

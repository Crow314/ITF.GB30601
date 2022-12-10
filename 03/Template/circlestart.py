# 長方形を*で描く
from figure_template import FigureTemplate
from xyrange import XYRange


class CircleStarT(FigureTemplate):
    # 左下が(2.0, 2.0) で サイズが 5.0 x 3.0 の長方形
    def _inside(self, x: float, y: float) -> bool:
        return (x**2 + y**2) <= 3**2

    # 描画範囲は，xが[0.0, 7.0], 0.25刻み．yが[0.0, 6.0]，0.5刻み．
    def _get_range(self) -> XYRange:
        return XYRange(-5.0, 5.0, 0.25, -5.0, 5.0, 0.5)

    # 内側なら"*", 外側なら" "
    def _plot_inside(self):
        print("★", end="")

    def _plot_outside(self):
        print("　", end="")

    def _next_line(self):
        print("\n")


if __name__ == "__main__":
    CircleStarT().draw()

from abc import ABC, abstractmethod
from xyrange import XYRange


class PlotStar(ABC):
    def plot_inside(self) -> None:
        print("★", end="")

    def plot_outside(self) -> None:
        print("　", end="")

    def next_line(self) -> None:
        print("\n")

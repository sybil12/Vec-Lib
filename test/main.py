import sys
import argparse

# import other packages
sys.path.insert(0, '../common')
sys.path.insert(0, '../curve_fitting')

from PolyLine import *
from BezierCurve import *
from CurveFitGG import *
from test import *


def main():
    print("Start of the project")
    # error = 0.1
    # d = [
    #     [0.0, 0.0], [0.5, 0.5], [1.0, 1.0], [1.5, 1.5], [2.0, 1.5],
    #     [2.5, 1.0], [3.0, 0.5], [3.5, 0.5], [4.0, 1.0], [4.0, 1.5],
    #     [3.5, 2.0], [3.0, 2.5], [2.5, 3.0], [2.0, 3.0], [1.5, 2.5],
    #     [1.0, 2.5]
    # ]
    # poly = PolyLine(d)
    # poly.draw(show=True)
    # test = Test(None)
    # test.run_corner_detector_basic(d)

    # curve_fit = CurveFitGG(d, error)
    # b_curves = curve_fit.fit_curve()
    # for idx, curve in enumerate(b_curves):
    #    curve.draw_by_vladan(False if idx != len(b_curves)-1 else True)
    parser = argparse.ArgumentParser(description="Arguments that can be specified")
    parser.add_argument('-f', '--file', help='input contour')
    parser.add_argument('--input_poly', help="true if you want to see the original contour")
    parser.add_argument('--filtered_poly', help="true if you want to see the resampled contour")
    parser.add_argument('--corners', help="true if you want to see detected corners")

    args = parser.parse_args()

    disp_original_cont, disp_filtered_poly, disp_corners = False, False, False
    file_name = args.file
    if args.input_poly is not None:
        print(disp_original_cont)
        disp_original_cont = True
    if args.filtered_poly is not None:
        print(disp_filtered_poly)
        disp_filtered_poly = True
    if args.corners is not None:
        print(disp_corners)
        disp_corners = True

    test = Test(file_name)
    test.run_corner_detector_test(disp_original_cont, disp_filtered_poly, disp_corners)


    # test.run_test()
    # print "finished"


if __name__ == "__main__":
    main()
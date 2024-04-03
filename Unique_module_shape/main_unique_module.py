import Unique_module.shape as shape

def main():
    forma = shape.Shape([shape.Point(0,0), shape.Point(1,0), shape.Point(1,1), shape.Point(0,1)])
    for edge in forma.compute_edges():
        print(f"start = ({edge.get_start().get_x()}, {edge.get_start().get_y()}), end = ({edge.get_end().get_x()}, {edge.get_end().get_y()})")
    print(forma.compute_inner_angles())
    
if __name__ == "__main__":
    main()
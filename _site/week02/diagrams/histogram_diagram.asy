settings.outformat = "svg";
import is590lib;

unitsize(2cm);
srand(123456);

int ncircles = 32;
int[] ngrid = {8, 8};
int[] single_grid = {1, 1};
real[] canvas_size = {8, 8};
path[] empty_paths = {};
path[] circle_paths = {};

draw_grid(single_grid, canvas_size, black+linewidth(2.0), empty_paths, black);

path p = unitcircle;

for (int i = 0; i < ncircles - 1 ; ++i) {
  real x = unitrand() * canvas_size[0];
  real y = -unitrand() * canvas_size[1];
  path c = shift(x, y) * scale(2.0 / (ngrid[0])) * p;
  filldraw(c, mediumgray);
  circle_paths.push(c);
}

clip(box((0,0), (canvas_size[0], -canvas_size[1])));
shipout("circles.svg");

draw_grid(ngrid, canvas_size, black + linewidth(2.0), empty_paths, black);

clip(box((0,0), (canvas_size[0], -canvas_size[1])));
shipout("circles_grid.svg");

draw_grid(ngrid, canvas_size, black + linewidth(2.0), circle_paths, black);

clip(box((0,0), (canvas_size[0], -canvas_size[1])));
shipout("circles_grid_filled.svg");

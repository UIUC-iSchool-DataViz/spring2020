settings.outformat = "svg";
import is590lib;

unitsize(2cm);
srand(123456);

int ncircles = 32;
int[] og = {1, 1};
int[] ng = {8, 8};
real[] cs = {8, 8};
path[] empty_paths = {};
path[] paths = {};

path p = unitcircle;

for (int i = 0; i < ncircles - 1 ; ++i) {
  real x = unitrand() * cs[0];
  real y = -unitrand() * cs[1];
  real s = unitrand() * cs[0] / 8.0; 
  path c = shift(x, y) * scale(s * 2.0 / (ng[0])) * p;
  paths.push(c);
}

void draw_circles() {
  for (int i = 0; i < paths.length; ++i) {
    filldraw(paths[i], mediumgray);
  }
}

draw_grid(og, cs, black+linewidth(2.0), empty_paths, black);
filldraw( shift(4.0, -4.0) * scale(2.0) * p, mediumgray);
shipout("single_circle.svg");

erase();
draw_circles();
draw_grid(og, cs, black+linewidth(2.0), empty_paths, black);
shipout("dots.svg");

erase();
draw_grid(ng, cs, linewidth(1.0), empty_paths, gray);
draw_circles();
shipout("dots_grid.svg");

erase();
draw_grid(ng, cs, linewidth(1.0), paths, gray);
draw_circles();
shipout("dots_grid_fill.svg");

erase();
draw_grid(ng * 2, cs, linewidth(1.0), empty_paths, gray);
draw_circles();
shipout("dots_grid_fine2.svg");

erase();
draw_grid(ng * 2, cs, linewidth(1.0), paths, gray);
draw_circles();
shipout("dots_grid_fine2_fill.svg");

erase();
draw_grid(ng * 4, cs, linewidth(1.0), empty_paths, gray);
draw_circles();
shipout("dots_grid_fine4.svg");

erase();
draw_grid(ng * 4, cs, linewidth(1.0), paths, gray);
draw_circles();
shipout("dots_grid_fine4_fill.svg");

settings.outformat = "svg";
import is590lib;

unitsize(1.0cm);
srand(123456);

pair[] data_points = { (1, 4), (5.5, 2), (3, 5) };
pen[] color = {orange, cyan, purple};
real[] size = {2.5, 0.75, 1.5};
int[] sides = {3, 4, 5};


void draw_axes() {
  draw((0,0)--(0,7), arrow=Arrow, linewidth(2.0));
  draw((0,0)--(7,0), arrow=Arrow, linewidth(2.0));
}

erase();
draw_axes();

for (int i = 0; i < data_points.length; ++i) {
  path c = shift(data_points[i]) * scale(0.25) * unitcircle;
  filldraw(c, linewidth(1.5), fillpen = lightgray);
}

shipout("dimensions_1.svg");

erase();
draw_axes();

for (int i = 0; i < data_points.length; ++i) {
  path c = shift(data_points[i]) * scale(0.25) * unitcircle;
  filldraw(c, linewidth(1.5), fillpen = color[i]);
}

shipout("dimensions_2.svg");

erase();
draw_axes();

for (int i = 0; i < data_points.length; ++i) {
  path c = shift(data_points[i]) * scale(0.25 * size[i]) * unitcircle;
  filldraw(c, linewidth(1.5), fillpen = color[i]);
}

shipout("dimensions_3.svg");

erase();
draw_axes();

for (int i = 0; i < data_points.length; ++i) {
  path c = shift(data_points[i]) * scale(0.25 * size[i]) * polygon(sides[i]);
  filldraw(c, linewidth(1.5), fillpen = color[i]);
}
shipout("dimensions_4.svg");

erase();
draw_axes();

for (int i = 0; i < data_points.length; ++i) {
  path c = shift(data_points[i]) * scale(0.25 * size[i]) * polygon(sides[i]);
  filldraw(c, linewidth(1.5), fillpen = color[i]);
}

draw((data_points[0]--data_points[1]), p=linewidth(1.5), arrow=EndArrow, margin = Margin(5.0, 2.0));
draw((data_points[1]--data_points[2]), p=linewidth(1.5), arrow=EndArrow, margin = Margin(2.0, 2.5));

shipout("dimensions_5.svg");


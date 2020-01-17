settings.outformat = "svg";
import is590lib;

unitsize(1.0cm);
srand(123456);

// Make our bottom edge


void draw_binbox(int N) {

  draw((0,0)--(10,0), linewidth(2.0));
  real xdist = 10.0 / N;
  // We do N+1 here so that we get both sides
  for (int i = 0; i < N + 1; ++i){
    draw((xdist * i, 0)--(xdist*i,2), linewidth(2.0));
  }
  label("0.0", (0.0, 1.0), W);
  label("1.0", (10.0, 1.0), E);

  filldraw( shift((3.0, 1.0)) * scale(0.5) * unitcircle, fillpen = mediumgray);

}

draw_binbox(1);
shipout("binning_1.svg");
erase();

draw_binbox(5);
draw((0.0, 2.5)--(2.0, 2.5), arrow=Arrows, linewidth(2.0));
label("0.2", (1.0, 2.5), N);
shipout("binning_2.svg");
erase();

draw_binbox(1);
draw((1.0, 0.0)--(1.0, 2.0), linewidth(2.0));
draw((1.7, 0.0)--(1.7, 2.0), linewidth(2.0));
draw((1.9, 0.0)--(1.9, 2.0), linewidth(2.0));
draw((3.6, 0.0)--(3.6, 2.0), linewidth(2.0));
draw((7.4, 0.0)--(7.4, 2.0), linewidth(2.0));
draw((9.1, 0.0)--(9.1, 2.0), linewidth(2.0));
label("0.2", (1.0, 2.5), N);
shipout("binning_3.svg");

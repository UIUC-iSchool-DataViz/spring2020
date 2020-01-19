settings.outformat = "svg";
import is590lib;

unitsize(2cm);
srand(123456);

transform linetrans = rotate(-30);

path linepath = shift(2.0, -1.0) * ((0, 0) -- (6, 0));

int[] og = {1, 1};
int[] ng = {8, 8};
real[] cs = {8, 8};
path[] empty_paths = {};
path[] paths = {linetrans * linepath};

void draw_line() {
    draw(linetrans * linepath, linewidth(16.0) + squarecap + heavygray);

    pathlabel("$\{$", linetrans * linepath, position = 0.0, sloped = true,
              p = fontsize(24pt));
    pathlabel("$\}$", linetrans * linepath, position = 1.0, sloped = true,
              p = fontsize(24pt));

    draw( linetrans * ( shift(0, -1.25) * relpoint(linepath, 0.0) ..
                      ( shift(0, -0.25) * relpoint(linepath, 0.0))), 
                      linewidth(1.5) + heavygray, arrow=Arrow);

    draw( linetrans * ( shift(0, -1.25) * relpoint(linepath, 1.0) ..
                      ( shift(0, -0.25) * relpoint(linepath, 1.0))), 
                      linewidth(1.5) + heavygray, arrow=Arrow);
}

draw_grid(og, cs, linewidth(1.0), empty_paths, heavygray);
draw_line();
shipout("line.svg");

erase();
draw_grid(ng, cs, linewidth(1.0), empty_paths, gray);
draw_line();
shipout("line_grid.svg");

erase();
draw_grid(ng, cs, linewidth(1.0), paths, gray);
draw_line();
shipout("line_grid_fill.svg");

erase();
draw_grid(ng * 2, cs, linewidth(1.0), empty_paths, gray);
draw_line();
shipout("line_grid_fine2.svg");

erase();
draw_grid(ng * 2, cs, linewidth(1.0), paths, gray);
draw_line();
shipout("line_grid_fine2_fill.svg");

erase();
draw_grid(ng * 4, cs, linewidth(1.0), empty_paths, gray);
draw_line();
shipout("line_grid_fine4.svg");

erase();
draw_grid(ng * 4, cs, linewidth(1.0), paths, gray);
draw_line();
shipout("line_grid_fine4_fill.svg");

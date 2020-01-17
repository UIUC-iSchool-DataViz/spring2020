settings.outformat = "svg";
import is590lib;

unitsize(2cm);

int[] boxcolors = {0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1};
int nfill = 0;

for (int i = 0; i < 12 ; ++i ) {
  pen p = rgb("ffab40");
  if(boxcolors[i] == 1) {
    p = rgb("0097a7");
    ++nfill;
  }
  filldraw(shift(i, 0) * box( (0,0), (1, -1)),
           fillpen = p, drawpen = linewidth(4.0) + rgb("9e9e9e"));
}

shipout("split.svg");

draw((1.0, -1.125) -- (1.0, -2.375), arrow=Arrow, linewidth(4.0) + rgb("9e9e9e"));

for (int i = 0; i < nfill; ++i) {
  pen p = rgb("0097a7");
  filldraw(shift(i, -2.75) * box( (0,0), (1, -1)),
           fillpen = p, drawpen = linewidth(4.0) + rgb("9e9e9e"));

}

for (int i = 0; i < 12 - nfill; ++i) {
  pen p = rgb("ffab40");
  filldraw(shift(i, -4.25) * box( (0,0), (1, -1)),
           fillpen = p, drawpen = linewidth(4.0) + rgb("9e9e9e"));

}

shipout("split_finished.svg");

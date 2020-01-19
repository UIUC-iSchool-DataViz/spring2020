settings.outformat = "svg";
import is590lib;

unitsize(1.0cm);
srand(123456);


void draw_dots( transform tf ) {

  draw( ((-2,-2)--(-2,10)--(10,10)--(10,-2)--cycle), nullpen);
  draw( (0,0)--(0,7), arrow=Arrow, linewidth(2.0));
  draw( (0,0)--(7,0), arrow=Arrow, linewidth(2.0));

  path p = scale(0.25) * unitcircle;

  filldraw(tf * shift(3,3) * p, fillpen=mediumgray);
  filldraw(tf * shift(5,1) * p, fillpen=mediumgray);
  filldraw(tf * shift(4,2) * p, fillpen=mediumgray);
  filldraw(tf * shift(1,3) * p, fillpen=mediumgray);
  filldraw(tf * shift(6,4) * p, fillpen=mediumgray);
  filldraw(tf * shift(4,5) * p, fillpen=mediumgray);
  filldraw(tf * shift(2,3.5) * p, fillpen=mediumgray);

  draw( tf * ((0.5, 0.5) -- (6.5, 0.5) -- (6.5, 5.5) -- (0.5, 5.5) -- cycle),
         linewidth(1.5));
}

draw_dots( identity() );
shipout("affine_1.svg");

erase();
draw_dots( shift(2, 1));
shipout("affine_2.svg");

erase();
draw_dots( rotate(-15) * shift(2, 1));
shipout("affine_3.svg");

erase();
draw_dots( scale(0.5, 1.2) * rotate(-15) * shift(2, 1));
shipout("affine_4.svg");

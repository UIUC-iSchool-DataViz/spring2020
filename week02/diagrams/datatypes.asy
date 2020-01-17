settings.outformat = "png";
settings.render = 0;
import is590lib;
import three;
unitsize(2.0cm);

void draw_grid_face(triple origin, triple dim1, triple dim2,
                    int N1, int N2, pen meshpen, pen surfacepen) {

  for (int i = 0; i < N1; ++i) {
    for (int j = 0; j < N2; ++j) {
      draw(surface(
        (origin + dim1*(i  ) + dim2*(j  ))
      --(origin + dim1*(i+1) + dim2*(j  ))
      --(origin + dim1*(i+1) + dim2*(j+1))
      --(origin + dim1*(i  ) + dim2*(j+1))
      --cycle), meshpen=meshpen, surfacepen=surfacepen, light=nolight);
    }
  }
}

void draw_mesh_face_cube(real size = 5.0, int N = 5) {
  draw(scale3(size) * unitbox, linewidth(2.0));
  real d = size/N;
  triple xdir = (d, 0, 0);
  triple ydir = (0, d, 0);
  triple zdir = (0, 0, d);
  draw_grid_face( (0,0,0), xdir, ydir, N, N, linewidth(2.0), white);
  draw_grid_face( (0,0,0), xdir, zdir, N, N, linewidth(2.0), white);
  draw_grid_face( (0,0,0), ydir, zdir, N, N, linewidth(2.0), white);
  draw_grid_face( (size,0,0), ydir, zdir, N, N, linewidth(2.0), white);
  draw_grid_face( (0,size,0), xdir, zdir, N, N, linewidth(2.0), white);
  draw_grid_face( (0,0,size), xdir, ydir, N, N, linewidth(2.0), white);
}

draw_mesh_face_cube();
shipout("cube.png");

draw_grid_face((0,5,2), (0, 0, 1), (1, 0, 0), 1, 5, linewidth(2.0), blue);
draw_grid_face((5,0,2), (0, 0, 1), (0, 1, 0), 1, 5, linewidth(2.0), blue);

shipout("cube_z_slice.png");

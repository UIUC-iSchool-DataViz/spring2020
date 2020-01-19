Reveal.addEventListener('ready', function() {

  var vis2spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
    "description": "A scatterplot",
    "data": {"name": "table",
             "values": [ {"x": 1.0, "y": 2.0},
                         {"x": 2.0, "y": 1.0},
                         {"x": 3.0, "y": 9.0},
                         {"x": 4.0, "y": 8.0},
                         {"x": 5.0, "y": 6.0} ] },
    "mark": "point",
      "encoding": {
        "x": {"field": "x","type": "quantitative"},
        "y": {"field": "y","type": "quantitative"}
      }
  };
  var embedded2 = vegaEmbed('#vis2', vis2spec, {'actions': false});
  var embedded3 = vegaEmbed('#vis3', vis2spec, {'actions': false});
  var embedded4 = vegaEmbed('#vis4', vis2spec, {'actions': false});

    document.getElementById("button3").addEventListener("click", function onButtonClick(event) {
        var cs = vega.changeset()
            .insert( [
                {'x': 1.0, 'y': 10.0},
                {'x': 5.0, 'y': 1.3},
                {'x': 2.1, 'y': 0.7}
            ]);
        embedded3.then( function(res) {
            res.view.change('table', cs).run();

        });
    });

    document.getElementById("button4").addEventListener("click", function onButtonClick(event) {
        var cs = vega.changeset()
            .insert( [
                {'x': 1.0, 'y': 10.0},
                {'x': 5.0, 'y': 1.3},
                {'x': 2.1, 'y': 0.7}
            ])
            .remove( function(t) {
              return t.x < t.y;
            });
        embedded4.then( function(res) {
            res.view.change('table', cs).run();

        });
    });

});

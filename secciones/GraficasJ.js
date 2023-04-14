new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'myfirstchart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [
      { Fecha: '1', medición: 20 },
      { Fecha: '2', medición: 10 },
      { Fecha: '3', medición: 5 },
      { Fecha: '4', medición: 5 },
      { Fecha: '5', medición: 20 }
    ],
    // The name of the data record attribute that contains x-values.
    xkey: 'Fecha',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['medición'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    labels: ['Medición']
  });
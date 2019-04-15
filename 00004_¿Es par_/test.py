describe('', function() {
  it("es_par(2) es verdadero", function() {
    assert(es_par(2));
  });

  it("es_par(8) es verdadero", function() {
    assert(es_par(8));
  });

  it("es_par(9890) es verdadero", function() {
    assert(es_par(9890));
  });

  it("es_par(1) es falso", function() {
    assert(!es_par(1));
  });

  it("es_par(879) es falso", function() {
    assert(!es_par(879));
  });
})

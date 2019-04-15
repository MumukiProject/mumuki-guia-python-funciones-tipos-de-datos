describe("", function() {
  it("esta_entre(10, 1, 10) es False", function() {
    assert(!esta_entre(10, 1, 10));
  });
  it("esta_entre(4, 4, 9) es False", function() {
    assert(!esta_entre(4, 4, 9));
  });
  it("esta_entre(12, 1, 10) es False", function() {
    assert(!esta_entre(12, 1, 10));
  });
  it("esta_entre(200, 54, 112) es False", function() {
    assert(!esta_entre(200, 54, 112));
  });
  it("esta_entre(67, 0, 100) es True", function() {
    assert(esta_entre(67, 0, 100));
  });
  it("esta_entre(2, 0, 100) es True", function() {
    assert(esta_entre(2, 0, 100));
  });
})

describe("", function() {
  it("esta_fuera_de_rango(10, 1, 10) es False", function() {
    assert(!esta_fuera_de_rango(10, 1, 10));
  });
  it("esta_fuera_de_rango(4, 4, 9) es False", function() {
    assert(!esta_fuera_de_rango(4, 4, 9));
  });
  it("esta_fuera_de_rango(12, 1, 10) es True", function() {
    assert(esta_fuera_de_rango(12, 1, 10));
  });
  it("esta_fuera_de_rango(200, 54, 112) es True", function() {
    assert(esta_fuera_de_rango(200, 54, 112));
  });
  it("esta_fuera_de_rango(67, 0, 100) es False", function() {
    assert(!esta_fuera_de_rango(67, 0, 100));
  });
  it("esta_fuera_de_rango(2, 0, 100) es False", function() {
    assert(!esta_fuera_de_rango(2, 0, 100));
  });
})

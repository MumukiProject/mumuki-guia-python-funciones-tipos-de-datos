describe("", function() {
  it("cuanto_carga(10, 5)", function() {
    assert.equal(cuanto_carga(10, 5), 5);
  });
  it("cuanto_carga(15, 5)", function() {
    assert.equal(cuanto_carga(15, 5), 5);
  });
  it("cuanto_carga(20, 5)", function() {
    assert.equal(cuanto_carga(20, 5), 5);
  });
  it("cuanto_carga(20, 2)", function() {
    assert.equal(cuanto_carga(20, 2), 2);
  });
  it("cuanto_carga(22, 5)", function() {
    assert.equal(cuanto_carga(22, 5), 3);
  });
  it("cuanto_carga(24, 2)", function() {
    assert.equal(cuanto_carga(24, 2), 1);
  });
  it("cuanto_carga(25, 5)", function() {
    assert.equal(cuanto_carga(25, 5), 0);
  });
});


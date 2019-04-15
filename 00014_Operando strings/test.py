describe("", function() {
  it(longitud_nombre_completo("Cosme", "Fulanito"), function() {
    assert.equal(longitud_nombre_completo("Cosme", "Fulanito"), 14);
  });
  it(longitud_nombre_completo("John", "Snow"), function() {
    assert.equal(longitud_nombre_completo("John", "Snow"), 9);
  });
  it(longitud_nombre_completo("Juana", "Azurduy"), function() {
    assert.equal(longitud_nombre_completo("Juana", "Azurduy"), 13);
  });
})

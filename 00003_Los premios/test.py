describe("", function() {
  it("medalla_segun_puesto(1)", function() {
    assert.equal(medalla_segun_puesto(1), "oro")
  })
  it("medalla_segun_puesto(2)", function() {
    assert.equal(medalla_segun_puesto(2), "plata")
  })
  it("medalla_segun_puesto(3)", function() {
    assert.equal(medalla_segun_puesto(3), "bronce")
  })
  it("medalla_segun_puesto(4)", function() {
    assert.equal(medalla_segun_puesto(4), "nada")
  })
  it("medalla_segun_puesto(5)", function() {
    assert.equal(medalla_segun_puesto(5), "nada")
  })
  it("medalla_segun_puesto(0)", function() {
    assert.equal(medalla_segun_puesto(0), "nada")
  })
})

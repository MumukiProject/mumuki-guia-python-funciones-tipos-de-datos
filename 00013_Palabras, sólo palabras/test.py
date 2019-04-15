describe("", function() {
  it('es_fin_de_semana("sábado")', function() {
    assert(es_fin_de_semana("sábado"));
  });
  it('es_fin_de_semana("domingo")', function() {
    assert(es_fin_de_semana("domingo"));
  });
  it('es_fin_de_semana("lunes")', function() {
    assert(!es_fin_de_semana("lunes"));
  })
  it('es_fin_de_semana("jueves")', function() {
    assert(!es_fin_de_semana("jueves"));
  })
})

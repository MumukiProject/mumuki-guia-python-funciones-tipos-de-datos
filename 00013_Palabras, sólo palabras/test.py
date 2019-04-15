
  def test_es_fin_de_semana_sábado(self):
    assert(es_fin_de_semana("sábado"))

  def test_es_fin_de_semana_domingo(self):
    assert(es_fin_de_semana("domingo"))

  def test_es_fin_de_semana_lunes(self):
    assert(not es_fin_de_semana("lunes"))

  def test_es_fin_de_semana_jueves(self):
    assert(not es_fin_de_semana("jueves"))



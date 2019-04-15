
  def test_es_fin_de_semana_sábado(self):
    self.assertTrue(es_fin_de_semana("sábado"))

  def test_es_fin_de_semana_domingo(self):
    self.assertTrue(es_fin_de_semana("domingo"))

  def test_es_fin_de_semana_lunes(self):
    self.assertTrue(not es_fin_de_semana("lunes"))

  def test_es_fin_de_semana_jueves(self):
    self.assertTrue(not es_fin_de_semana("jueves"))




  def test_el_sabado_es_fin_de_semana(self):
    self.assertTrue(es_fin_de_semana("sábado"))

  def test_el_domingo_es_fin_de_semana(self):
    self.assertTrue(es_fin_de_semana("domingo"))

  def test_el_lunes_NO_es_fin_de_semana(self):
    self.assertFalse(es_fin_de_semana("lunes"))

  def test_el_viernes_NO_es_fin_de_semana(self):
    self.assertFalse(es_fin_de_semana("viernes"))



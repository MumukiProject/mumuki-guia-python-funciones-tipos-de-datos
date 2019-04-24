  
  def test_es_numero_de_la_suerte_2_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(2))

  def test_es_numero_de_la_suerte_4_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(4))

  def test_es_numero_de_la_suerte_6_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(6))

  def test_es_numero_de_la_suerte_8_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(8))

  def test_es_numero_de_la_suerte_9_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(9))

  def test_es_numero_de_la_suerte_81_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(81))

  def test_es_numero_de_la_suerte_12456_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(12456))

  def test_es_numero_de_la_suerte_3003_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(3003))

  def test_es_numero_de_la_suerte_es_verdadero_si_es_multiplo_de_2(self):
    self.assertTrue(es_numero_de_la_suerte(4654))

  def test_es_numero_de_la_suerte_es_also_si_no_es_multiplo_de_2_ni_de_3(self):
    self.assertFalse(es_numero_de_la_suerte(49))

  def test_es_numero_de_la_suerte_es_also_si_no_es_positivo(self):
    self.assertFalse(es_numero_de_la_suerte(-3))

  def test_es_numero_de_la_suerte_menos_4_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(-4))

  def test_es_numero_de_la_suerte_7_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(7))

  def test_es_numero_de_la_suerte_15_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(15))



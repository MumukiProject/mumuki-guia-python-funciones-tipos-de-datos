  
  def test_esNumeroDeLaSuerte_2_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(2))

  def test_esNumeroDeLaSuerte_4_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(4))

  def test_esNumeroDeLaSuerte_6_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(6))

  def test_esNumeroDeLaSuerte_8_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(8))

  def test_esNumeroDeLaSuerte_9_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(9))

  def test_esNumeroDeLaSuerte_81_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(81))

  def test_esNumeroDeLaSuerte_12456_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(12456))

  def test_esNumeroDeLaSuerte_3003_es_verdadero(self):
    self.assertTrue(esNumeroDeLaSuerte(3003))

  def test_esNumeroDeLaSuerte_es_verdadero_si_es_multiplo_de_2(self):
    self.assertTrue(esNumeroDeLaSuerte(4654))

  def test_esNumeroDeLaSuerte_es_also_si_no_es_multiplo_de_2_ni_de_3(self):
    self.assertFalse(esNumeroDeLaSuerte(49))

  def test_esNumeroDeLaSuerte_es_also_si_no_es_positivo(self):
    self.assertFalse(esNumeroDeLaSuerte(-3))

  def test_esNumeroDeLaSuerte_menos_4_es_falso(self):
    self.assertFalse(esNumeroDeLaSuerte(-4))

  def test_esNumeroDeLaSuerte_7_es_falso(self):
    self.assertFalse(esNumeroDeLaSuerte(7))

  def test_esNumeroDeLaSuerte_15_es_falso(self):
    self.assertFalse(esNumeroDeLaSuerte(15))



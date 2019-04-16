  def test_es_par_2_es_verdadero(self):
    self.assertTrue(es_par(2))
  
  def test_es_par_8_es_verdadero(self):
    self.assertTrue(es_par(8))
  
  def test_es_par_9890_es_verdadero(self):
    self.assertTrue(es_par(9890))
  
  def test_es_par_1_es_falso(self):
    self.assertFalse(es_par(1))
  
  def test_es_par_879_es_falso(self):
    self.assertFalse(es_par(879))
  
  

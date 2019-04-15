
  def test_cuanto_carga_10_5(self):
    self.assertEqual(cuanto_carga(10, 5), 5)

  def test_cuanto_carga_15_5(self):
    self.assertEqual(cuanto_carga(15, 5), 5)

  def test_cuanto_carga_20_5(self):
    self.assertEqual(cuanto_carga(20, 5), 5)

  def test_cuanto_carga_20_2(self):
    self.assertEqual(cuanto_carga(20, 2), 2)

  def test_cuanto_carga_22_5(self):
    self.assertEqual(cuanto_carga(22, 5), 3)

  def test_cuanto_carga_24_2(self):
    self.assertEqual(cuanto_carga(24, 2), 1)

  def test_cuanto_carga_25_5(self):
    self.assertEqual(cuanto_carga(25, 5), 0)




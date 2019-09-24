
  def test_longitud_nombre_completo_Cosme_Fulanito(self):
    self.assertEqual(longitud_nombre_completo("Cosme", "Fulanito"), 14)

  def test_longitud_nombre_completo_John_Snow(self):
    self.assertEqual(longitud_nombre_completo("John", "Snow"), 9)

  def test_longitud_nombre_completo_Juana_Azurduy(self):
    self.assertEqual(longitud_nombre_completo("Juana", "Azurduy"), 13)

  def test_se_contempla_el_espacio_entre_nombre_y_apellido(self):
    try:
      longitud = longitud_nombre_completo("Gus", "Trucco")
    except:
      longitud = 10
    
    if(longitud == 9):
      self.fail("Te faltó contar el espacio")
  
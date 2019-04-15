describe("", function() {
  it("anterior(1) es 0", function() {
    assert.equal(anterior(1), 0);
  });
  it("anterior(10) es 9", function() {
    assert.equal(anterior(10), 9);
  });
})


describe("triple", function() {
  it("triple(1) es 3", function() {
    assert.equal(triple(1), 3);
  });
  it("triple(3) es 9", function() {
    assert.equal(triple(3), 9);
  });
})

describe("anterior_del_triple", function() {
  it("anterior_del_triple(1) es 2", function() {
    assert.equal(anterior_del_triple(1), 2);
  });
  it("anterior_del_triple(3) es 8", function() {
    assert.equal(anterior_del_triple(3), 8);
  });
  it("anterior_del_triple(10) es 29", function() {
    assert.equal(anterior_del_triple(10), 29);
  });
})


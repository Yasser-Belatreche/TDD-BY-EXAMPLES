package MoneyExample;

import org.junit.Test;

import static org.junit.Assert.assertEquals;;

public class DollarTest {

  @Test
  public void should_multiply() {
    Dollar five = new Dollar(5);
    five.times(2);
    assertEquals(10, five.amount);
  }
}
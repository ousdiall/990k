//Ousmane Diall tun47370@temple.edu
//Program name: ChangeDispenser

import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class ChangeDispenser {

	// Initiating all the lists needed to calculate the amount of coins
	static List<Integer> coinValue = new ArrayList<>();
	static List<String> coinName = new ArrayList<>();
	static List<String> coinNamePlural = new ArrayList<>();
	static List<Double> coinConversion = new ArrayList<>();
	static List<Integer> coinAmount = new ArrayList<>();

	// This method creates the elements of the lists created above.

	public static double makeChange() {
		// The name and their plural form lists are used to create a representation
		// of the result in the end of the program.
		coinName.add("DOLLAR");
		coinName.add("HALF DOLLAR");
		coinName.add("QUARTER");
		coinName.add("DIME");
		coinName.add("NICKEL");
		coinName.add("PENNY");

		coinNamePlural.add("DOLLARS");
		coinNamePlural.add("HALF DOLLARS");
		coinNamePlural.add("QUARTERS");
		coinNamePlural.add("DIMES");
		coinNamePlural.add("NICKELS");
		coinNamePlural.add("PENNIES");

		// The values store the coins as integers, and multiplies it
		// to 100. This is because doubles and floats aren't accurate
		// enough to represent money in Java, and will create rounding errors.

		coinValue.add(100);
		coinValue.add(50);
		coinValue.add(25);
		coinValue.add(10);
		coinValue.add(05);
		coinValue.add(01);

		// The coin amount list stores how many coins are present
		// after the recursion.
		for (int i = 0; i < 6; i++) {
			coinAmount.add(0);
		}

		// This method also allows the user to input a method.
		// this method then multiplies the user input by 100 so that it can
		// represent an integer and be used in the recursion.
		Scanner in = new Scanner(System.in);
		System.out.print("Enter in the amount of change: ");
		double chan = in.nextDouble();
		chan *= 100;
		return chan;
	}

	private static List<Double> makeChange(double reduce) {
		// We must loop through every element in the coinValue list
		// until we find an element that is less than or equal to
		// the given double
		for (int i = 0; i < coinValue.size(); i++) {
			if (reduce >= coinValue.get(i)) {
				// This adds the biggest element from coinValue that is less than
				// the user input, into a list that will convert the element
				// into a decimal
				coinConversion.add((double) coinValue.get(i));
				// This return statement subtracts the user input by the maximum
				// value in the coinValue list that is less than
				// the user input.
				return makeChange(reduce - coinValue.get(i));
			}
		}
		// This loop converts every collected value into a decimal, and
		// is used as the list that collected the amount of coins
		for (int i = 0; i < coinConversion.size(); i++) {
			coinConversion.set(i, coinConversion.get(i) / 100);
		}

		// This part creates the increments of every coin collected in
		// the coinConversion. If there is more than one of any coin, we
		// use the plural form of the coin name for the printout
		int incDollar = 0;
		int incHalfDollar = 0;
		int incQuarter = 0;
		int incDime = 0;
		int incNickel = 0;
		int incPenny = 0;

		for (int i = 0; i < coinConversion.size(); i++) {
			if (coinConversion.get(i) == 1.0) {
				incDollar++;
				coinAmount.set(0, incDollar);
			} else if (coinConversion.get(i) == .5) {
				incHalfDollar++;
				coinAmount.set(1, incHalfDollar);
			} else if (coinConversion.get(i) == .25) {
				incQuarter++;
				coinAmount.set(2, incQuarter);
			} else if (coinConversion.get(i) == .10) {
				incDime++;
				coinAmount.set(3, incDime);
			} else if (coinConversion.get(i) == .05) {
				incNickel++;
				coinAmount.set(4, incNickel);
			} else if (coinConversion.get(i) == .01) {
				incPenny++;
				coinAmount.set(5, incPenny);
			}
		}

		// Finally, this prints out the amount of coins in the coinConversion list
		// as well as the coinName and/or coinNamePlural list, depending on
		// if there are no coins, 1 coin, or multiple coins.

		for (int i = 0; i < coinAmount.size(); i++) {
			if (coinAmount.get(i) > 1 || coinAmount.get(i) == 0) {
				System.out.println(coinAmount.get(i) + " " + coinNamePlural.get(i));
			} else {
				System.out.println(coinAmount.get(i) + " " + coinName.get(i));
			}

		}

		return coinConversion;
	}

	public static void main(String[] args) {
		Double j = makeChange();
		makeChange(j);

	}

}

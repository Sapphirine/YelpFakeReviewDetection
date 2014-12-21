package bigDataAnalytics.project;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Rating_Similarity {

	public static double[] CalRateSim(String filePath) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader(filePath));
		String line;
		ArrayList<Integer> ratings = new ArrayList<Integer>();
		while ((line = br.readLine()) != null) {
			ratings.add(line.charAt(line.length() - 1) - '0');
		}
		br.close();
		// System.out.println(ratings.get(8));
		double[] rv = new double[ratings.size()];
		for (int i = 0; i < ratings.size(); i++) {
			double sumRatings = 0;
			for (int j = 0; j < ratings.size(); j++) {
				if (i != j) {
					sumRatings += ((double) Math.abs(ratings.get(i)
							- ratings.get(j))) / 5;
				}
			}
			rv[i] = 1 - sumRatings / (ratings.size() - 1);
		}
		return rv;
	}

}

package bigDataAnalytics.project;

import java.io.File;

public class GetDir {

	public static String[] ReturnFolderNames(String s) {
		File folder = new File(s);
		File[] listOfFiles = folder.listFiles();

		String[] rv = new String[listOfFiles.length];
		for (int i = 0; i < listOfFiles.length; i++) {

			rv[i] = listOfFiles[i].getPath();
			// System.out.println("Directory " + listOfFiles[i].getName());

		}
		return rv;
	}

}

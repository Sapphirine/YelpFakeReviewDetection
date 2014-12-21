package bigDataAnalytics.project;

public class keyPair {
	int a;
	int b;
	public keyPair(int i, int j) {
		a = i;
		b = j;
	}
	
	@Override
	public boolean equals(Object object) {
		if (!(object instanceof keyPair)) {
			return false;
		} else {
			keyPair csObject = (keyPair) object;
			if ((csObject.a == this.a && csObject.b == this.b) || (csObject.a == this.b && csObject.b == this.a)) {
				return true;
			} else {
				return false;
			}
		}
	}
	
	@Override
	public int hashCode() {
		Integer aa = a;
		Integer bb = b;
		return aa.hashCode() * bb.hashCode();
	}
}

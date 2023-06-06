package shared;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * 
 *
 * @author Lara
 */
public class MyGenBank {
	private String id = "ID";
	private String ac = "AC";
	private String dt = "DT";
	private String kw = "KW";
	private String oc = "OC";
	private Fasta fasta;

	// Konstruktor
	public MyGenBank(String id, String ac, String dt, String oc, String kw, String de, String dna) {

		this.id = id;
		this.ac = ac;
		this.dt = dt;
		this.kw = kw;
		this.oc = oc;
		this.fasta = new Fasta(de, dna);

	}

	public String toString() {
		return "ID " + id + "\nAC " + ac + "\nDT " + dt + "\nKW " + kw + "\nOC " + oc + "\n" + fasta.toString() + "\n"
				+ "//";
	}

	public String getID() {
		return id;
	}

	public String getDT() {
		return dt;
	}

	public String getOC() {
		return oc;
	}

	public String getKW() {
		return kw;
	}

	public Fasta getFasta() {
		return fasta;
	}

	public static MyGenBank EMBLToMyGenBank(String path, String pathOut) throws IOException {
		// Versuch Eigenschaften herauszufiltern
		BufferedReader br = new BufferedReader(new FileReader(path));
		MyGenBank m = EMBLToMyGenBank(br);
		br.close();
		m.toFile(pathOut);
		return m;
	}

	//Overload
	public static MyGenBank EMBLToMyGenBank(BufferedReader br) throws IOException {
		String line;
		String id = "", ac = "", dt = "", kw = "", oc = "", de = "", dna = "";

		while (br.ready() && (line = br.readLine()) != null) {
			if (line.startsWith("ID")) {
				id += getContent(line) + " ";
			} else if (line.startsWith("AC")) {
				ac += getContent(line) + " ";
			} else if (line.startsWith("DT")) {
				dt += getContent(line) + " ";
			} else if (line.startsWith("KW")) {
				kw += getContent(line) + " ";
			} else if (line.startsWith("OC")) {
				oc += getContent(line) + " ";
			} else if (line.startsWith("DE")) {
				de += getContent(line) + " ";
			} else if (line.startsWith("SQ")) {
				dna = "";
				while (!(line = br.readLine()).startsWith("//")) { // solange nicht // gelesen wird tue:

					dna += line.replaceAll("[^acgt]", "");
				}
			}

		}
		return new MyGenBank(id, ac, dt, oc, kw, de, dna);
	}

	private static String getContent(String line) {
		return line.substring(2).trim(); // trim = spaces am Anfang und Ende löschen
	}

	// what about fasta (header=de, and sequence?)

	public void toFile(String path) throws IOException {
		Path filePath = Path.of(path);
		Files.writeString(filePath, toString());
	}

	public static MyGenBank readMyGenBankFile(String path) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader(path));
		MyGenBank m = readMyGenBankFile(br);
		br.close();
		return m;
	}

	public static MyGenBank readMyGenBankFile(BufferedReader br) throws IOException {
		String line;
		String id = "", ac = "", dt = "", kw = "", oc = "", de = "", dna = "";

		while (br.ready() && (line = br.readLine()) != null) {
			if (line.startsWith("ID")) {
				id = getContent(line);
			} else if (line.startsWith("AC")) {
				ac = getContent(line);
			} else if (line.startsWith("DT")) {
				dt = getContent(line);
			} else if (line.startsWith("KW")) {
				kw = getContent(line);
			} else if (line.startsWith("OC")) {
				oc = getContent(line);
			} else if (line.startsWith(">")) {
				de = line; // alles außer ">"-Zeichen

				dna = "";
				while (!(line = br.readLine()).startsWith("//")) { // solange nicht gelesen wird tue:

					dna += line;
				}
			}

		}
		return new MyGenBank(id, ac, dt, kw, oc, de, dna);
	}

	public static MyGenBank GenBankToMyGenBank(String path, String pathOut) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader(path));
		MyGenBank m = genBankToMyGenBank(br);
		m.toFile(pathOut);
		br.close();
		return m;
	}

	public static MyGenBank genBankToMyGenBank(BufferedReader br) throws IOException {
		String line;
		StringBuilder id = new StringBuilder(), ac = new StringBuilder(), dt = new StringBuilder(),
				kw = new StringBuilder(), oc = new StringBuilder(), de = new StringBuilder(), dna = new StringBuilder();
		String lastKey = "NA"; // ignoriert alles was nicht gewollt ist
		line = br.readLine(); // erste Zeile untersuchen, wo nächstes Zeichen/Wort beginnt
		int keywordLength = getKeywordLength(line);
		line = line.trim();
		lastKey = findPropInGenBank(line, id, ac, dt, kw, oc, de, dna, br);
		while (br.ready() && (line = br.readLine()) != null) { // ready, wenn lesbar
			if (line.length() > keywordLength && line.substring(0, keywordLength).trim().length() == 0) { // check ob
				line = lastKey + " " + line;
			}
			line = line.trim();
			lastKey = findPropInGenBank(line, id, ac, dt, kw, oc, de, dna, br);
		}

		return new MyGenBank(id.toString(), ac.toString(), dt.toString(), oc.toString(), kw.toString(),
				de.toString(), dna.toString());
	}

	public static String findPropInGenBank(String line, StringBuilder id, StringBuilder ac, StringBuilder dt,
			StringBuilder kw, StringBuilder oc, StringBuilder de, StringBuilder dna, BufferedReader br)
			throws IOException {

		if (line.startsWith("LOCUS")) {
			id.append(getProp("LOCUS", line) + " ");
			return "LOCUS";
		} else if (line.startsWith("PUBMED")) {
			dt.append(getProp("PUBMED", line) + " ");
			return "PUBMED";
		} else if (line.startsWith("ACCESSION")) {
			ac.append(getProp("ACCESSION", line) + " ");
			return "ACCESSION";
		} else if (line.startsWith("KEYWORDS")) {
			kw.append(getProp("KEYWORDS", line) + " ");
			return "KEYWORDS";
		} else if (line.startsWith("ORGANISM")) {
			oc.append(getProp("ORGANISM", line) + " ");
			return "ORGANISM";
		} else if (line.startsWith("DEFINITION")) {
			de.append(getProp("DEFINITION", line) + " ");
			return "DEFINITION";
		} else if (line.startsWith("ORIGIN")) {
			while (!(line = br.readLine()).startsWith("//")) { // solange nicht // gelesen wird tue:

				dna.append(line.replaceAll("[^acgt]", "")); // alles was nicht acgt ist, ersetzen

			}
			return "NA"; // not available

		} else
			return "NA";

	}

	private static String getProp(String prop, String line) {
		return line.substring(prop.length()).trim(); // trim -> entfernt beliebige Whitespace-Zeichen vor und danach
	}

	public static int getKeywordLength(String line) { // bei GenBankToMyGenBank verwendet
		boolean firstWord = false; // because of spaces
		boolean spaces = false; // spaces = a
		for (int i = 0; i < line.length(); i++) {
			if (!String.valueOf(line.charAt(i)).matches("\s") && !firstWord) { // key found
				firstWord = true;
			} else if (String.valueOf(line.charAt(i)).matches("\s") && firstWord) { // spaces after key found
				spaces = true;
			} else if (!String.valueOf(line.charAt(i)).matches("\s") && firstWord & spaces) { // start of value found
				return i;
			}
		}
		return 0;
	}

	public static void main(String args[]) throws IOException {

		MyGenBank m = EMBLToMyGenBank("/Users/larry/Desktop/PP/TestFile.txt",
				"/Users/larry/Desktop/PP/EMBLFormatinMyGB.txt");
		// System.out.println(m);
		m.toFile("/Users/larry/Desktop/PP/MyGenbank.txt");

		MyGenBank.GenBankToMyGenBank("/Users/larry/Desktop/PP/GenBankFormat.txt",
				"/Users/larry/Desktop/PP/GenBankFormatinMyGB.txt");
	}

}

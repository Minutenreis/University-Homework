package shared;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * 
 *
 * @author Lara
 */

public class Fasta {

	private String header = ">";
	private String dna = "";

	public boolean checkHeader(String header) {
		return header.matches("^>.*"); // beginnt mit > und soll kein \n enthalten
	}

	public boolean checkDNA(String dna) {
		return dna.matches("[acgt]*");
	}

	// Standardkonstruktor implementieren
	public Fasta() { // Non-argument Constructor
	}

	// Überladener Konstruktor
	public Fasta(String header, String dna) {
		setHeader(header);
		setDNA(dna);
	}

	// Kopierkonstruktor
	public Fasta(Fasta fasta) {
		this.header = fasta.header;
		this.dna = fasta.dna;
	}

	// Methoden
	public void resetValue(String header, String dna) {
		this.header = ">";
		this.dna = "";
	}

	public String getHeader() {
		return header;
	}

	public String getDNA() {
		return dna;
	}

	public void setHeader(String header) {
		if (checkHeader(header)) {
			this.header = header;
		} else {
			throw new IllegalHeaderException(header); // gibt Fehler aus
		}

	}

	public void setDNA(String dna) {
		if (checkDNA(dna)) {
			this.dna = dna;
		} else {
			throw new IllegalSequenceException(dna); // gibt Fehler aus
		}
	}

	public int dnaLength() {
		return dna.length();
	}

	public String toString() {
		String dnaOutput = "";
		for (int i = 0; i < dna.length(); i++) {
			if (i % 80 == 0) { // 80 Zeichen pro Zeile gewährleisten
				dnaOutput += "\n";
			}
			dnaOutput += dna.charAt(i);
		}
		String content = header + "\n" + dnaOutput;
		return content;
	}

	public String combine(String dna_2) {
		String neu_dna = dna + dna_2;
		return neu_dna;
	}

	public String[] split(String dna, int parts) { // In wie viele Teile soll der String geteilt werden?
		int length = dna.length() / parts; // Länge der Substrings
		int rest = dna.length() % parts;

		String[] split = new String[parts]; // String-Array wird mit Länge jedes Teils initialisiert

		int currentLength = 0; // Verfolgt Startindex
		for (int i = 0; i < parts; i++) { // jeder Teilstring wird einzeln berechnet
			int restLength = i < rest ? length + 1 : length;
			split[i] = dna.substring(currentLength, currentLength + restLength); // von aktueller Position bis Länge
			currentLength += restLength; // des aktuellen Teils
		}
		return split;
	}

	public String dotPlot(String dna_1, String dna_2) {
		StringBuilder sb = new StringBuilder("");
		// in method preparation
		for (int i = 0; i < dna_1.length(); i++) {
			if (i == 0) {
				sb.append(" |" + dna_1.charAt(i) + "|");
			} else if (i == dna_1.length() - 1) {
				sb.append(dna_1.charAt(i) + "|" + "\n");
			} else {
				sb.append(dna_1.charAt(i) + "|");
			}
		}

		for (int i = 0; i < dna_2.length(); i++) {
			sb.append(dna_2.charAt(i) + "|"); // charAt => returns the character at the
												// specified index in a string
			for (int j = 0; j < dna_1.length(); j++) {
				if (dna_1.charAt(j) == dna_2.charAt(i)) {
					sb.append("*|");
				} else {
					sb.append(" |");
				}
			}
			sb.append("\n");
		}
		return sb.toString();
	}

	// Aufgabenblatt 2

	public static Fasta getFastaFromFile(String path) throws IOException {
		Path filePath = Path.of(path); // Path Objekt erstellen
		String content = Files.readString(filePath);
		content.replace("\r", ""); // falls leere Zeile -> soll ignoriert werden
		String[] str = content.split("\n"); // nach Zeilenumbruch teilen
		String header = str[0];
		String dna = "";
		for (int i = 1; i < str.length; i++) { // ntes Element ist nicht mehr in str, deswegen "<"
			dna += str[i];
		}
		Fasta f = new Fasta(header, dna);
		f.toString();
		return f;

	}

	public static void writeFastaToFile(Fasta fasta, String path) throws IOException {
		Path filePath = Path.of(path);
		Files.writeString(filePath, fasta.toString());
	}

	public static void main(String args[]) throws IOException {

		Fasta fasta = new Fasta(">header",
				"aaatttgggcccaaatgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggttgggcccaaatttgggcccaaatttgggccc");
		// Fasta into File
		Fasta.writeFastaToFile(fasta, "/Users/larry/Desktop/PP/Fasta.txt");

		// Fasta from File
		Fasta fasta2 = new Fasta(Fasta.getFastaFromFile("/Users/larry/Desktop/PP/Fasta.txt"));
		System.out.println(fasta2);
		// Fasta.getFastaFromFile("/Users/larry/Desktop/PP/Fasta.txt");

	}

}

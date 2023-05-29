package BioInfo.shared;

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
		return header.startsWith(">");
	}

	public boolean lineHeader(String dna) {
		return header.matches("^>.*");
	}

	public boolean checkDNA(String dna) {
		return dna.matches("[ACGT]*");
	}

	// Standardkonstruktor implementieren
	public Fasta() { // Non-argument Constructor
	}

	// Überladener Konstruktor
	public Fasta(String header, String dna) throws IllegalHeaderException, IllegalSequenceException {
		if (!checkHeader(header)) {
			throw new IllegalHeaderException(header);
		}
		this.header = header;
		if (!checkDNA(dna)) {
			throw new IllegalSequenceException(dna);
		}
		this.dna = dna;

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

	// public String getEverything() {
	// return header + dna;
	// }

	public int dnaLength() {
		return dna.length();
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

	public static String dotPlot(String dna_1, String dna_2) {
		// in method preparation
		StringBuilder out = new StringBuilder("");
		for (int i = 0; i < dna_1.length(); i++) {
			if (i == 0) {
				out.append(" |" + dna_1.charAt(i) + "|");
			} else if (i == dna_1.length() - 1) {
				out.append(dna_1.charAt(i) + "|" + "\n");
			} else {
				out.append(dna_1.charAt(i) + "|");
			}
		}

		for (int i = 0; i < dna_2.length(); i++) {
			out.append(dna_2.charAt(i) + "|"); // charAt => returns the character at the specified index in a
												// string
			for (int j = 0; j < dna_1.length(); j++) {
				if (dna_1.charAt(j) == dna_2.charAt(i)) {
					out.append("*|");
				} else {
					out.append(" |");
				}
			}
			out.append("\n");
		}
		return out.toString();
	}

	public void writeToFile(String path) throws IOException {
		Path filePath = Path.of(path);
		String dna = getDNA();
		String dnaOutput = "";
		for (int i = 0; i < dna.length(); i++) {
			if (i % 80 == 0) {
				dnaOutput += "\n";
			}
			dnaOutput += dna.charAt(i);
		}
		String content = header + "\n" + dnaOutput;
		Files.writeString(filePath, content);
	}

	public static Fasta getFastaFromFile(String path)
			throws IOException, IllegalHeaderException, IllegalSequenceException {
		Path filePath = Path.of(path);
		String content = Files.readString(filePath);
		String[] lines = content.split("\n");
		String header = lines[0];
		String dna = "";
		for (int i = 1; i < lines.length; i++) {
			dna += lines[i];
		}
		return new Fasta(header, dna);
	}
}

all:
	cat part1.pas > MAIN.PAS
	./gen_passwords.py >> MAIN.PAS
	cat part2.pas >> MAIN.PAS
	./gen_lines.py >> MAIN.PAS
	cat part3.pas >> MAIN.PAS

clean:
	rm MAIN.PAS

.PHONY: all say_hello generate clean

all: unpack

unpack:
	unzip character_directory.zip
	mv character_directory photomosaic/character_directory
	ls photomosaic

clean:
	@echo "Cleaning up..."
	rm -rf photomosaic/character_directory

install: clean unpack

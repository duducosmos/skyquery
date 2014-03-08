BINDIR = $(DESTDIR)/usr/bin/
LIBDIR = $(DESTDIR)/usr/share/
clean:
		rm -f *.py[co] */*.py[co]
install:
		mkdir -p $(BINDIR)
		mkdir -p $(LIBDIR)applications/
		mkdir -p $(LIBDIR)pixmaps/

		cp -r bin/* $(BINDIR)
		cp -r applications/* $(LIBDIR)applications/
		cp -r pixmaps/* $(LIBDIR)pixmaps/
unistall:
		rm -rf $(BINDIR)skyquery
		rm -rf $(BINDIR)Skyquery
		rm -rf $(LIBDIR)applications/skyquery.desktop
		rm -rf $(LIBDIR)pixmaps/SkyQuery.ico


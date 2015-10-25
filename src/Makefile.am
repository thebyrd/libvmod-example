AM_CPPFLAGS = @VMOD_INCLUDES@ -Wall -Werror

vmoddir = @VMOD_DIR@
vmod_LTLIBRARIES = libvmod_dynamic.la

libvmod_dynamic_la_LDFLAGS = -module -export-dynamic -avoid-version -shared

libvmod_dynamic_la_SOURCES = \
	vmod_dynamic.c

nodist_libvmod_dynamic_la_SOURCES = \
	vcc_if.c \
	vcc_if.h

dist_man_MANS = vmod_dynamic.3

vmod_dynamic.3: vmod_dynamic.man.rst
	${RST2MAN} $< $@


vmod_dynamic.lo vmod_dynamic.man.rst: vcc

vcc: @VMODTOOL@ $(top_srcdir)/src/vmod_dynamic.vcc
	@VMODTOOL@ $(top_srcdir)/src/vmod_dynamic.vcc

VMOD_TESTS = $(top_srcdir)/src/tests/*.vtc
.PHONY: $(VMOD_TESTS) vcc

$(top_srcdir)/src/tests/*.vtc: libvmod_dynamic.la
	@VARNISHTEST@ -Dvarnishd=@VARNISHD@ -Dvmod_topbuild=$(abs_top_builddir) $@

check: $(VMOD_TESTS)

EXTRA_DIST = \
	vmod_dynamic.vcc \
	$(VMOD_TESTS)

CLEANFILES = \
	$(builddir)/vcc_if.c \
	$(builddir)/vcc_if.h \
	$(builddir)/vmod_dynamic.rst \
	$(builddir)/vmod_dynamic.man.rst \
	$(dist_man_MANS)

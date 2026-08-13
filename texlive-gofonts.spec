%global tl_name gofonts
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	GoSans and GoMono fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gofonts
License:	other-free lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gofonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gofonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the GoSans and GoMono families of fonts designed by the Bigelow & Holmes
foundry for the Go project. GoSans is available in three weights:
Regular, Medium, and Bold (with corresponding italics). GoMono is
available in regular and bold, with italics. Notes on the design may be
found at https://blog.golang.org/go-fonts.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from gofonts:
Map go.map
TL_DROPIN_EOF

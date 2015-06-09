$pdflatex = "xelatex %O %S";
$out_dir = "tmp";
$aux_dir = "tmp";
@default_files = ( "main.tex" );
$pdf_mode = 1;
$silent = 1;

push @extra_latex_options,    "-shell-escape";
push @extra_pdflatex_options, "-shell-escape";
push @extra_latex_options,    "-file-line-error";
push @extra_pdflatex_options, "-file-line-error";
push @extra_latex_options,    "-8bit";
push @extra_pdflatex_options, "-8bit";
#push @extra_latex_options,    "-halt-on-error";
#push @extra_pdflatex_options, "-halt-on-error";

$ENV{'TEXMFLOCAL'}='fonts/lmufonts/texmf/:' . ($ENV{'TEXMFLOCAL'} || '');

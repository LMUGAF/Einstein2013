$pdflatex = "xelatex %O %S";
$out_dir = "tmp";
$aux_dir = "tmp";
@default_files = ( "EE2013.tex" );
$pdf_mode = 1;
#$silent = 1;
push @extra_latex_options, "-shell-escape";
push @extra_pdflatex_options, "-shell-escape";

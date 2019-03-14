# My Latex tips for writing docs and letters

## Writing letters
The following is a list of Latex tags or packages to used in order to craft a simple Latex A4 PDF letter.

```tex
% define a new A4 document with 12pt font size
\documentclass[a4paper,12pt]{article}

% for mobile phone etc symbols
\usepackage{marvosym}
	
% french accents etc	
\usepackage[francais]{babel}

% set margins with no header and no footer
\usepackage[left=1.9cm,top=2cm,bottom=2.5cm,right=1.9cm,nohead,nofoot]{geometry}

% if fancy tables are needed
\usepackage{array}

% if colors are needed
\usepackage{color}

% to use TrueType fonts. Caveat: need to compile with XeLatex
\usepackage{fontspec}
\setmainfont{Linux Libertine O}

% no page numbers
\pagestyle{empty}

% for images and set image files list of paths
\usepackage{graphicx}
\graphicspath{{.}{../../../Photos/}}

% no paragraph identation (or change it to whatever is needed)
\setlength{\parindent}{0pt}

% space between paragraphs
\setlength{\parskip}{11pt}

% interline space
\linespread{1.125}

% PDF metadata
\usepackage[
            pdfauthor={Robert Martin},
            pdftitle={My letter}
            ]{hyperref}
            
% specific to French language
\frenchspacing

%% ------------------------------------------------------------
%% document start
%% ------------------------------------------------------------
\begin{document}

%% ------------------------------------------------------------
%% header table
%% ------------------------------------------------------------
\begin{tabular}{p{10cm} p{5cm}}
	
	\begin{minipage}[t]{0.40\textwidth}
		\begin{flushleft}
			{\Large \textbf{Robert Martin}}\\[10pt]
			11 rue de la Liberté \\
			75001 Paris\\[8pt]
			\Mobilefone ~ +33 06 00 00 00 00 +\\
			\Email ~ robert.martin@outlook.fr\\[20pt]
		\end{flushleft}
	\end{minipage}
	
	&
	
	\begin{minipage}[t]{0.40\textwidth}
		\begin{flushright}
			{\Large \textbf{ACME corporation}}\\[10pt]
			6649 N Blue Gum St\\
			New Orleans (LA)\\
		\end{flushright}
	\end{minipage}  
	
\end{tabular}



\begin{flushleft}
Location, and date here

Letter object here
\end{flushleft}



\vspace{1.5cm}

%% ------------------------------------------------------------
%% Letter body
%% ------------------------------------------------------------
Dear Sir,

\vspace{1.5cm}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


\vspace{1cm}
\hspace{10cm} Robert Martin

\end{document}
```

Refer to [Sample PDF file](sample_letter.pdf)

## Fonts
To view all the fonts available in your Linux system, run the Python script located in the **font** directory:

```command
$ python3 gen_fonts.py > latex_fonts.tex
```
and compile the generated Latex file to [Latex fonts sample](fonts/latex_fonts.pdf)
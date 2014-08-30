\newpage
\calHeader{$start_month}{$start_year}{$end_month}{$end_year}{$kw}
\begin{tabular}{|@{}p{.5\textwidth}@{}|@{}p{.5\textwidth}@{}|}
	\hline
	\multicolumn{2}{|@{}l@{}|}{\begin{calDay}{Mo}{$wd0_dayOfMonth}$wd0_feiertage$wd0_text \end{calDay}}\\\hline
	\multicolumn{2}{|@{}l@{}|}{\begin{calDay}{Di}{$wd1_dayOfMonth}$wd1_feiertage$wd1_text \end{calDay}}\\\hline
	\multicolumn{2}{|@{}l@{}|}{\begin{calDay}{Mi}{$wd2_dayOfMonth}$wd2_feiertage$wd2_text \end{calDay}}\\\hline
	\multicolumn{2}{|@{}l@{}|}{\begin{calDay}{Do}{$wd3_dayOfMonth}$wd3_feiertage$wd3_text \end{calDay}}\\\hline
	\multicolumn{2}{|@{}l@{}|}{\begin{calDay}{Fr}{$wd4_dayOfMonth}$wd4_feiertage$wd4_text \end{calDay}}\\\hline
	\begin{calDay}[red]{Sa}{$wd5_dayOfMonth}$wd5_feiertage$wd5_text \end{calDay} &
	\begin{calDay}[red]{So}{$wd6_dayOfMonth}$wd6_feiertage$wd6_text \end{calDay} \\\hline
\end{tabular}
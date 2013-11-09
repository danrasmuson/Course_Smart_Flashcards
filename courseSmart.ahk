; if you figured out how to use a function you could just pass the params in there
+1::
copyTerm("OneWord")
exit

+2::
copyTerm("TwoWord")
exit

+3::
copyTerm("ThreeWord")
exit

+4::
copyTerm("FourWord")
exit

+5::
copyTerm("FiveWord")
exit


copyTerm(word)
{
	; cdopy text from coursesmart
	MouseGetPos, xpos, ypos
	MouseMove, xpos, ypos+55
	click

	; paste to sublime
	sleep 250
	Send #3 ; sublime must be 3rd in window task bar
	Send ^v
	Send {enter}
	Send %word%
	Send {enter}
	Send {enter}
	Send #2 ; chrome must be 2nd in window task bar
}
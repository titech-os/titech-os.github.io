#! /opt/local/bin/perl
#------------------------------------------------------------------
# YOU ARE COMING TO THE DESTINATION ALMOST. PLEASE DO A LITTLE EFFORT.
#
# How to setup search form of htags
# =================================
#
# You should start HTTP server so that this script is executed as a CGI script.
# Setup procedure for it depends on the HTTP server which you are using.
# If you are using Apache, 'HTML/.htaccess' might be helpful for you.
#
#------------------------------------------------------------------
#
# Copyright (c) 1997, 2004, 2006, 2008, 2010 Tama Communications Corporation
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
$global_command = '/usr/local/bin/global';
sub header {
	"Content-type: text/html\n\n" .
	"<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>\
<html xmlns='http://www.w3.org/1999/xhtml'>\
<head>\
<title>Result</title>\
<meta name='robots' content='noindex,nofollow' />\
<meta name='generator' content='GLOBAL-6.5.2' />\
<meta http-equiv='Content-Style-Type' content='text/css' />\
<link rel='stylesheet' type='text/css' href='$basedir/style.css' />\
</head>\n<body>\n";
}
sub tailer {
	"</body>\n</html>\n";
}
sub title {
	"<h1 class='title'>" . $_[0] . "</h1>\n";
}
sub error {
	"<h2 class='error'>Error</h2>\n";
}
sub message {
	"<h3 class='message'>" . $_[0] . "</h3>\n";
}
@pairs = split (/&/, $ENV{'QUERY_STRING'});
foreach $p (@pairs) {
	($name, $value) = split(/=/, $p);
	$value =~ tr/+/ /;
	$value =~ s/%([\dA-Fa-f][\dA-Fa-f])/pack("C", hex($1))/eg;
	$form{$name} = $value;
}
$basedir = "..";
if ($form{'id'}) {
	$url = $ENV{'HTTP_REFERER'};
	if (!$url) {
		print header();
		print error();
		print message("Your browser doesn't send HTTP_REFERER. Please use another one.");
		print tailer();
		exit 0;
	}
	$basedir = $url;
	$basedir =~ s!/[^\/]+$!!;		# remove file name.
	$basedir =~ s!/defines$!!;
	$basedir =~ s!/S$!!;
	$basedir =~ s!/$!!;
}
sub error_and_exit {
	print header();
	print error();
	print message($_[0] . "<a href='$basedir/mains.html'>[return]</a>");
	print tailer();
	exit 0;
}
if ($form{'pattern'} eq '') {
	error_and_exit("Pattern not specified.");
}
$pattern = $form{'pattern'};
$flag = '';
$words = 'definitions';
if ($form{'type'} eq 'reference') {
	$flag = 'r';
	$words = 'references';
} elsif ($form{'type'} eq 'symbol') {
	$flag = 's';
	$words = 'symbols';
} elsif ($form{'type'} eq 'path') {
	$flag = 'P';
	$words = 'paths';
} elsif ($form{'type'} eq 'grep') {
	$flag = 'g';
	$words = 'patterns';
} elsif ($form{'type'} eq 'idutils') {
	$flag = 'I';
	$words = 'patterns';
}
$iflag = '';
if ($form{'icase'}) {
	$iflag = 'i';
}
$oflag = '';
if ($form{'other'} && ($flag eq 'g' || $flag eq 'P')) {
	$oflag = 'o';
}
if (-d "cgi-bin") {
	# This code avoids the bug of the python built-in web server.
	chdir("cgi-bin");
	if ($?) {
		error_and_exit("Couldn't change 'cgi-bin' directory.");
	}
}
$html = 'html';
if (-f "../GTAGSROOT" && open(GTAGSROOT, "../GTAGSROOT")) {
	$gtagsroot = <GTAGSROOT>;
	chop($gtagsroot);
	close(GTAGSROOT);
} else {
	$gtagsroot = "../..";
}
chdir($gtagsroot);
if ($?) {
	error_and_exit("GTAGSROOT directory not found.");
}
#
# fork and exec global(1) to avoid command substitutions in $pattern.
# The --result=ctags-xid print the file id of the path at the head
# of each line.
#
$flags = '-' . $flag . $iflag . $oflag . 'e';
if ($^O eq 'MSWin32') {
	#
	# This code was commented out, because it may have a security hole in the
	# future.  To use this code, please uncomment in your own responsibility.
	#
	#open(PIPE, "$global_command" . " --result=ctags-xid $flags \"$pattern\" |");
	error_and_exit("Feature not implemented.");
} else {
	open(PIPE, "-|") || exec "$global_command", '--result=ctags-xid', $flags, $pattern;
	if ($?) {
		error_and_exit("Cannot execute global.");
	}
}
local(%ctab) = ('&', '&amp;', '<', '&lt;', '>', '&gt;');
$pattern =~ s/([&<>])/$ctab{$1}/ge;
local($tag, $lno, $filename);
if ($line1 = <PIPE>) {
	push(@line, $line1);
	if ($line2 = <PIPE>) {
		push(@line, $line2);
	}
}
sub input {
	$line = (@line > 0) ? shift @line : <PIPE>;
	return $line;
}
if (@line == 0) {
	# not found
	print header();
	print title($pattern);
	print message("Pattern not found. <a href='$basedir/mains.html'>[return]</a>");
	print tailer();
	exit 0;
} elsif (@line == 1) {
	# direct jump
	($fid, $tag, $lno, $filename) = split(/[ \t]+/, shift @line);
	print "Location: $basedir/S/$fid.$html#L$lno\n\n";
	# Python's built-in webserver doesn't support redirects issued from CGI scripts.
	print "<html>\n";
	print qq(<head><meta http-equiv="Refresh" content="0; url=$basedir/S/$fid.$html#L$lno" /></head>\n);
	print "<body>";
	print tailer();
	exit 0;
}
print header();
print title($pattern);
print "Following $words are matched to above pattern.<hr />\n";
#
# Input format:
#
# fid tag   lno filename
# ---------------------------------------------
# 100 main  32 ./main.c main(argc, argv)
#
print "<pre>\n";
$count = 0;
while ($_ = input()) {
	chop;
	$count++;
	($fid, $tag, $lno, $filename) = split;
	s/^[0-9]+[ \t]+//;
	s/([&<>])/$ctab{$1}/ge;
	s!(^[^ \t]+)!<a href='$basedir/S/$fid.$html#L$lno'>$1<\/a>!;
	print "<span class='curline'>$_</span>\n";
}
print "</pre>\n";
close(PIPE);
print "<hr />$count objects located.\n";
print tailer();
exit 0;

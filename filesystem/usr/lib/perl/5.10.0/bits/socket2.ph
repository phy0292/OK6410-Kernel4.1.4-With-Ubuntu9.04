require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_SYS_SOCKET_H)) {
    die("Never include <bits/socket2.h> directly; use <sys/socket.h> instead.");
}
1;

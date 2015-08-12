# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is the Python XPCOM language bindings.
#
# The Initial Developer of the Original Code is ActiveState Tool Corp.
# Portions created by ActiveState Tool Corp. are Copyright (C) 2000, 2001
# ActiveState Tool Corp.  All Rights Reserved.
#
# Contributor(s):
#   Mark Hammond <MarkH@ActiveState.com> (original author)
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

# Generated by h2py from nsError.h
# CMD line: h2py.py -i (nsresult) nsError.h

# XXX - NOTE - some manual code at the end, and all literals moved back to ints
NS_ERROR_MODULE_XPCOM = 1
NS_ERROR_MODULE_BASE = 2
NS_ERROR_MODULE_GFX = 3
NS_ERROR_MODULE_WIDGET = 4
NS_ERROR_MODULE_CALENDAR = 5
NS_ERROR_MODULE_NETWORK = 6
NS_ERROR_MODULE_PLUGINS = 7
NS_ERROR_MODULE_LAYOUT = 8
NS_ERROR_MODULE_HTMLPARSER = 9
NS_ERROR_MODULE_RDF = 10
NS_ERROR_MODULE_UCONV = 11
NS_ERROR_MODULE_REG = 12
NS_ERROR_MODULE_FILES = 13
NS_ERROR_MODULE_DOM = 14
NS_ERROR_MODULE_IMGLIB = 15
NS_ERROR_MODULE_MAILNEWS = 16
NS_ERROR_MODULE_EDITOR = 17
NS_ERROR_MODULE_XPCONNECT = 18
NS_ERROR_MODULE_PROFILE = 19
def NS_FAILED(_nsresult): return ((_nsresult) & -2147483648)

NS_ERROR_SEVERITY_SUCCESS = 0
NS_ERROR_SEVERITY_ERROR = 1
NS_ERROR_MODULE_BASE_OFFSET = 69
def NS_ERROR_GET_CODE(err): return ((err) & 65535)

def NS_ERROR_GET_MODULE(err): return (((((err) >> 16) - NS_ERROR_MODULE_BASE_OFFSET) & 8191))

def NS_ERROR_GET_SEVERITY(err): return (((err) >> 31) & 1)

NS_OK = 0
NS_COMFALSE = 1
NS_ERROR_BASE = (  -1041039360)
NS_ERROR_NOT_INITIALIZED = (NS_ERROR_BASE + 1)
NS_ERROR_ALREADY_INITIALIZED = (NS_ERROR_BASE + 2)
NS_ERROR_NOT_IMPLEMENTED = (  -2147467263)
NS_NOINTERFACE = (  -2147467262)
NS_ERROR_NO_INTERFACE = NS_NOINTERFACE
NS_ERROR_INVALID_POINTER = (  -2147467261)
NS_ERROR_NULL_POINTER = NS_ERROR_INVALID_POINTER
NS_ERROR_ABORT = (  -2147467260)
NS_ERROR_FAILURE = (  -2147467259)
NS_ERROR_UNEXPECTED = (  -2147418113)
NS_ERROR_OUT_OF_MEMORY = (  -2147024882)
NS_ERROR_ILLEGAL_VALUE = (  -2147024809)
NS_ERROR_INVALID_ARG = NS_ERROR_ILLEGAL_VALUE
NS_ERROR_NO_AGGREGATION = (  -2147221232)
NS_ERROR_NOT_AVAILABLE = (  -2147221231)
NS_ERROR_FACTORY_NOT_REGISTERED = (  -2147221164)
NS_ERROR_FACTORY_REGISTER_AGAIN = (  -2147221163)
NS_ERROR_FACTORY_NOT_LOADED = (  -2147221000)
NS_ERROR_FACTORY_NO_SIGNATURE_SUPPORT = \
                                           (NS_ERROR_BASE + 257)
NS_ERROR_FACTORY_EXISTS = (NS_ERROR_BASE + 256)
NS_ERROR_PROXY_INVALID_IN_PARAMETER = (  -2147418096)
NS_ERROR_PROXY_INVALID_OUT_PARAMETER = (  -2147418095)

##### END OF GENERATED CODE
#####
def NS_ERROR_GENERATE_FAILURE(module,code):
	# slightly optimized, and avoids 2.3->2.4 long/int changes
	# return (NS_ERROR_SEVERITY_ERROR<<31) | ((module+NS_ERROR_MODULE_BASE_OFFSET)<<16) | (code)
	return -2147483648 | ((module+NS_ERROR_MODULE_BASE_OFFSET)<<16) | (code)

def NS_ERROR_GENERATE_SUCCESS(module,code):
	#return (NS_ERROR_SEVERITY_SUCCESS<<31) | ((module+NS_ERROR_MODULE_BASE_OFFSET)<<16) | (code)
	return ((module+NS_ERROR_MODULE_BASE_OFFSET)<<16) | (code)

NS_BASE_STREAM_CLOSED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_BASE, 2)
NS_BASE_STREAM_OSERROR = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_BASE, 3)
NS_BASE_STREAM_ILLEGAL_ARGS = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_BASE, 4)
NS_BASE_STREAM_NO_CONVERTER = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_BASE, 5)
NS_BASE_STREAM_BAD_CONVERSION = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_BASE, 6)
NS_BASE_STREAM_WOULD_BLOCK = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_BASE, 7)
NS_ERROR_FILE_UNRECOGNIZED_PATH = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 1)
NS_ERROR_FILE_UNRESOLVABLE_SYMLINK = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 2)
NS_ERROR_FILE_EXECUTION_FAILED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 3)
NS_ERROR_FILE_UNKNOWN_TYPE = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 4)
NS_ERROR_FILE_DESTINATION_NOT_DIR = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 5)
NS_ERROR_FILE_TARGET_DOES_NOT_EXIST = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 6)
NS_ERROR_FILE_COPY_OR_MOVE_FAILED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 7)
NS_ERROR_FILE_ALREADY_EXISTS = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 8)
NS_ERROR_FILE_INVALID_PATH = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 9)
NS_ERROR_FILE_DISK_FULL = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 10)
NS_ERROR_FILE_CORRUPTED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 11)
NS_ERROR_FILE_NOT_DIRECTORY = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 12)
NS_ERROR_FILE_IS_DIRECTORY = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 13)
NS_ERROR_FILE_IS_LOCKED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 14)
NS_ERROR_FILE_TOO_BIG = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 15)
NS_ERROR_FILE_NO_DEVICE_SPACE = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 16)
NS_ERROR_FILE_NAME_TOO_LONG = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 17)
NS_ERROR_FILE_NOT_FOUND = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 18)
NS_ERROR_FILE_READ_ONLY = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 19)
NS_ERROR_FILE_DIR_NOT_EMPTY = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 20)
NS_ERROR_FILE_ACCESS_DENIED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_FILES, 21)

## from netCore.h
NS_ERROR_ALREADY_CONNECTED =  NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 11)

NS_ERROR_NOT_CONNECTED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 12)
NS_ERROR_IN_PROGRESS = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 15)
NS_ERROR_OFFLINE = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 16)

## from nsISocketTransportService.idl
NS_ERROR_CONNECTION_REFUSED = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 13)

NS_ERROR_NET_TIMEOUT = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 14)

# Status nsresult codes: used with nsIProgressEventSink::OnStatus 
NS_NET_STATUS_RESOLVING_HOST  = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 3)
NS_NET_STATUS_CONNECTED_TO    = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 4)
NS_NET_STATUS_SENDING_TO      = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 5)
NS_NET_STATUS_RECEIVING_FROM  = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 6)
NS_NET_STATUS_CONNECTING_TO   = NS_ERROR_GENERATE_FAILURE(NS_ERROR_MODULE_NETWORK, 7)

# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf8 -*-
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

u"""Store global configuration information"""

import os
import sys
import socket

from duplicity import __version__


# The current version of duplicity
version = __version__

# Prefix for all files (appended before type-specific prefixes)
file_prefix = b""

# Prefix for manifest files only
file_prefix_manifest = b""

# Prefix for archive files only
file_prefix_archive = b""

# Prefix for sig files only
file_prefix_signature = b""

# The name of the current host
hostname = socket.gethostname()

# For historical reasons also save the FQDN for comparing manifests, but
# we tend to prefer the hostname going forward.
fqdn = socket.getfqdn()

# The main local path.  For backing up the is the path to be backed
# up.  For restoring, this is the destination of the restored files.
local_path = None

# The symbolic name of the backup being operated upon.
backup_name = None

# For testing -- set current time
current_time = None

# Set to the Path of the archive directory (the directory which
# contains the signatures and manifests of the relevent backup
# collection), and for checkpoint state between volumes.
# NOTE: this gets expanded in duplicity.commandline
os.environ[u"XDG_CACHE_HOME"] = os.getenv(u"XDG_CACHE_HOME", os.path.expanduser(u"~/.cache"))
archive_dir = os.path.expandvars(u"$XDG_CACHE_HOME/duplicity")
archive_dir_path = None

# config dir for future use
os.environ[u"XDG_CONFIG_HOME"] = os.getenv(u"XDG_CONFIG_HOME", os.path.expanduser(u"~/.config"))
config_dir = os.path.expandvars(u"$XDG_CONFIG_HOME/duplicity")

# Restores will try to bring back the state as of the following time.
# If it is None, default to current time.
restore_time = None

# If set, restore only the subdirectory or file specified, not the
# whole root.
restore_dir = None

# The backend representing the remote side
backend = None

# Are errors fatal (set for retry decorator in backend.py)
# See example of use in multibackend.py _list()
# Do not use in normal cases!
are_errors_fatal = {
    u'delete': (True, None),
    u'get': (True, None),
    u'list': (True, None),
    u'move': (True, None),
    u'put': (True, None),
    u'query': (True, None),
}

# If set, the Select object which iterates paths in the local
# source directory.
select = None

gpg_binary = None

# Set to GPGProfile that will be used to compress/uncompress encrypted
# files.  Replaces encryption_keys, sign_key, and passphrase settings.
gpg_profile = None

# Options to pass to gpg
gpg_options = u''

# Maximum file blocksize
max_blocksize = 2048

# If true, filelists and directory statistics will be split on
# nulls instead of newlines.
null_separator = None

# number of retries on network operations
num_retries = 5

# True if Pydev debugger should be activated
pydevd = False

# Character used like the ":" in time strings like
# 2002-08-06T04:22:00-07:00.  The colon isn't good for filenames on
# windows machines.
time_separator = u":"

# Global lockfile used to manage concurrency
lockpath = u""
lockfile = None

# If this is true, only warn and don't raise fatal error when backup
# source directory doesn't match previous backup source directory.
allow_source_mismatch = None

# If set, abort if cannot do an incremental backup.  Otherwise if
# signatures not found, default to full.
incremental = None

# If set, print the statistics after every backup session
print_statistics = True

# If set, use short (< 30 char) filenames for all the remote files.
short_filenames = False

# If set, forces a full backup if the last full backup is older than
# the time specified
full_force_time = None

# Used to confirm certain destructive operations like deleting old files.
force = None

# If set, signifies time in seconds before which backup files should
# be deleted.
remove_time = None

# If set, signifies the number of backups chains to keep when performing
# a remove-all-but-n-full.
keep_chains = None

# If set, signifies that remove-all-but-n-full in progress
remove_all_but_n_full_mode = None

# If set, signifies that remove-all-inc-of-but-n-full in progress (variant of remove-all-but-n-full)
remove_all_inc_of_but_n_full_mode = None

# Don't actually do anything, but still report what would be done
dry_run = False

# If set to false, then do not encrypt files on remote system
encryption = True

# If set to false, then do not compress files on remote system
compression = True

# volume size. default 200M
volsize = 200 * 1024 * 1024

# after this volume, we will switch to multipart upload
mp_factor = 1.1
mp_segment_size = mp_factor * volsize

# Working directory for the tempfile module. Defaults to /tmp on most systems.
temproot = None

# network timeout value
timeout = 30

# FTP data connection type
ftp_connection = u'passive'

# Protocol for webdav
webdav_proto = u'http'

# Asynchronous put/get concurrency limit
# (default of 0 disables asynchronicity).
async_concurrency = 0

# Whether to use "new-style" subdomain addressing for S3 buckets. Such
# use is not backwards-compatible with upper-case buckets, or buckets
# that are otherwise not expressable in a valid hostname.
s3_use_new_style = False

# Whether to create European buckets (sorry, hard-coded to only
# support european for now).
s3_european_buckets = False

# File owner uid keeps number from tar file. Like same option in GNU tar.
numeric_owner = False

# Do no restore the uid/gid when finished, useful if you're restoring
# data without having root privileges or Unix users support
do_not_restore_ownership = False

# Whether to use plain HTTP (without SSL) to send data to S3
# See <https://bugs.launchpad.net/duplicity/+bug/433970>.
s3_unencrypted_connection = False

# Whether to use S3 Reduced Redudancy Storage
s3_use_rrs = False

# Whether to use S3 Infrequent Access Storage
s3_use_ia = False

# Whether to use S3 Glacier Storage
s3_use_glacier = False

# Whether to use S3 Glacier IR Storage
s3_use_glacier_ir = False

# Whether to use S3 Glacier Deep Archive Storage
s3_use_deep_archive = False

# Whether to use S3 One Zone Infrequent Access Storage
s3_use_onezone_ia = False

# True if we should use boto multiprocessing version
s3_use_multiprocessing = False

# Chunk size used for S3 multipart uploads.The number of parallel uploads to
# S3 be given by chunk size / volume size. Use this to maximize the use of
# your bandwidth. Defaults to 25MB
s3_multipart_chunk_size = 25 * 1024 * 1024

# Minimum chunk size accepted by S3
s3_multipart_minimum_chunk_size = 5 * 1024 * 1024

# Maximum number of processes to use while doing a multipart upload to S3
s3_multipart_max_procs = None

# Maximum time to wait for a part to finish when doig a multipart upload to S3
s3_multipart_max_timeout = None

# Use server side encryption in s3
s3_use_sse = False

# Use server side kms encryption in s3
s3_use_sse_kms = False
s3_kms_key_id = None
s3_kms_grant = None

# region and endpoint of s3
s3_region_name = None
s3_endpoint_url = None

# Which storage policy to use for Swift containers
swift_storage_policy = u""

# The largest size upload supported in a single put call for azure
azure_max_single_put_size = None

# The size of the blocks put to azure blob storage if bigger than azure_max_single_put_size
azure_max_block_size = None

# Maximum number of parallel connections to use when the blob size for azure exceeds 64MB
azure_max_connections = None

# Standard storage tier used for storring backup blobs (Hot|Cool|Archive).
azure_blob_tier = None

# Whether to use the full email address as the user name when
# logging into an imap server. If false just the user name
# part of the email address is used.
imap_full_address = False

# Name of the imap folder where we want to store backups.
# Can be changed with a command line argument.
imap_mailbox = u"INBOX"

# Sync partial metadata by default
metadata_sync_mode = u"partial"

# Whether the old filename format is in effect.
old_filenames = False

# Wheter to specify --use-agent in GnuPG options
use_agent = False

# ssh commands to use, used by ssh_pexpect (defaults to sftp, scp)
scp_command = None
sftp_command = None

# default to batch mode using public-key encryption
ssh_askpass = False

# user added ssh options
ssh_options = u""

# default cf backend is pyrax
cf_backend = u"pyrax"

# default to fully deleting files in b2
b2_hide_files = False

# HTTPS ssl options (currently only webdav, lftp)
ssl_cacert_file = None
ssl_cacert_path = None
ssl_no_check_certificate = False

# user added rsync options
rsync_options = u""

# will be a Restart object if restarting
restart = None

# used in testing only - raises exception after volume
fail_on_volume = 0

# used in testing only - skips uploading a particular volume
skip_volume = 0

# ignore (some) errors during operations; supposed to make it more
# likely that you are able to restore data under problematic
# circumstances. the default should absolutely always be True unless
# you know what you are doing.
ignore_errors = False

# Renames (--rename)
rename = {}

# enable data comparison on verify runs
compare_data = False

# When symlinks are encountered, the item they point to is copied rather than
# the symlink.
copy_links = False

# When selected, triggers a dry-run before a full or incremental to compute
# changes, then runs the real operation and keeps track of the real progress
progress = False

# Controls the upload progress messages refresh rate. Default: update each
# 3 seconds
progress_rate = 3

# Level of Redundancy in % for Par2 files
par2_redundancy = 10

# Verbatim par2 other options
par2_options = u""

# Number of par2 volumes
par2_volumes = 1

# Whether to enable gio backend
use_gio = False

# If set, log the chnages is the set instead of the normal collection status
show_changes_in_set = None

# If set, collect only the file status, not the whole root.
file_changed = None

# If set, skip collecting the files_changed list in statistics, nullifies --file-changed
no_files_changed = False

# delay (in seconds) before next operation after failure
backend_retry_delay = 30

# option for mediafire to purge files on delete instead of sending to trash
mf_purge = False

# Fake root directory path for iDrived backend
fakeroot = None

# default filesystem encoding
# In Python 2 it seems that sys.getfilesystemencoding() will normally return
# 'utf-8' or some other sane encoding, but will sometimes fail and return
# either 'ascii' or None.  Both are bogus, so default to 'utf-8' if it does.
fsencoding = sys.getfilesystemencoding()
fsencoding = fsencoding if fsencoding not in [u'ascii', u'ANSI_X3.4-1968', None] else u'utf-8'

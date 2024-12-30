DISCLAIMER - ABANDONED/UNMAINTAINED CODE / DO NOT USE
=======================================================
While this repository has been inactive for some time, this formal notice, issued on **December 10, 2024**, serves as the official declaration to clarify the situation. Consequently, this repository and all associated resources (including related projects, code, documentation, and distributed packages such as Docker images, PyPI packages, etc.) are now explicitly declared **unmaintained** and **abandoned**.

I would like to remind everyone that this project’s free license has always been based on the principle that the software is provided "AS-IS", without any warranty or expectation of liability or maintenance from the maintainer.
As such, it is used solely at the user's own risk, with no warranty or liability from the maintainer, including but not limited to any damages arising from its use.

Due to the enactment of the Cyber Resilience Act (EU Regulation 2024/2847), which significantly alters the regulatory framework, including penalties of up to €15M, combined with its demands for **unpaid** and **indefinite** liability, it has become untenable for me to continue maintaining all my Open Source Projects as a natural person.
The new regulations impose personal liability risks and create an unacceptable burden, regardless of my personal situation now or in the future, particularly when the work is done voluntarily and without compensation.

**No further technical support, updates (including security patches), or maintenance, of any kind, will be provided.**

These resources may remain online, but solely for public archiving, documentation, and educational purposes.

Users are strongly advised not to use these resources in any active or production-related projects, and to seek alternative solutions that comply with the new legal requirements (EU CRA).

**Using these resources outside of these contexts is strictly prohibited and is done at your own risk.**

Regarding the potential transfer of the project to another entity, discussions are ongoing, but no final decision has been made yet. As a last resort, if the project and its associated resources are not transferred, I may begin removing any published resources related to this project (e.g., from PyPI, Docker Hub, GitHub, etc.) starting **March 15, 2025**, especially if the CRA’s risks remain disproportionate.

# INSTALLATION

Thank you for trying duplicity.  To install, run:

```
python setup.py install
```

The build process can be also be run separately:

```
python setup.py build
```

If you want to use python 3 replace the `python` command with `python3`

The default prefix is /usr, so files are put in /usr/bin,
/usr/share/man/, etc.  An alternate prefix can be specified using the
--prefix=<prefix> option.  For example:

```
python setup.py install --prefix=/usr/local
export PYTHONPATH='/usr/local/lib/python.x/site-packages/'
/usr/local/bin/duplicity -V`
```

# REQUIREMENTS

 * Python 2.7, or 3.5 to 3.9
 * librsync v0.9.6 or later
 * GnuPG for encryption
 * fasteners 0.14.1 or later for concurrency locking
 * for scp/sftp -- python-paramiko
 * for ftp -- lftp version 3.7.15 or later
 * Boto 2.0 or later for single-processing S3 or GCS access (default)
 * Boto 2.1.1 or later for multi-processing S3 access
 * Boto 2.7.0 or later for Glacier S3 access
 * Boto3 1.15 or later for S3

If you install from the source package, you will also need:

 * Python development files, normally found in module 'python-dev'.
 * librsync development files, normally found in module 'librsync-dev'.

Install python modules by performing the following command in duplicity's root directory:

```
pip install -r requirements.txt
```
or:

```
pip3 install -r requirements.txt
```
if you're using python3

# DEVELOPMENT

For more information on downloading duplicity's source code from the
code repository and developing for duplicity, see README-REPO.

# HELP

For more information see the duplicity home page at:

  http://www.nongnu.org/duplicity

or post to the mailing list at

  https://lists.nongnu.org/mailman/listinfo/duplicity-talk
